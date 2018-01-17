import codecs
import json
import random
import sys

from data_process import sentence_split

reload(sys)
sys.setdefaultencoding('utf-8')


def write_json_to_file(file_name, data):
    with codecs.open(file_name, 'w', encoding='utf8') as json_file:
        data = json.dumps(data, ensure_ascii=False, encoding='utf8')
        json_file.write(unicode(data))


def read_json_from_file(file_name):
    # Reading data back
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = json.load(f)
    return data


def api_text_json_sentence_split(input_json_file, output_json_file=None):
    if output_json_file is None:
        output_json_file = "split_" + input_json_file
    result_json = []
    data_json = read_json_from_file(input_json_file)
    for each_data in data_json:
        api_text = each_data["text"]
        if api_text is not None:
            api_text_list = sentence_split(api_text)
            for each_description in api_text_list:
                if each_description == "":
                    continue
                team = each_data.copy()
                team['text'] = each_description
                team['sentence_index'] = api_text_list.index(each_description) + 1
                result_json.append(team)
    write_json_to_file(output_json_file, result_json)


def annotated_by_sentence_index(input_json_file, output_json_file=None):
    if output_json_file is None:
        output_json_file = "annotated_" + input_json_file
    result_json = []
    data_json = read_json_from_file(input_json_file)
    for each_data in data_json:
        team = each_data.copy()
        if "sentence_index" not in team.keys():
            team["sentence_index"] = 1
        if "knowledge_pattern" not in team.keys():
            sentence_index = team["sentence_index"]
            if sentence_index == 1:
                team["knowledge_pattern"] = "functionality and behavior"
            else:
                team["knowledge_pattern"] = "others"

        result_json.append(team)
    write_json_to_file(output_json_file, result_json)


def complete_api_text_json(input_json_file, output_json_file=None):
    if output_json_file is None:
        output_json_file = "completed_" + input_json_file
    result_json = []
    data_json = read_json_from_file(input_json_file)
    for each_data in data_json:
        team = each_data.copy()
        if "sentence_index" not in team.keys():
            team["sentence_index"] = 1
        if "knowledge_pattern" not in team.keys():
            team["knowledge_pattern"] = "others"

        result_json.append(team)
    write_json_to_file(output_json_file, result_json)


def split_api_text_json_by_knowledge_pattern(input_json_file):
    result_json = {}
    data_json = read_json_from_file(input_json_file)
    for each_data in data_json:
        try:
            if each_data["knowledge_pattern"] not in result_json.keys():
                result_json[each_data["knowledge_pattern"]] = []
            result_json[each_data["knowledge_pattern"]].append(each_data)
        except Exception:
            print Exception, str(Exception)

    for type in result_json.keys():
        write_json_to_file(type + "_" + input_json_file, result_json[type])


def random_sample_from_api_text_json(input_json_file, number=1000):
    data_json = read_json_from_file(input_json_file)

    old_len = len(data_json)
    print input_json_file + " old_len=" + str(old_len)
    if number > old_len:
        number = old_len - 2
    print input_json_file + " sample =" + str(number)

    result_index_list = random.sample(range(0, old_len), number)
    result_json = []
    for result_index in result_index_list:
        result_json.append(data_json[result_index])

    write_json_to_file("sample_" + str(number) + "_" + input_json_file, result_json)


def parse_api_text_json_to_fast_text_train_format(input_json_file):
    data_json = read_json_from_file(input_json_file)
    output_json_file = "fastText_format_" + input_json_file
    output_json_file = output_json_file.replace(".json", ".txt")
    with codecs.open(output_json_file, 'w', encoding='utf8') as output:
        for each_data in data_json:
            try:
                label = "__label__" + each_data["knowledge_pattern"].replace(" ", "_")
                line = each_data["text"].replace("\t", " ") + "\t" + label
                output.write(line)
                output.write("\n")
            except Exception:
                print Exception, str(Exception)
