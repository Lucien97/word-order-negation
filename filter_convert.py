from projection import projection


def verse_verb_detection(verse_pos_dic):
    verb_ids = []
    for key, value in verse_pos_dic.items():
        if value[0] == 'VERB':
            verb_ids.append(key)
    return verb_ids


def relation_extraction(verb_ids, verse_pos_dic, verse_dep_dic):
    relation_dic = {}
    single_verb_dic = {}
    for key, value in verse_dep_dic.items():
        if value[0] in verb_ids:
            verse_pos_dic[key].insert(0, value[1])
            single_verb_dic[key] = verse_pos_dic[key]
            relation_dic[value[0]] = single_verb_dic
    return relation_dic


def word_order_detection(relation_dic):
    verse_order_list = []
    for verb_id, verb_dic in relation_dic.items():
        subj_id = 0
        obj_id = 0
        neg_id = 0
        for key, value in verb_dic.items():
            if value[0] == 'nsubj':
                subj_id = key
            if value[0] == 'obj':
                obj_id = key
            if value[-1] == 'neg':
                neg_id = key
        if subj_id != 0 and obj_id != 0:
            order_list = [subj_id, verb_id, obj_id, neg_id]
            verse_order_list.append(order_list)
    return verse_order_list


def file_order_detection(s_pos_dic, s_dep_dic, file_dir):
    order_list = []
    t_pos_dic, t_dep_dic = projection(s_pos_dic, s_dep_dic, file_dir)
    a = 1
    for verse_id, verse_pos in t_pos_dic.items():
            verb_ids = verse_verb_detection(verse_pos)
            if verb_ids != []:
                relation_dic = relation_extraction(verb_ids, verse_pos, t_dep_dic[verse_id])
                if relation_dic != {}:
                    verse_order_list = word_order_detection(relation_dic)
                    if verse_order_list != []:
                        order_list.append(verse_order_list)
    return order_list


def list2pattern(verb_list):
    pattern_dic = {0: 'S', 1: 'V', 2: 'O', 3: 'Neg'}
    order_str = ''
    if verb_list[-1] == 0:
        temp_list = list(map(int, verb_list[:-1]))
    else:
        temp_list = list(map(int, verb_list))
    sort_id = sorted(range(len(temp_list)), key=lambda k: temp_list[k])
    for id in sort_id:
        order_str += pattern_dic[id]
    return order_str


def order_list2order(order_list):
    order_dic = {}
    for verse_list in order_list:
        for verb_list in verse_list:
            temp_list = list2pattern(verb_list)
            if temp_list not in order_dic.keys():
                order_dic[temp_list] = 1
            order_dic[temp_list] += 1
    return order_dic
