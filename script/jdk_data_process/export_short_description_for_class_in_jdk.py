from util.jdk_data_export import export_class_short_description_from_jdk
from util.json_util import write_json_to_file

description_json = export_class_short_description_from_jdk()

write_json_to_file("jdk_class_short_description.json", description_json)
