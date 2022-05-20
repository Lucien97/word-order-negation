pos_dir = '/Users/chen/Typology/pos&dep_files'


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


def pos_line_parsing(string):
    result = ['_', '_']
    split_str = string.split('\t')
    result[0] = split_str[1].split(': ')[1]
    feat_str = split_str[3].split(': ')[1]
    if feat_str != '_':
        if 'Polarity=Neg' in feat_str.split('|'):
            result[1] = 'neg'
    return result


def pos_file_parsing(lan):
    pos_dic = {}
    pos_file_dir = pos_dir + '/' + lan + '-pos.txt'
    pos_pop_list = find_overlap(pos_file_dir)
    with open(pos_file_dir) as pos_file:
        pos_lines = pos_file.readlines()
    word_id = 0
    sentence_index = 0
    for line in pos_lines:
        word_pos = {}
        if '#' in line:
            word_id = 0
            sentence_index = line[1:-2]
            pos_dic[sentence_index] = {}
        else:
            word_pos[str(word_id)] = pos_line_parsing(line)
            pos_dic[sentence_index].update(word_pos)
            word_id += 1
    for item in pos_pop_list:
        pos_dic.pop(item)
    return pos_dic
