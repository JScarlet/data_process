import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def write_json_to_file(file_name, data):
    with open(file_name, 'w') as file_object:
        json.dump(data, file_object)