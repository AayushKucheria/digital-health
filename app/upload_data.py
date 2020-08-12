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

messages = [[]]
chosen = [[]]


# Convert csv files to lists
def csv_to_list():  # Works for multiple files
    global messages, chosen

    print("Starting conversion for file.")
    file_list = glob.glob("data/*.csv")

    # If there are multiple csv files, ask to specify
    if len(file_list) > 1:
        print("Available Files:", file_list)
        names = input(
            "Please copy files you want to upload and separate them with comma: ")  # TODO: Add checkbox view to web?

        if names != "":
            chosen = names.split(',')
    else:
        chosen = file_list[0]

    # Convert chosen csv files data to list
    for i in range(0, len(chosen)):
        with open(chosen[i], 'r') as read_obj:
            messages.append(pd.read_csv(read_obj))
            print(messages[i])
    # for i in range(0, len(chosen)):
    #     with open(chosen[i], 'r') as read_obj:
    #         csv_reader = csv.reader(read_obj)
    #         for row in csv_reader:
    #             messages[i].append(row)
    #         print(messages[i])


# Find the max session for Patient and return max + 1 for next session
def session(mtype: str, mid: int, all_tables: np.array):
    sessions = [1]
    for i in all_tables:
        if i[0] == mtype and i[1] == mid:
            sessions.append(i[2])
    return max(sessions) + 1


if __name__ == "__main__":

    # Inserting csv values in list of list 'messages'
    csv_to_list()

    # Get data out from filenames and sort it wrt time: (type, name, time)
    table_names = []
    for filename in chosen:
        table_names.append(
            re.search("data/(.*?).csv", filename).group(1))  # Gets table name from csv filename (the middle part)
    table_names.sort(key=lambda x: float(x.split('_')[2]))  # Sorting wrt time

    db: Session = SessionLocal()

    # For each list (session), get the needed patient data from db
    # And create new table to store the data
    i = 0
    for curr_table in table_names:
        # Get id of the patient if any
        data = curr_table.split('_')  # type, name, time
        recording_type: str = data[0]
        name = data[1]
        patient = crud.get_patient_by_name(db, name)

        if patient is None:
            print("Patient doesn't exist. Create patient first.")
        else:
            tables_list = crud.get_tables_by_name(db)
            table_list_data = np.array([x.split('_') for x in tables_list])  # Array of (type, id, session number)

            # Get relevant table name
            session_number = session(recording_type, patient.id, table_list_data)
            finalname = str(patient.id) + "_" + str(session_number)
            print(type(patient.id))
            finalname = crud.create_emg_table(db, str(finalname))  # (database, table name)

            path = "data/" + data[0] + "_" + data[1] + "_" + data[2] + ".csv"

            # Send data to database
            crud.send_data(db, csv_path=path, tablename=finalname)
        i += 1
