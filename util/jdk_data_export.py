import sys

import pymysql

from util.code_text_process import clean_html_text, clean_html_text_with_replacement
from util.relation import Relation

reload(sys)
sys.setdefaultencoding('utf-8')

conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='fdroid',
    charset='utf8'
)

cur = conn.cursor()


def html_data_process():
    '''export all html text as a json array'''
    result = []
    try:
        cur.execute("select doc_website, html_body from javadoc_body")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            doc_website = each_list[0]
            html_body = each_list[1]

            temp["doc_website"] = doc_website
            temp["html_body"] = html_body
            result.append(temp)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_package_name_json():
    '''export all package Name into a json array'''
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
            temp["name"] = name
            temp["type"] = "Package"
            temp["parent_API"] = jdk_version
            result.append(temp)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_class_name_json():
    '''export all class Name into a json array'''
    result = []
    try:
        cur.execute("select name, package_id,type from jdk_class")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            package_id = each_list[1]
            type = each_list[2]
            sql = "select name from jdk_package where package_id = " + str(package_id)
            cur.execute(sql)
            package_query = cur.fetchone()
            package_name = package_query[0]
            temp["name"] = name
            temp["type"] = type
            temp["parent_API"] = package_name
            result.append(temp)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_method_name_json():
    result = []
    try:
        cur.execute("select full_declaration, name, type, class_id from jdk_method")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            full_declaration = each_list[0]
            name = each_list[1]
            type = each_list[2]
            class_id = each_list[3]
            sql = "select name from jdk_class where class_id = " + str(class_id)
            cur.execute(sql)
            class_query = cur.fetchone()
            class_name = class_query[0]
            if full_declaration is None:
                temp["name"] = name
            else:
                temp["name"] = clean_html_text(full_declaration)
            temp["type"] = type
            temp["parent_API"] = class_name
            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_package_short_description_from_jdk():
    '''export the short description from jdk'''
    result = []
    try:
        cur.execute("select name,description,library_id from jdk_package")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            description = each_list[1]
            library_id = each_list[2]

            description = clean_html_text_with_replacement(description)
            if description is None or description is "":
                continue

            sql = "select jdk_version from jdk_library where library_id = " + str(library_id)
            cur.execute(sql)
            library_query = cur.fetchall()
            jdk_version = "jdk" + str(library_query[0][0])

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = jdk_version
            temp["API_Type"] = "Package"
            temp["text_title"] = "description"
            temp["sub_title"] = name
            temp["text"] = description
            temp["knowledge_pattern"] = "functionality and behavior"

            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_package_detail_description_from_jdk():
    result = []
    try:
        cur.execute("select name,Detail_description,library_id from jdk_package")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            description = each_list[1]
            library_id = each_list[2]

            description = clean_html_text_with_replacement(description)
            if description is None or description is "":
                continue

            sql = "select jdk_version from jdk_library where library_id = " + str(library_id)
            cur.execute(sql)
            library_query = cur.fetchall()
            jdk_version = "jdk" + str(library_query[0][0])

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = jdk_version
            temp["API_Type"] = "Package"
            temp["text_title"] = "description"
            temp["sub_title"] = name
            temp["text"] = description

            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_exception_throw_from_method_for_jdk():
    result = []
    try:
        cur.execute("select Name, Class_id,Method_id, Description from jdk_exception")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            Class_id = each_list[1]
            Method_id = each_list[2]
            Description = each_list[3]
            sql = "select name from jdk_class where class_id = " + str(Class_id)
            cur.execute(sql)
            class_query = cur.fetchone()
            class_name = class_query[0]

            sql = "select name from jdk_method where method_id = " + str(Method_id)
            cur.execute(sql)
            method_query = cur.fetchone()
            method_name = method_query[0]
            method_name = clean_html_text(method_name)

            temp["API_name"] = class_name + "." + method_name + "()"
            temp["API_name_full_declaration"] = method_name
            temp["parent_API_name"] = class_name
            temp["API_Type"] = "Method"
            temp["text_title"] = "throws"
            temp["sub_title"] = name
            temp["text"] = clean_html_text_with_replacement(Description)
            temp["knowledge_pattern"] = "directive"

            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_class_short_description_from_jdk():
    '''export the short description from jdk'''
    result = []
    try:
        cur.execute("select name,Description,Package_id,type from jdk_class")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            description = each_list[1]
            description = clean_html_text(description)
            if description is None or description is "":
                continue
            package_id = each_list[2]
            type = each_list[3]

            sql = "select name from jdk_package where Package_id = " + str(package_id)
            cur.execute(sql)
            package_query = cur.fetchall()
            package_name = str(package_query[0][0])

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = package_name
            temp["API_Type"] = type
            temp["text_title"] = "description"
            temp["text"] = description
            temp["knowledge_pattern"] = "functionality and behavior"

            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_class_detail_description_from_jdk():
    '''export the short description from jdk'''
    result = []
    try:
        cur.execute("select name,Detail_description,Package_id,type from jdk_class")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            description = each_list[1]
            package_id = each_list[2]
            type = each_list[3]

            description = clean_html_text_with_replacement(description)
            if description is None or description is "":
                continue

            sql = "select name from jdk_package where Package_id = " + str(package_id)
            cur.execute(sql)
            package_query = cur.fetchall()
            package_name = str(package_query[0][0])

            temp["API_name"] = name
            temp["API_name_full_declaration"] = name
            temp["parent_API_name"] = package_name
            temp["API_Type"] = type
            temp["text_title"] = "description"
            temp["text"] = description

            result.append(temp)

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_method_detail_description_from_jdk():
    '''export the short description from jdk for method'''
    result = []
    try:
        cur.execute("select name,Description,Class_id,Type,Full_declaration from jdk_method")
        lists = cur.fetchall()
        for each_list in lists:
            try:
                temp = {}
                name = each_list[0]
                description = each_list[1]
                description = clean_html_text_with_replacement(description)
                if description is None or description is "":
                    continue
                class_id = each_list[2]
                type = each_list[3]
                full_declaration = clean_html_text(each_list[4])
                if full_declaration is None or full_declaration is "":
                    continue
                sql = "select name from jdk_class where class_id = " + str(class_id)
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
                temp["text"] = description

                result.append(temp)
            except Exception as e:
                print(Exception, ": ", e)
    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_class_see_also_relation_from_jdk():
    '''export see also relation from jdk'''
    result = []
    try:
        cur.execute("select See_also_title,Class_id,See_also_website from jdk_class_see_also")
        lists = cur.fetchall()
        for each_list in lists:
            temp = {}
            name = each_list[0]
            class_id = each_list[1]
            see_also_website = each_list[2]
            name = clean_html_text(name)
            if name is None or name is "":
                continue

            sql = "select name from jdk_class where class_id = " + str(class_id)
            cur.execute(sql)
            class_query = cur.fetchone()
            class_name = class_query[0]

            result.append(Relation(subject=class_name, relation="see also", object=name))
            result.append(
                Relation(subject=class_name, relation="has see-also hyperlink", object=see_also_website))
            result.append(Relation(subject=name, relation="has hyperlink to", object=see_also_website))

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_method_see_also_relation_from_jdk():
    '''export see also relation from jdk'''
    result = []
    try:
        cur.execute("select See_also_title,Class_id,Method_id,See_also_website from jdk_method_see_also")
        lists = cur.fetchall()
        for each_list in lists:
            name = each_list[0]
            class_id = each_list[1]
            method_id = each_list[2]
            see_also_website = each_list[3]
            name = clean_html_text(name)
            if name is None or name is "":
                continue

            sql = "select name from jdk_class where class_id = " + str(class_id)
            cur.execute(sql)
            class_query = cur.fetchone()
            class_name = class_query[0]

            sql = "select name from jdk_method where method_id = " + str(method_id)
            cur.execute(sql)
            method_query = cur.fetchone()
            method_name = method_query[0]
            method_name = clean_html_text(method_name)
            if method_name.upper() == method_name:
                full_method_name = class_name + "." + method_name
            else:
                full_method_name = class_name + "." + method_name + "()"

            result.append(Relation(subject=full_method_name, relation="short name", object=name))
            result.append(Relation(subject=full_method_name, relation="see also", object=name))
            result.append(
                Relation(subject=full_method_name, relation="has see-also hyperlink", object=see_also_website))
            result.append(Relation(subject=name, relation="has hyperlink to", object=see_also_website))

    except Exception as e:
        print(Exception, ": ", e)
    return result


def export_return_description_from_method_for_jdk():
    '''export the short description from jdk for method'''
    result = []
    try:
        cur.execute("select name,return_string,Class_id,Type,Full_declaration from jdk_method")
        lists = cur.fetchall()
        for each_list in lists:
            try:
                temp = {}
                name = each_list[0]
                description = each_list[1]
                description = clean_html_text_with_replacement(description)
                if description is None or description is "":
                    continue
                class_id = each_list[2]
                type = each_list[3]
                full_declaration = clean_html_text(each_list[4])
                if full_declaration is None or full_declaration is "":
                    continue
                sql = "select name from jdk_class where class_id = " + str(class_id)
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
                temp["text_title"] = "returns"
                temp["text"] = description

                result.append(temp)
            except Exception as e:
                print(Exception, ": ", e)
    except Exception as e:
        print(Exception, ": ", e)
    return result
