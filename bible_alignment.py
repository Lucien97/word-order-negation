import os
import re
from pathlib import Path

align_tool_path = '/maceflomal/align.py'
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
    with open('/Users/chen/Typology/bible_files/' + lan_to_file[item]) as source_file:
        source_file_dic = file_dic_generation(source_file)
    bible_files = Path('/Users/chen/Typology/bible_files').glob('*.txt')
    for bible in bible_files:
        lan = str(bible).split('/')[1].split('-')[0]
        if lan == item:
            # print(str(bible) + ' is skipped!')
            continue
        else:
            file_name = item + '-' + str(bible).split('/')[1]
            output_file_dir = '/Users/chen/Typology/alignment-' + file_name
            with open(bible) as bible_file:
                bible_dic = file_dic_generation(bible_file)
            with open('./' + file_name, 'a+') as file:
                source_language_file = os.path.abspath(file.name)
                # a = 0
                # b = 0
                item_del = []
                for bible_item in bible_dic:
                    if bible_item in source_file_dic:
                        file.write(source_file_dic[bible_item])
                        # a += 1
                    else:
                        item_del.append(bible_item)
                        # b += 1
            for item in item_del:
                bible_dic.pop(item)
            temp_file_name = 'temp-' + file_name
            with open('/Users/chen/Typology/' + temp_file_name, 'a+') as temp_file:
                target_language_file = os.path.abspath(temp_file.name)
                for item in bible_dic:
                    temp_file.write(bible_dic[item])
            # print('这里源文件有{}行没有数据！'.format(b))
            print(len(source_file_dic))
            print(len(bible_dic))
            print(item_del)
            print(source_language_file)
            print(target_language_file)
            print(output_file_dir)
            # print('there are {} lines in total'.format(a))
            os.system('python3 {} --overwrite -m 3 -s {} -t {} -f {}'.format(align_tool_path, source_language_file,
                                                                             target_language_file, output_file_dir))
            break
    break
