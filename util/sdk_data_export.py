import sys

import pymysql

from util.code_text_process import clean_html_text, clean_html_text_with_replacement

reload(sys)
sys.setdefaultencoding('utf-8')

conn = pymysql.connect(
    host='10.141.221.75',
    port=3306,
    user='root',
    passwd='root',
    db='knowledgeGraph',
    charset='utf8'
)

cur = conn.cursor()


def export_package_description_from_sdk():
    result = []
    try:
        cur.execute("select Package_name,Short_description_label,Long_description_label from androidAPI_package")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            short_description = each_list[1]
            long_description = each_list[2]

            short_description = clean_html_text_with_replacement(short_description)

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = "Android API 27"
            temp["API_Type"] = "Package"
            temp["text_title"] = "description"
            temp["sub_title"] = name

            if short_description is None or short_description is "":
                pass
            else:

                temp["text"] = short_description
                result.append(temp)
                temp = temp.copy()

            long_description = clean_html_text_with_replacement(long_description)
            if long_description is None or long_description is "":
                pass
            else:
                temp["text"] = long_description
                result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_class_description_from_sdk():
    '''export the description from jdk'''
    result = []
    try:
        cur.execute("select Class_name,Short_description_label,Long_description_label,Package_id from androidAPI_class")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            short_description = each_list[1]
            short_description = clean_html_text_with_replacement(short_description)
            long_description = each_list[2]
            long_description = clean_html_text_with_replacement(long_description)

            package_id = each_list[3]
            type = "Class"

            sql = "select Package_name from androidAPI_package where id = " + str(package_id)
            cur.execute(sql)
            package_query = cur.fetchall()
            package_name = str(package_query[0][0])

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = package_name
            temp["API_Type"] = type
            temp["text_title"] = "description"

            if short_description is None or short_description is "":
                pass
            else:
                temp["text"] = short_description
                temp["knowledge_pattern"] = "functionality and behavior"
                result.append(temp)
                temp = temp.copy()

            if long_description is None or long_description is "":
                pass
            else:
                temp["text"] = long_description
                temp["knowledge_pattern"] = "others"
                result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_method_description_from_sdk():
    '''export the short description from jdk for method'''
    result = []
    try:
        cur.execute(
            "select Method_name,Short_description_label,Long_description_label,Class_id,Full_declaration from androidAPI_method")
        lists = cur.fetchall()
        for each_list in lists:
            try:
                temp = {}
                name = each_list[0]
                short_description = each_list[1]
                short_description = clean_html_text_with_replacement(short_description)

                long_description = each_list[2]
                long_description = clean_html_text_with_replacement(long_description)
                if long_description is None or long_description is "":
                    pass
                class_id = each_list[3]
                type = "Method"
                full_declaration = clean_html_text(each_list[4])
                if full_declaration is None or full_declaration is "":
                    continue
                else:
                    full_declaration = full_declaration.replace(" (", "(")
                sql = "select Class_name from androidAPI_class where id = " + str(class_id)
                cur.execute(sql)
                class_query = cur.fetchall()
                class_name = str(class_query[0][0])

                if type == "Method":
                    temp["API_name"] = class_name + "." + name + "()"
                else:
                    temp["API_name"] = class_name + "." + name
                temp["API_name_full_declaration"] = full_declaration
                temp["parent_API_name"] = class_name
                temp["API_Type"] = type
                temp["text_title"] = "description"

                if short_description is None or short_description is "":
                    pass
                else:
                    temp["text"] = short_description
                    result.append(temp)
                    temp = temp.copy()

                if long_description is None or long_description is "":
                    pass
                else:
                    temp["text"] = long_description
                    result.append(temp)

            except Exception as e:
                print(Exception, ": ", e)
    except Exception as e:
        print(Exception, ": ", e)
    return result
