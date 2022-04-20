import stanza

# preferred_source = ['afr-x-bible-newworld', 'bel-x-bible-bokun', 'bul-x-bible-newworld', 'cat-x-bible-inter',
#                     'ces-x-bible-newworld', 'dan-x-bible-newworld', 'deu-x-bible-newworld', 'ekk-x-bible-1997',
#                     'ell-x-bible-newworld', 'eng-x-bible-newworld2013', 'epo-x-bible', 'eus-x-bible-batua',
#                     'fin-x-bible-newworld', 'fra-x-bible-newworld', 'gle-x-bible', 'hin-x-bible-bsi',
#                     'hrv-x-bible-newworld', 'hun-x-bible-newworld', 'hye-x-bible-newworld', 'ind-x-bible-newworld',
#                     'ita-x-bible-newworld', 'kat-x-bible-revised', 'kor-x-bible-newworld2014', 'lav-x-bible',
#                     'lit-x-bible-tikejimozodis', 'mkd-x-bible-2004', 'nld-x-bible-newworld', 'nno-x-bible-1978',
#                     'nob-x-bible-newworld', 'pol-x-bible-newworld', 'por-x-bible-newworld1996',
#                     'ron-x-bible-newworld', 'rus-x-bible-newworld', 'slk-x-bible-newworld', 'slv-x-bible-newworld',
#                     'sme-x-bible', 'spa-x-bible-newworld', 'sqi-x-bible-interconfessional', 'swe-x-bible-newworld',
#                     'tur-x-bible-newworld', 'ukr-x-bible-2009', 'vie-x-bible-newworld', 'zsm-x-bible-goodnews']

file_to_language = {'deu-x-bible-newworld': 'de', 'eng-x-bible-newworld2013': 'en', 'fra-x-bible-newworld': 'fr',
                    'fin-x-bible-newworld': 'fi', 'spa-x-bible-newworld': 'es', 'swe-x-bible-newworld': 'sv',
                    'ces-x-bible-newworld': 'cs'}
stanza.download('fr')
nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma,depparse')

with open('./bible_files/fra-x-bible-newworld.txt') as file:
    lines = file.readlines()

for line in lines[11:]:
    doc = nlp(line[9:])
    for sent in doc.sentences:
        with open('./bible_files/pos-fra-x-bible-newworld.txt', 'a+') as pos_file, \
                open('./bible_files/dep-fra-x-bible-newworld.txt', 'a+') as dep_file:
            pos_file.write(f'#{line[:9]}')
            pos_file.write('\n')
            dep_file.write(f'#{line[:9]}')
            dep_file.write('\n')
            for word in sent.words:
                pos_file.write(f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')
                pos_file.write('\n')
                dep_file.write(f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}')
                dep_file.write('\n')
