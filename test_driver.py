#!/usr/bin/env python3

import sys
import re
from file_system import dir_walk, count_occurrences, count_all_occurrences

top_dir = ""
hidden_dirs = ""
searchable_files = ""
hidden_dirs      = re.compile(r'\.\w*')
searchable_files = re.compile(r'\.txt$')
top_dir          = '/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data'
print('------------------------------')
file_list = dir_walk(root=top_dir, ignore=hidden_dirs, search=searchable_files)
word_list = ["there", "Michael", "running", "man"]
print("Final word counts are {0}".format(count_all_occurrences(word_list, file_list)))