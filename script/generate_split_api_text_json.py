import sys

from util.json_util import api_text_json_sentence_split

reload(sys)
sys.setdefaultencoding('utf-8')
if len(sys.argv) > 1:
    input_json_file_list = sys.argv[1:]
    for input_json_file in input_json_file_list:
        api_text_json_sentence_split(input_json_file)
