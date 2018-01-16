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

with codecs.open('jdk_corpus.txt', 'w', 'utf-8') as corpus_file:
    for text_part_json in data:
        corpus_file.writelines(text_part_json['text'].replace('\n', " "))
        corpus_file.write("\n")
