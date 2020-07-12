import glob
import re
from _csv import reader

from sqlalchemy.orm import Session

import crud

from database import SessionLocal
import pandas as pd

name = ""
messages = []


# Convert csv file to pandas list
def csv_to_list():
    global name, messages

    print("Starting conversion for file. Please specify name.")
    file_list = glob.glob("data/*.csv")

    # If there are multiple csv files, ask to specify
    if len(file_list) > 1:
        print("Available Files:", file_list)
        name = input("Please enter file name (without path or .csv): ")

    if name != "":
        chosen = "data/" + name + ".csv"
    else:
        name = re.search(("data/(.*?).csv", file_list[0]))
        chosen = file_list[0]

    # Convert chosen csv file to list
    with open(chosen, 'r') as read_obj:
        csv_reader = reader(read_obj)
        messages = list(csv_reader)


if __name__ == "__main__":

    # Inserting csv values in list 'messages'
    csv_to_list()

    # Get id of the patient if any
    db: Session = SessionLocal()
    patient = crud.get_patient_by_name(db, name)

    # If ID Present, add list to new partition in existing table with name = "EMG_ID"
    # If ID not present, add list to new partition in new table with name = "EMG_ID"
    print(patient.id)
    tables_list = crud.get_tables_by_name(db)
    tables_list[:] = [s.replace('EMG_', '') for s in tables_list]  # Remove "EMG_" from table name and just keep id
    tables_df = pd.Series(tables_list)

    # print("Printing table names: ")
    # for i in tables_df:
    #     print(i)

    # TODO: @sophie this will change according to your schema
    if patient.id in tables_df:
        #  TODO: Add messages (list of data) to table or create new table for this session
        print(patient.id)
    else:  # If no EMG table for this patient, create a new one with "EMG_id" as name.
        crud.create_emg_table(db, patient.id)  # (database, table name)
        #  TODO: Add messages to table
