This repo is for my graduation thesis on language typology.
And hope I can graduate in time.


Update on 19th April:

1. Find preferred sources based on the json file provided by Robert;
2. Use Stanza to do POS-taging and dependency parsing on deu-x-bible-newworld, eng-x-bible-newworld2013 and fra-x-bible-newworld. (More files to be processed, time permitting.)

Update on 20th April:

1. Use stanza to do POS-tagging and dependency parsing on fin-x-bible-newworld.txt to make source languages more diverse;
2. Now I have indexes and (pure) content for word alignment.

Update on 21st April:

1. Now I can get some results from word alignment by writing a command line in terminal;
2. Tried to automate the alignment pipeline of thousands of files. Now I have a prototype that works for a single file.

Update on 22nd April:

1. Now the prototype if refined further, considering different index cross bible files, though only one language works out from the code with five languages in the same for loop.

To do list:

1. To make the automated alignment pipeline work for other languages except for German.
2. Think about the pipeline for the projection.
3. Start writing.

For Cui:

I've uploaded the python script called "bible_same_length.py" where the for loop is wrong. Please check it yourself.