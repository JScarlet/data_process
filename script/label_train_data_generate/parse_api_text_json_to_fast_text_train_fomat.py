import sys

from util.json_util import parse_api_text_json_to_fast_text_train_format

reload(sys)
sys.setdefaultencoding('utf-8')

input_json_file = "label_sentence_json.json"
parse_api_text_json_to_fast_text_train_format(input_json_file)
