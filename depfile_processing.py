dep_dir = '/Users/chen/Typology/pos&dep_files'


def dep_line_parsing(string):
    result = []
    split_string = string.split('\t')
    word_id = split_string[0].split(': ')[1]
    result.append(split_string[2].split(': ')[1])
    result.append(split_string[4].split(': ')[1][:-1])
    return word_id, result


def dep_file_parsing(lan):
    dep_dic = {}
    with open(dep_dir + '/' + lan + '-dep.txt') as dep_file:
        dep_lines = dep_file.readlines()
    sentence_index = 0
    for number, line in enumerate(dep_lines):
        word_dep = {}
        if '#' in line:
            sentence_index = line[1:-2]
            dep_dic[sentence_index] = {}
        else:
            word_id, result = dep_line_parsing(line)
            word_dep[word_id] = result
            dep_dic[sentence_index].update(word_dep)
    return dep_dic
