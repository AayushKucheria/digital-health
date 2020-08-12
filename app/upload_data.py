'''
Upload csv data to database
'''

import csv
import glob
import re

import numpy as np
from sqlalchemy.orm import Session
import pandas as pd

import crud
from database import SessionLocal

messages = []
chosen = []


def csv_to_list():
    """
    Show user all filenames in folder: "data/" and ask to choose.\n
    Then, for each chosen csv, append the data to messages
    
    :return: Unit
    """
    global messages, chosen

    file_list = glob.glob("data/*.csv")

    # If there are multiple csv files, ask to specify
    if len(file_list) > 1:
        print("Available Files:", file_list)
        names = input(
            "Please copy files you want to upload and separate them with comma: ")  # TODO: Add checkbox view to web?

        if names != "":
            a = names.split(',')  # All files to read separated by ","
            a = map(str.strip, a)  # Remove whitespaces from the sides
            for elem in a:
                if elem != "":
                    chosen.append(elem)

    else:  # Only 1 data file in folder
        chosen.append(file_list[0])

    # Append chosen csv files data to list
    for j in chosen:
        with open(j, 'r') as read_obj:
            messages.append(pd.read_csv(read_obj))


# Find the max session for Patient and return max + 1 for next session
def session(mtype: str, mid: int, all_tables: np.array):
    """
    Finds the max session number for patient in Database and returns
    max + 1 as the newest session number.
    
    :param mtype: Current Recording type (Eeg or Emg)
    :param mid: Current Patient ID
    :param all_tables: Details of all tables in DB: (Recording Type, Patient ID, Session number) 
    :return: Current Session number (last + 1)
    """
    sessions = [1]
    for i in all_tables:
        if i[0] == mtype and int(i[1]) == mid:
            sessions.append(int(i[2]))  # Append session number for i
    return max(sessions) + 1  


if __name__ == "__main__":

    # Inserting csv values in list of list 'messages'
    csv_to_list()
    for i in messages:
        print(i.head(5))

    # Get data out from filenames and sort it wrt time: (type, name, time)
    table_names = []
    for filename in chosen:
        table_names.append(
            re.search("data/(.*?).csv", filename).group(1))  # Gets "Emg_Aayush_Time" from csv path
    table_names.sort(key=lambda x: float(x.split('_')[2]))  # Sorting wrt time

    db: Session = SessionLocal()

    # Set table name (acc to DB), create the table, and upload data to it
    for curr_table in table_names:
        
        data = curr_table.split('_')  # (type, name, time)
        recording_type: str = str(data[0]).lower()
        name = str(data[1]).lower()
        print("Name: ", name)
        print("Recording Type: ", recording_type)
        # Check if patient with this name exists in DB
        patient = crud.get_patient_by_name(db, name)
        if patient is None:
            print("Patient doesn't exist. Create patient first.")
        
        # All is okay, continue.
        # Get all table names from db --> Get new session number for this patient
        # --> Set tableName (replace time with session)
        # --> Create table in DB --> Send data to the table
        else:
            db_tables = crud.get_session_tables(db)
            db_tableName_data = np.array([x.split('_') for x in db_tables])  # Array of (type, id, session number)
            print("Filtered Table Data: ", db_tableName_data)
            # Get relevant table name
            session_number = session(recording_type, int(patient.id), db_tableName_data)
            # finalName = str(patient.id) + "_" + str(session_number)
            # finalName = crud.create_emg_table(db, str(finalName))  # (database, table name)

            finalName = str(recording_type) + "_" + str(patient.id) + "_" + str(session_number)
            path = "data/" + data[0] + "_" + data[1] + "_" + data[2] + ".csv"
            print("FinalName: ", finalName)
            # Send data to database
            crud.send_data(db, csv_path=path, tablename=finalName)
