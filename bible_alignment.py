import os
import re
import shutil
from pathlib import Path

align_tool_path = '/Users/chen/Typology/maceflomal/'
lan_to_file = {'deu': 'deu-x-bible-newworld.txt', 'eng': 'eng-x-bible-newworld2013.txt',
               'fra': 'fra-x-bible-newworld.txt', 'fin': 'fin-x-bible-newworld.txt',
               'ces': 'ces-x-bible-newworld.txt'}


def file_dic_generation(filename):
    file_dic = {}
    filename = str(filename.name)
    with open(filename) as target_file:
        lines = target_file.readlines()
        assign_flag = 0
        for line in lines:
            if assign_flag:
                try:
                    index, content = line.split('\t')
                    index = ''.join(re.findall(r'\d', index))
                    file_dic[index] = content
                except ValueError:
                    continue
            if 'notes' in line:
                assign_flag = 1
    return file_dic


for item in lan_to_file:
    # print(item)
    item_alignment_dir = '/Users/chen/Typology/' + item
    if not os.path.exists(item_alignment_dir):
        os.mkdir(item_alignment_dir)
    with open('/Users/chen/Typology/bible_files/' + lan_to_file[item]) as source_file:
        source_file_dic = file_dic_generation(source_file)
    bible_files = Path('/Users/chen/Typology/bible_files').glob('*.txt')
    for bible in bible_files:
        bible_name = str(bible).split('/')[-1]
        bible_lan = bible_name.split('-')[0]
        if bible_lan == item:
            print(str(bible) + ' is skipped!')
            continue
        else:
            gen_file_name = item + '-' + bible_name
            gen_file_dir = '/Users/chen/Typology/' + gen_file_name
            with open(bible) as bible_file:
                tar_file_dic = file_dic_generation(bible_file)
            with open(gen_file_dir, 'a+') as file:
                verses_del = []
                for verse in tar_file_dic:
                    if verse in source_file_dic:
                        file.write(source_file_dic[verse])
                    else:
                        verses_del.append(verse)
            for verse_del in verses_del:
                tar_file_dic.pop(verse_del)
            temp_file_name = 'rev-' + bible_name
            temp_file_dir = '/Users/chen/Typology/' + temp_file_name
            with open(temp_file_dir, 'a+') as temp_file:
                for verse in tar_file_dic:
                    temp_file.write(tar_file_dic[verse])
        s_file = shutil.move(gen_file_dir, align_tool_path + gen_file_name)
        t_file = shutil.move(temp_file_dir, align_tool_path + temp_file_name)
        align_result_file = item_alignment_dir + '/' + item + '-' + bible_name + '.txt'
        os.chdir('/Users/chen/Typology/maceflomal')
        os.system('python3 {} --overwrite -m 3 -s {} -t {} -f {}'.format('align.py', s_file, t_file, align_result_file))
        os.remove(s_file)
        os.remove(t_file)
