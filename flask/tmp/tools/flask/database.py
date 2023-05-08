# Flask Database
import os
import json

info = {
    'sys': {
        # Set Url website
        'Url': 'http://127.0.0.1',
    },
    'title': '100 Number',
    'lens': 101,
}


def save_database(data):
    try:
        file_path = os.path.join(os.getcwd(), 'database.json')
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump({}, f)
            with open(file_path, 'r') as f:
                jsonData = json.load(f)
                jsonData.update(data)
            with open(file_path, 'w') as f:
                json.dump(jsonData, f)
    except Exception as e:
        print(e)
