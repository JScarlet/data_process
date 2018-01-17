import codecs
import json
import sys

if len(sys.argv) <= 3:
    print "must specific the json file for combining"
    sys.exit(1)
combined_json_file_name = sys.argv[1]
json_file_name_list = sys.argv[2:]

print json_file_name_list
conbined_json = []
for json_file_name in json_file_name_list:
    # Reading data back
    with codecs.open(json_file_name, 'r', 'utf-8') as f:
        data = json.load(f)
        conbined_json.extend(data)
with codecs.open(combined_json_file_name, 'w', 'utf-8') as out_put_file:
    json.dump(conbined_json, out_put_file)
