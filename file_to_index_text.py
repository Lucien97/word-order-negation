import os
import re
from pathlib import Path

bible_files = Path('./bible_files').glob('*.txt')

os.makedirs('./bible_text')
os.makedirs('./bible_index')

for bible in bible_files:
    directory, file_name = str(bible).split('/')
    with open(bible) as source_file, \
            open('./bible_text/' + file_name, 'a+') as text_file, \
            open('./bible_index/' + file_name, 'a+') as index_file:
        lines = source_file.readlines()
        save_flag = 0
        for line in lines:
            if save_flag:
                try:fi
                    index, content = line.split('\t')
                    index = ''.join(re.findall(r'\d', index))
                    text_file.write(content)
                    index_file.write(index + '\n')
                except ValueError as ve:
                    print(file_name)
                    print(line[:-1])
                    print(ve)
                    print('\n')
            if 'notes' in line:
                save_flag = 1
