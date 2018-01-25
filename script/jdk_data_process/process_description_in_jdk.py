from util.json_util import generate_annotated_json_object, write_json_to_file, read_json_from_file, \
    api_text_json_sentence_split_for_json_object

package_short_description_json = read_json_from_file("jdk_package_short_description.json")
package_long_description_json = read_json_from_file("jdk_package_detail_description.json")
class_short_description_json = read_json_from_file("jdk_class_short_description.json")
class_long_description_json = read_json_from_file("jdk_class_detail_description.json")
method_long_description_json = read_json_from_file("jdk_method_detail_description.json")
method_returns_description_json = read_json_from_file("jdk_method_return_description.json")
method_throws_description_json = read_json_from_file("jdk_exception.json")
method_parameter_description_json = read_json_from_file("jdk_parameter_detail_description.json")

description_json_list = [
    package_short_description_json,
    package_long_description_json,
    class_short_description_json,
    class_long_description_json,
    method_long_description_json,
    method_returns_description_json,
    method_throws_description_json,
    method_parameter_description_json,
]
description_json = []
for team_json_list in description_json_list:
    for item in team_json_list:
        description_json.append(item)

write_json_to_file("jdk_all_description.json", description_json)
description_json = api_text_json_sentence_split_for_json_object(description_json)

annotated_description_object = generate_annotated_json_object(description_json)
write_json_to_file("annotated_jdk_all_description.json", annotated_description_object)
