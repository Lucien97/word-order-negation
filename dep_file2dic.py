dep_dir = '/Users/chen/Typology/pos&dep_files'


def find_overlap(file_dir):
    pop_dic = {}
    pop_item = []
    with open(file_dir) as test_file:
        lines = test_file.readlines()
        for line in lines:
            if line[0] == '#':
                verse_id = line[1:-2]
                if verse_id not in pop_dic:
                    pop_dic[verse_id] = 1
                else:
                    pop_dic[verse_id] += 1
        for key, value in pop_dic.items():
            if value > 1:
                pop_item.append(key)
    return pop_item


def dep_line_parsing(string):
    result = []
    split_string = string.split('\t')
    word_id = str(int(split_string[0].split(': ')[1]) - 1)
    result.append(split_string[2].split(': ')[1])
    result.append(split_string[4].split(': ')[1][:-1])
    return word_id, result


def dep_file_parsing(lan):
    dep_dic = {}
    dep_file_dir = dep_dir + '/' + lan + '-dep.txt'
    dep_pop_list = find_overlap(dep_file_dir)
    with open(dep_file_dir) as dep_file:
        dep_lines = dep_file.readlines()
    sentence_index = 0
    for line in dep_lines:
        word_dep = {}
        if '#' in line:
            sentence_index = line[1:-2]
            dep_dic[sentence_index] = {}
        else:
            word_id, result = dep_line_parsing(line)
            word_dep[word_id] = result
            dep_dic[sentence_index].update(word_dep)
    for item in dep_pop_list:
        dep_dic.pop(item)
    return dep_dic
