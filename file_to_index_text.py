import os
from pathlib import Path

bible_files = Path('./corpus').glob('*.txt')

# os.makedirs('./bible_text')
# os.makedirs('./bible_index')

for bible in bible_files:
    directory, file_name = str(bible).split('/')
    with open(bible) as source_file, \
            open('./bible_text/' + file_name, 'a+') as text_file, \
            open('./bible_index/' + file_name, 'a+') as index_file:
        lines = source_file.readlines()
        for line in lines[11:]:
            index = line[:9]
            content = line[9:]
            text_file.write(content)
            index_file.write(index + '\n')