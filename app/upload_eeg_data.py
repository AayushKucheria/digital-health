'''
Pick relevant columns from emotiv eeg csv file and upload to database
'''

import glob
import re
import pandas as pd

def get_data_from_csv():
    """
    Select eeg csv files in data folder.
    Pick relevant columns and store to list
    :return:
    """

    messages = []

    file_list = glob.glob("data/eeg/*.csv")

    for i in file_list:
        with open(i, 'r') as read_obj:
            initial = pd.read_csv(read_obj, usecols=['Timestamp', 'EEG.AF3', 'EEG.T7', 'EEG.Pz', 'EEG.T8', 'EEG.AF4'])
            print(initial[0:5])