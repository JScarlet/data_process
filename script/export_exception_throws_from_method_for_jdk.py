from util.jdk_data_export import export_exception_throw_from_method_for_jdk
from util.json_util import write_json_to_file

exception_json = export_exception_throw_from_method_for_jdk()

write_json_to_file("jdk_exception.json", exception_json)
