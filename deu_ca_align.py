import os
import bible_file_processing
import alignment_intersection
from pathlib import Path


deu_source_file = '/Users/chen/Typology/bible_files/deu-x-bible-newworld.txt'
deu_dic = bible_file_processing.file2dic(deu_source_file)

ca_files = Path('/Users/chen/Typology/Central_Africa').glob('*.txt')

for ca_file in ca_files:
    ca_lan_name = ca_file.name.split('-')[0]
    ca_file_dic = bible_file_processing.file2dic(ca_file)
    ca_deu_dic = bible_file_processing.dic_compare(deu_dic, ca_file_dic)
    with open('/Users/chen/Typology/maceflomal/s_temp_file.txt', 'a+') as s_file, \
            open('/Users/chen/Typology/maceflomal/t_temp_file.txt', 'a+') as t_file:
        for item in ca_deu_dic:
            s_file.write(ca_deu_dic[item][0] + '\n')
            t_file.write(ca_deu_dic[item][1] + '\n')
    os.chdir('/Users/chen/Typology/maceflomal')
    os.system('python3 {} --overwrite -m 3 -s {} -t {} -f {} -r {}'.format('align.py', 's_temp_file.txt',
                                                                           't_temp_file.txt', 'forward.txt',
                                                                           'reverse.txt'))
    final_align = alignment_intersection.align_check(ca_deu_dic, 'forward.txt', 'reverse.txt')
    with open('/Users/chen/Typology/maceflomal/deu-' + ca_lan_name + '.txt', 'a+') as final_file:
        for item in final_align:
            final_file.write(item + '\t')
            final_file.write(final_align[item] + '\n')
    break
