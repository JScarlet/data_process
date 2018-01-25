import sys

from util.android_data_export import android_html_data_process
from util.code_text_process import clean_html_text_with_replacement
from util.html_relation_extractor import extract_relation_from_html
from util.json_util import write_json_to_file

reload(sys)
sys.setdefaultencoding('utf-8')

'''
read the jdk_html.json,
generate the clean text by remove tags in html and replace large code elements.
extract the simple html link relation from html
'''

android_sdk_html_json = android_html_data_process()
write_json_to_file("android_sdk_html.json", android_sdk_html_json)

clean_text = []
relation_set = set([])

document_link_relation_json = []

for android_html in android_sdk_html_json:
    clean_text.append({"text": clean_html_text_with_replacement(android_html["html_body"])})
    base_url = android_html["doc_website"]
    relation_set_from_html_body = relation_set.union(
        extract_relation_from_html(android_html["html_body"], base_url=base_url))
    relation_set = relation_set_from_html_body
    relations_json = []
    for relation in relation_set_from_html_body:
        document_link_relation_json_item = {"doc_website": android_html["doc_website"]}
        relations_json.append(relation.to_json())
        document_link_relation_json_item["link_relations"] = relations_json
        document_link_relation_json.append(document_link_relation_json_item)

relations_json = []
for relation in relation_set:
    relations_json.append(relation.to_json())

write_json_to_file("android_link_relation_from_html.json", relations_json)
write_json_to_file("android_contain_link_relation_from_html.json", document_link_relation_json)
write_json_to_file("android_sdk_clean_text.json", clean_text)
