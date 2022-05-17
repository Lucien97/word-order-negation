pos_dir = '/Users/chen/Typology/pos&dep_files'


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
    with open(pos_dir + '/' + lan + '-pos.txt') as pos_file:
        pos_lines = pos_file.readlines()
    word_id = 1
    sentence_index = 0
    for number, line in enumerate(pos_lines):
        word_pos = {}
        if '#' in line:
            word_id = 1
            sentence_index = line[1:-2]
            pos_dic[sentence_index] = {}
        else:
            word_pos[word_id] = pos_line_parsing(line)
            pos_dic[sentence_index].update(word_pos)
            word_id += 1
    return pos_dic
