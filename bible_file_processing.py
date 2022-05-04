import re


def file2dic(file_dir):
    file_dic = {}
    with open(file_dir) as target_file:
        lines = target_file.readlines()
        assign_flag = 0
        for line in lines:
            if assign_flag:
                try:
                    index, content = line.split('\t')
                    if content == '\n':
                        continue
                    else:
                        index = ''.join(re.findall(r'\d', index))
                        file_dic[index] = content[:-1]
                except ValueError:
                    continue
            if 'notes' in line:
                assign_flag = 1
    return file_dic


def dic_compare(s_dic, t_dic):
    align_dic = {}
    source_item_pop = []
    target_item_pop = []
    for item in t_dic:
        if item not in s_dic:
            target_item_pop.append(item)
    for item in s_dic:
        if item not in t_dic:
            source_item_pop.append(item)
    for item in target_item_pop:
        t_dic.pop(item)
    for item in source_item_pop:
        s_dic.pop(item)
    for item in t_dic:
        align_dic[item] = [s_dic[item], t_dic[item]]
    return align_dic

