#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) <= 1:
    print "must specific the json file for training fastText word embedding"
    sys.exit(1)

json_file_name = sys.argv[1]

# Reading data back
with open(json_file_name, 'r') as f:
    data = json.load(f)

out_put_file_name = sys.argv[2]
with codecs.open(out_put_file_name, 'w', 'utf-8') as corpus_file:
    for text_part_json in data:
        all_text = text_part_json['text']
        # sentences = sentence_split(all_text)
        # for sentence in sentences:
        #     corpus_file.write(sentence)
        #     corpus_file.write("\n")
        corpus_file.write(all_text)
        corpus_file.write("\n")
