import requests

to_predict_dict = {'satisfaction_level': 0.38,
                   'last_evaluation': 0.53,
                   'number_project': 2,
                   'average_montly_hours': 157,
                   'time_spend_company': 3,
                   'Work_accident': 0,
                   'promotion_last_5years': 0,
                   'sales': 'support',
                   'salary': 'low'}

url = 'http://127.0.0.1:8000/predict'
r = requests.post(url, json=to_predict_dict);
r.json()
