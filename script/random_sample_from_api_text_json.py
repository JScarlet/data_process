import sys

from util.json_util import random_sample_from_api_text_json

reload(sys)
sys.setdefaultencoding('utf-8')
if len(sys.argv) > 1:
    input_json_file_list = sys.argv[1:]
    for input_json_file in input_json_file_list:
        random_sample_from_api_text_json(input_json_file)
