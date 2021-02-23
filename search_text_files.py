#!/usr/bin/env python3

import sys
import re
import os
from collections import defaultdict

from count_words_in_files import dir_walk, count_all_occurrences

"""Counts # of times words appear in the text files in a dir tree

Requires that user invoke it from the command line, specifying the 
root directory and a list of words to search for.  

It ignores hidden directories (those that start with "."). It 
only searches for word occurrences within files whose 
extension is ".txt".
"""


top_dir          = ""
hidden_dirs      = ""
searchable_files = ""
hidden_dirs      = re.compile(r'\.\w*')
searchable_files = re.compile(r'\.txt$')
output_totals    = defaultdict(list)

n = len(sys.argv)
if (n <= 3):
    print("Please supply directory root where you want to start the search, and some words to search for!")
else:
    top_dir = sys.argv[1]
    if (not(os.path.isdir(top_dir))):
        print("Error -- root directory that you supplied is invalid!")
    else:
        word_list = sys.argv[2:]
        print('------------------------------') # Strictly for show
        file_list = dir_walk(root=top_dir, ignore=hidden_dirs, search=searchable_files)
        output_totals = count_all_occurrences(word_list, file_list)

        print("Final Word Counts are:")
        for k in output_totals:
            print(k,sep=" ",end=" ")
            print(output_totals.get(k))
            