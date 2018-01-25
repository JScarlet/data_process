import json
import sys

from util.json_util import write_json_to_file
from util.code_text_process import clean_html_text_with_replacement
from util.html_relation_extractor import extract_relation_from_html

reload(sys)
sys.setdefaultencoding('utf-8')

'''
read the jdk_html.json,
generate the clean text by remove tags in html and replace large code elements.
extract the simple html link relation from html
'''
jdk_html_json = json.load(open("jdk_html.json"))

clean_text = []
relation_set = set([])

base_url_list = ["http://docs.oracle.com/javase/1.5.0/docs/api",
                 "http://docs.oracle.com/javase/6/docs/api",
                 "http://docs.oracle.com/javase/7/docs/api",
                 "http://docs.oracle.com/javase/8/docs/api"]
for jdk_html in jdk_html_json:
    clean_text.append({"text": clean_html_text_with_replacement(jdk_html["html_body"])})
    base_url = ""
    for url in base_url_list:
        if url in jdk_html["doc_website"]:
            base_url = url
            break

    relation_set = relation_set.union(extract_relation_from_html(jdk_html["html_body"], base_url=base_url))

relations_json = []
for relation in relation_set:
    relations_json.append(relation.to_json())

write_json_to_file("jdk_relation_from_html.json", relations_json)
write_json_to_file("jdk_clean_text.json", clean_text)
