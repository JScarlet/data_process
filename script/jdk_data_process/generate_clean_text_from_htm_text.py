import json
import sys

from util.code_text_process import clean_html_text_with_replacement
from util.json_util import write_json_to_file

reload(sys)
sys.setdefaultencoding('utf-8')

'''
read the jdk_html.json,
generate the clean text by remove tags in html and replace large code elements.
extract the simple html link relation from html
'''
jdk_html_json = json.load(open("jdk_html.json"))
clean_text = []
for jdk_html in jdk_html_json:
    clean_text.append({"text": clean_html_text_with_replacement(jdk_html["html_body"])})
    base_url = ""

write_json_to_file("jdk_clean_text.json", clean_text)
