#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import json
import sys

import fasttext


def __read_json_from_file(file_name):
    # Reading data back
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = json.load(f)
    return data


def __write_json_to_file(file_name, data):
    with codecs.open(file_name, 'w', encoding='utf8') as json_file:
        data = json.dumps(data, ensure_ascii=False, encoding='utf8')
        json_file.write(unicode(data))


reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) <= 2:
    print "must specific model file and the json waited for annotation"
    sys.exit(1)

model_file_path = sys.argv[1]
json_path = sys.argv[2]
sentence_model = fasttext.load_model(model_file_path)

api_json_data = __read_json_from_file(json_path)
for api_json_data_item in api_json_data:
    api_text = api_json_data_item["text"]
    api_text = api_text.split("\n", " ")

    label, probability = sentence_model.predict(api_text, k=1, threshold=0.0)
    probability = probability.tolist()

    api_json_data["knowledge_pattern"] = label.replace('__label__', "").replace("_", " ")
    api_json_data["knowledge_pattern_probability"] = probability
__write_json_to_file("fasttext_annotated_" + json_path, api_json_data)
