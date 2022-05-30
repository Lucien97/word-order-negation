def align_str2dic(string):
    temp_dic = {}
    align_pair = string.split(' ')
    for item in align_pair:
        temp_dic[item.split('-')[0]] = item.split('-')[1]
    return temp_dic


def align2dic(alignment_dir):
    align_dic = {}
    with open(alignment_dir) as align_file:
        raw_lines = align_file.readlines()
    for line in raw_lines:
        if line != '\n':
            split_line = line.split('\t')
            align_dic[split_line[0]] = align_str2dic(split_line[1][:-1])
    return align_dic


def projection(source_pos_dic, source_dep_dic, alignment_dir):
    align_dic = align2dic(alignment_dir)
    proj_dep_dic = {}
    proj_pos_dic = {}
    for verse_id, align_pair in align_dic.items():
        temp_dep_dic = {}
        temp_pos_dic = {}
        if verse_id in source_dep_dic:
            for source_id, target_id in align_pair.items():
                head_id = source_dep_dic[verse_id][source_id][0]
                if head_id in align_pair.keys():
                    temp_dep_dic[target_id] = [align_pair[head_id], source_dep_dic[verse_id][source_id][1]]
                    temp_pos_dic[target_id] = source_pos_dic[verse_id][source_id]
                    temp_pos_dic[align_pair[head_id]] = source_pos_dic[verse_id][head_id]
                if head_id == '-1':
                    temp_dep_dic[target_id] = ['-1', 'root']
                    temp_pos_dic[target_id] = source_pos_dic[verse_id][source_id]
            proj_dep_dic[verse_id] = temp_dep_dic
            proj_pos_dic[verse_id] = temp_pos_dic
    return proj_pos_dic, proj_dep_dic
