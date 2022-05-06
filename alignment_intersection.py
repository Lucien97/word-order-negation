def single_align_check(str1, str2):
    seg_str1 = str1.split(' ')
    seg_str2 = str2.split(' ')
    align_intersection = []
    for single_align in seg_str1:
        if single_align in seg_str2:
            align_intersection.append(single_align)
    return ' '.join(align_intersection)


def align_check(align_dic, for_file, re_file):
    final_alignment = {}
    with open(for_file) as f_file, open(re_file) as r_file:
        f_lines = f_file.readlines()
        r_lines = r_file.readlines()
    for i, key in enumerate(align_dic):
        result = single_align_check(f_lines[i], r_lines[i])
        if result != '':
            final_alignment[key] = result
    return final_alignment
