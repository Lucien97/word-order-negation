import os
from file_processing import file2dic, dic_compare
from pathlib import Path


deu_source_file = '/Users/chen/Typology/bible_files/deu-x-bible-newworld.txt'
deu_dic = file2dic(deu_source_file)

ca_files = Path('/Users/chen/Typology/Central_Africa').glob('*.txt')

for ca_file in ca_files:
    ca_file_dic = file2dic(ca_file)
    ca_deu_dic = dic_compare(deu_dic, ca_file_dic)
    index_file_name = ca_file.name
    index_file_dir = '/Users/chen/Typology/deu_indexes/'
    with open('/Users/chen/Typology/maceflomal/s_temp_file.txt', 'a+') as s_file, \
            open('/Users/chen/Typology/maceflomal/t_temp_file.txt', 'a+') as t_file, \
            open(index_file_dir + index_file_name, 'a+') as index_file:
        for item in ca_deu_dic:
            index_file.write(item + '\n')
            s_file.write(ca_deu_dic[item][0] + '\n')
            t_file.write(ca_deu_dic[item][1] + '\n')
    os.system('python3 {} --overwrite -m 3 -s {} -t {} -f {} -r {}'.format('align.py', 's_temp_file.txt',
                                                                           't_temp_file.txt', 'forward.txt',
                                                                           'reverse.txt'))

    break
