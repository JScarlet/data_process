import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def write_json_to_file(file_name, data):
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)


def read_json_from_file(file_name):
    # Reading data back
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data
