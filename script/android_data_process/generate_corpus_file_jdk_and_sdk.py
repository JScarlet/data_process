#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

json_file_name_list = ["jdk_clean_text.json", "sdk_clean_text.json"]

out_put_file_name = "api_document_corpus.txt"
with codecs.open(out_put_file_name, 'w', 'utf-8') as corpus_file:
    # Reading data back
    for json_file_name in json_file_name_list:
        with codecs.open(json_file_name, 'r', 'utf-8') as f:
            data = json.load(f)
            for text_part_json in data:
                all_text = text_part_json['text']
                corpus_file.write(all_text)
                corpus_file.write("\n")
