import sys

from util.json_util import annotated_by_sentence_index

reload(sys)
sys.setdefaultencoding('utf-8')
if len(sys.argv) > 1:
    input_json_file_list = sys.argv[1:]
    for input_json_file in input_json_file_list:
        annotated_by_sentence_index(input_json_file)
