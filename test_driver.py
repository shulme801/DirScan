#!/usr/bin/env python3

import re
from file_system import dir_walk, count_occurrences

top_dir = ""
hidden_dirs = ""
searchable_files = ""
hidden_dirs      = re.compile(r'\.\w*')
searchable_files = re.compile(r'\.txt$')
top_dir          = '/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data'
print('------------------------------')
print(dir_walk(root=top_dir, ignore=hidden_dirs, search=searchable_files))

print("total is {}".format(str(count_occurrences("man","/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data/file_02.txt"))))