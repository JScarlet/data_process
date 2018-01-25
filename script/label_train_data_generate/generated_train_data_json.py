import codecs
import json

from util.json_util import conbine_json_file

combined_json_file_name = "label_sentence_json.json"
json_file_name_list = ["concept_simple_annotated_all_description.json",
                       "directive_simple_annotated_all_description.json",
                       "functionality and behavior_simple_annotated_all_description.json",
                       "value instance description_simple_annotated_all_description.json"
                       ]

print json_file_name_list
conbined_json = conbine_json_file(json_file_name_list)
with codecs.open(combined_json_file_name, 'w', 'utf-8') as out_put_file:
    json.dump(conbined_json, out_put_file)
