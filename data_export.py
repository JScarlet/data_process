import json

import pymysql

conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='fdroid',
    charset='utf8'
)

cur = conn.cursor()

def package_data_process():
    result = []
    try:
        cur.execute("select name, library_id from jdk_package")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            library_id = each_list[1]
            sql = "select jdk_version from jdk_library where library_id = " + str(library_id)
            cur.execute(sql)
            library_query = cur.fetchall()
            jdk_version = "jdk" + str(library_query[0][0])
            temp.setdefault("name", name)
            temp.setdefault("type", "package")
            temp.setdefault("parent_API", jdk_version)
            result.append(temp)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def class_data_process():
    result = []
    try:
        cur.execute("select name, package_id from jdk_class")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            package_id = each_list[1]
            sql = "select name from jdk_package where package_id = " + str(package_id)
            cur.execute(sql)
            package_query = cur.fetchone()
            package_name = package_query[0]
            temp.setdefault("name", name)
            temp.setdefault("type", "class")
            temp.setdefault("parent_API", package_name)
            result.append(temp)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def method_data_process():
    result = []
    try:
        cur.execute("select handled_full_declaration, name, type, class_id from jdk_method")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            handled_full_declaration = each_list[0]
            name = each_list[1]
            type = each_list[2]
            class_id = each_list[3]
            sql = "select name from jdk_class where class_id = " + str(class_id)
            cur.execute(sql)
            class_query = cur.fetchone()
            class_name = class_query[0]
            if handled_full_declaration is None:
                temp.setdefault("name", name)
            else:
                temp.setdefault("name", handled_full_declaration)
            temp.setdefault("type", type)
            temp.setdefault("parent_API", class_name)
            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def write_in_file(data):
    with open("API_name.json", 'w') as file_object:
        json.dump(data, file_object)

if __name__ == "__main__":
    package_result = package_data_process()
    #print(package_result)
    class_result = class_data_process()
    #print(class_result)
    method_result = method_data_process()
    #print(method_result)
    result = package_result + class_result + method_result
    write_in_file(result)