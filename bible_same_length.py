# import os
from pathlib import Path

lan_to_file = {'deu': 'deu-x-bible-newworld', 'eng': 'eng-x-bible-newworld2013', 'fra': 'fra-x-bible-newworld',
               'fin': 'fin-x-bible-newworld', 'ces': 'ces-x-bible-newworld'}

bible_files = Path('./bible_files').glob('*.txt')

# check if we have the dirs for the files with same length
# for item in lan_to_file:
#     dir = './' + item + '_same_length'
#     if not os.path.exists(dir):
#         os.makedirs(dir)

for item in lan_to_file:
    print(item)
    lan_dic = {}
    with open('./bible_files/' + lan_to_file[item] + '.txt') as lan_file:
        lines = lan_file.readlines()
        for line in lines[11:]:
            lan_dic[line[:8]] = line[9:-1]
        print('language dic created')
    for bible in bible_files:
        lan = str(bible).split('/')[1].split('-')[0]
        if lan == item:
            print(str(bible) + ' is skipped!')
            continue
        else:
            other_lan_dic = {}
            # same_length_dic = {}
            file_dir = './' + item + '_same_length/'
            file_name = item + '-' + str(bible).split('/')[1]
            with open(bible) as other_lan_file:
                lines = other_lan_file.readlines()
                for line in lines[11:]:
                    other_lan_dic[line[:8]] = line[9:-1]
            with open(file_dir + file_name, 'a+') as file:
                for other_lan_item in other_lan_dic:
                    if other_lan_item in lan_dic:
                        file.write(lan_dic[other_lan_item] + '\n')
                        # same_length_dic[other_lan_item] = lan_dic[other_lan_item]
