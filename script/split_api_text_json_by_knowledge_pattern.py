import sys

from util.json_util import split_api_text_json_by_knowledge_pattern

reload(sys)
sys.setdefaultencoding('utf-8')
if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    split_api_text_json_by_knowledge_pattern(input_json_file)
