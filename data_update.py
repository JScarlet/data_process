import pymysql

conn = pymysql.connect(
    host='10.141.221.73',
    port=3306,
    user='root',
    passwd='root',
    db='fdroid',
    charset='utf8'
)


def read_data():
    lists = []
    try:
        with conn.cursor() as cur:
            sql = 'select class_id, detail_description from jdk_class where class_id < 8265'
            #sql = 'select class_id, detail_description from jdk_class where class_id = 1632'
            cur.execute(sql)
            lists = cur.fetchall()
            #for each in lists:
            #    print(each)
    except:
        conn.rollback()
    return lists


def data_clean(data_list):
    result = []
    for each in data_list:
        if each[1] != None:
            temp = []
            description = each[1]
            while description.find('<') != -1:
                description = tag_remove(description)
                # print(description)
            description = description.replace('\n', '').replace('  ', ' ').strip()
            temp.append(each[0])
            temp.append(description)
            print(temp)
            result.append(temp)
    return result


def tag_remove(sentence):
    left_bracket_index = sentence.find('<')
    right_bracket_index = sentence.find('>')
    while sentence[left_bracket_index + 1: right_bracket_index + 1].find('<') != -1:
        left_bracket_index = left_bracket_index + sentence[left_bracket_index + 1: right_bracket_index + 1].find('<') + 1
    tag = sentence[left_bracket_index: right_bracket_index + 1]
    #print(tag)
    sentence = sentence.replace(tag, '')
    return sentence


def update_data(result_list):
    try:
        with conn.cursor() as cur:
            for each in result_list:
                cur.execute('update jdk_class set handled_description = %s where class_id = %s', (each[1], each[0]))
                print(str(each[0]) + " has saved in database")
                conn.commit()
    except:
        conn.rollback()


if __name__ == '__main__':
    data_list = read_data()
    result = data_clean(data_list)
    for each in result:
        print(each)
    update_data(result)