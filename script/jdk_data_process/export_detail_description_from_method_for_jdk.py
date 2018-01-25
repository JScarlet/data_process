from util.jdk_data_export import export_method_detail_description_from_jdk
from util.json_util import write_json_to_file

exception_json = export_method_detail_description_from_jdk()

write_json_to_file("jdk_method_detail_description.json", exception_json)
