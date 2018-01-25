from util.jdk_data_export import export_parameter_from_method_for_jdk
from util.json_util import write_json_to_file

description_json = export_parameter_from_method_for_jdk()

write_json_to_file("jdk_parameter_detail_description.json", description_json)
