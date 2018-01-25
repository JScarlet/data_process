import re

from util.jdk_data_export import export_package_name_json, export_class_name_json, export_method_name_json
from util.json_util import write_json_to_file

'''
extract the jdk api entity in to a json file to build a dictionary about jdk
'''


class APIDictionaryItem:
    def __init__(self, name, type, parent_API):
        self.name = name
        self.type = type
        self.parent_API = parent_API

    def __eq__(self, other):
        if isinstance(other, APIDictionaryItem):
            if self.name == other.name and self.type == other.type:
                if self.parent_API == other.parent_API:
                    return True
                else:
                    if self.type == 'package':
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False

    def to_json(self):
        return {"name": self.name, "type": self.type, "parent_API": self.parent_API}

    def __hash__(self):
        return hash(self.name + self.type + self.parent_API)

    def __str__(self):
        return self.name + ',' + self.type + ',' + self.parent_API


def __reduce_duplicate(api_item_jsons):
    result_set = set([])
    for api_item in api_item_jsons:
        result_set.add(
            APIDictionaryItem(name=api_item['name'],
                              type=api_item['type'],
                              parent_API=api_item['parent_API']))
    return list(result_set)


def __clean_api_name_string(api_name):
    return re.sub(r'\s+', ' ', api_name.replace(u'\u00a0', " "))


def __parse_to_json(api_item_list):
    api_item_jsons = []
    for api_item in api_item_list:
        api_item_jsons.append(api_item.to_json())
    return api_item_jsons


if __name__ == "__main__":
    package_result = __reduce_duplicate(export_package_name_json())
    print(package_result)
    class_result = __reduce_duplicate(export_class_name_json())
    print(class_result)
    method_result = __reduce_duplicate(export_method_name_json())
    print(method_result)
    result = package_result + class_result + method_result

    result = __parse_to_json(result)
    for jdk_api_name in result:
        jdk_api_name['name'] = __clean_api_name_string(jdk_api_name['name'])
    write_json_to_file("JDK_API_name.json", result)
