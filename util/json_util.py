import codecs
import io
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def write_json_to_file(file_name, data):
    with io.open(file_name, 'w', encoding='utf8') as json_file:
        data = json.dumps(data, ensure_ascii=False, encoding='utf8')
        json_file.write(unicode(data))


def read_json_from_file(file_name):
    # Reading data back
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = json.load(f)
    return data
