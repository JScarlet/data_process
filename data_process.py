import json
import nltk
import pymysql

conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='fdroid',
    charset='utf8'
)

type_dict = {'package': 'jdk_package', 'method': 'jdk_method', 'class': 'jdk_class'}


def read_data(api_type):
    lists = []
    try:
        with conn.cursor() as cur:
            sql = 'select name, handled_description from ' + type_dict.get(api_type) + ' where class_id < 20'
            cur.execute(sql)
            lists = cur.fetchall()
            for each in lists:
                print(each)
    except:
        conn.rollback()
    finally:
        conn.close()
    return lists


def package_data_process(data_list, api_type):
    result = []
    for each_data in data_list:
        name = each_data[0]
        descriptions = each_data[1]
        if descriptions is not None:
            description_list = sentence_split(descriptions)
            for each_description in description_list:
                temp = {}
                temp.setdefault('API_name', name)
                temp.setdefault('text_title', api_type)
                temp.setdefault('text', each_description)
                temp.setdefault('sentence_index', description_list.index(each_description) + 1)
                result.append(temp)
    return result


def write_in_file(result):
    with open('method.json', 'a') as file_object:
        json.dump(result, file_object)


def sentence_split(descriptions):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    description_list = tokenizer.tokenize(descriptions)
    return description_list

if __name__ == '__main__':
    api_type = 'method'
    data_list = read_data(api_type)
    result = package_data_process(data_list, api_type)
    write_in_file(result)