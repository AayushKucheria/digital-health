'''
TODO: Write code to remove title line once the integration is done. Rn I removed it manually
TODO: Until then, delete row 1 in csv file and also have less rows.
Pick relevant columns from emotiv eeg csv file and upload to database
Filenames must be of the form: "data/eeg/(.*?).md.csv"
'''
import argparse
import glob
import re
import pandas as pd
from app.database import SessionLocal
from sqlalchemy.orm import Session
import app.crud as crud
import numpy as np
import os
from pathlib import Path

messages = []
file_list = []


def get_data_from_csv():
    """
    Select eeg csv files in data/eeg folder.
    Pick relevant columns and store in list
    :return:
    """
    global messages, file_list
    messages = []

    file_list = glob.glob("data/eeg/*.csv")

    for i in file_list:
        with open(i, 'r') as read_obj:
            messages.append(
                pd.read_csv(read_obj, usecols=['Timestamp', 'EEG.AF3', 'EEG.T7', 'EEG.Pz', 'EEG.T8', 'EEG.AF4']))


# Find the max session for Patient and return max + 1 for next session
def session(mtype: str, mid: int, all_tables: np.array):
    """
    Finds the max session number for patient in Database and returns
    max + 1 as the newest session number.

    :param mtype: Current Recording type (Eeg or Emg)
    :param mid: Current Patient ID
    :param all_tables: Details of all tablenames in DB: ["session", "eeg", "patient_id", "session_id"]
    :return: Current Session number (max_in_db + 1)
    """
    sessions = [0]
    for i in all_tables:
        if i[1] == mtype and int(i[2]) == mid:
            sessions.append(int(i[3]))  # Append session number for i
    return max(sessions) + 1


def start(patient_id: int):
    db: Session = SessionLocal()

    # Inserting csv values in list of list 'messages'
    get_data_from_csv()

    # # Sort files wrt time: (type, name, time)
    # half_file_names = []
    # for filename in file_list:
    #     half_file_names.append(
    #         re.search("data/eeg/(.*?).md.csv", filename).group(1))  # Gets "eeg_number_date_time" from csv path
    #     # TODO: Sort wrt absolute timestamp in files
    # half_file_names.sort(key=lambda x: float(x.split('_')[3]))  # Sorting wrt time # Not date, note this.

    # Set table name (acc to DB), create the table, and upload data to it
    for curr_file in file_list:
        name = re.search("data/eeg/(.*?).md.csv", curr_file).group(1)
        data = name.split('_')  # (eeg_number_date_time)
        # recording_type: str = str(data[0]).lower()
        # number = str(data[1]).lower()

        # Check if patient with this name exists in DB
        patient = crud.get_patient_by_id(db, patient_id)
        if patient is None:
            print("Patient doesn't exist. Create patient first.")

        # All is okay, continue.
        # Fetch tablenames from the db, and calculate the session number for this file.
        # Once that's done, set the tablename and upload the table to the database.
        else:
            # Fetch tablenames
            db_session_tables = crud.get_session_tables(db)
            # Details of all tablenames in DB: ["session", "eeg", "patient_id", "session_id"]
            db_tableName_data = np.array(
                [x.split('_') for x in db_session_tables])

            # Get relevant session number
            session_number = session("eeg", int(patient.id), db_tableName_data)

            finalName = "session_" + "eeg_" + str(patient.id) + "_" + str(session_number)
            print("FinalName: ", finalName)

            # Send data to database
            for i in messages:
                is_sent = crud.send_data_from_df(db, tablename=finalName, df=i)

                if is_sent:
                    new_path = "data/uploaded/" + name + ".md.csv"
                    Path(curr_file).rename(new_path)
                    return True
                else:
                    return False


if __name__ == "__main__":
    # Get patient id from args parser else use default
    parser = argparse.ArgumentParser()
    parser.add_argument("--pid",
                        default=1, type=int, help="The patient id for these sessions?")
    args = parser.parse_args()
    print(args.pid)
    start(args.pid)
