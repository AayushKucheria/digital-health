'''
List of important data
'''

host = 'ec2-34-197-188-147.compute-1.amazonaws.com'
port = 5432
database = 'db2rqfi8hqb9l5'
user = 'qrutnlncgfznek'
password = 'ca0781860fbb93e669ec0c0ca760ad32ae1c84d5e1580f6bc11aa4ec3c6d8764'

# Commands
# Set heroku app--> heroku git:remote -a digital-health-protopaja
# Run app --> uvicorn main:app --reload
# Start SQL Queries --> psql -h ec2-34-197-188-147.compute-1.amazonaws.com -U qrutnlncgfznek db2rqfi8hqb9l5
# Exit SQL Queries --> \q

# SQL QUERIES
# Insert new patient --> INSERT INTO patients (age, sex, name) VALUES (14, 'Male', 'Aayush'), ...;
# Get all patients --> SELECT * FROM patients;

# GANGLION BOARD DETAILS
# board_id: 1
# serial_port field of BrainFlowInputParams structure
# mac_address field of BrainFlowInputParams structure, if its empty BrainFlow will try to autodiscover Ganglion
# optional: timeout field of BrainFlowInputParams structure, default is 15sec
