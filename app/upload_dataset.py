'''
Upload all files in the bonn_dataset folder to database
'''

import glob
import re

import pandas as pd
from database import engine

if __name__ == "__main__":

    file_list = glob.glob("data/bonn_dataset/*.csv")
    df = []

    # Save name and contents of each file as a dataframe to df (list)
    # The name will act as the tablename and the contents the values inside the table
    for i in range(0, len(file_list)):
        name = re.search("data/bonn_dataset/(.*?).csv", file_list[i]).group(1)
        with open(file_list[i], 'r') as read_obj:
            df.append((name, pd.read_csv(read_obj, index_col=0)))

    connection = engine.connect()

    try:
        for i in df:  # For each dataframe, upload it to database
            try:
                name = i[0]
                values = i[1]
                frame = values.to_sql(name, connection, if_exists='replace')
            except ValueError as vx:
                print(vx)
            except Exception as ex:
                print(ex)
            else:
                print("PostgreSQL Table %s has been created successfully." % name)
    finally:
        connection.close()
