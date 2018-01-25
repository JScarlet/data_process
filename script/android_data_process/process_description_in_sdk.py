from util.json_util import generate_annotated_json_object, write_json_to_file
from util.sdk_data_export import export_class_description_from_sdk, export_package_description_from_sdk, \
    export_method_description_from_sdk

package_description_json = export_package_description_from_sdk()
write_json_to_file("sdk_package_description.json", package_description_json)

class_description_json = export_class_description_from_sdk()
write_json_to_file("sdk_class_description.json", class_description_json)

method_description_json = export_method_description_from_sdk()
write_json_to_file("sdk_method_description.json", method_description_json)

description_json = []
for item in package_description_json:
    description_json.append(item)
for item in class_description_json:
    description_json.append(item)
for item in method_description_json:
    description_json.append(item)

write_json_to_file("sdk_all_description.json", description_json)

annotated_description_object = generate_annotated_json_object(description_json)
write_json_to_file("annotated_sdk_all_description.json", description_json)
