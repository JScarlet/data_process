from util.jdk_data_export import export_method_see_also_relation_from_jdk
from util.json_util import write_json_to_file

'''
extract the jdk api entity see also relation
'''


def __parse_to_json(relation_list):
    json_list = []
    for relation in relation_list:
        json_list.append(relation.to_json())
    return json_list


if __name__ == "__main__":
    relation_set = set(export_method_see_also_relation_from_jdk())
    result = __parse_to_json(relation_set)
    write_json_to_file("jdk_see_also_relation_for_method.json", result)
