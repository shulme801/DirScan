#!/usr/bin/env python3

import os
import re

def dir_walk(**kwargs):

    top_dir      = kwargs.get("root")
    ignore       = kwargs.get("ignore")
    searchable   = kwargs.get("search")

    if (not(os.path.isdir(top_dir))):
        top_dir = os.getcwd()

    file_list = []
    for root, dirs, files in os.walk(top_dir, topdown=True):
        print(dirs)
        # could have used dirs[:] = [d for d in dirs if not d.startswith('.')] instead of a regular expression      
        dirs[:] = [d for d in dirs if not ignore.search(d)]
        for file in files:
            if (searchable.search(file)): #Could use the endswith() method, but I wanted tp practice regular expressions
                #append the file name to the list
                file_list.append(os.path.join(root,file))
    return(file_list)
    

hidden_files     = re.compile(r'/\.\w+')
searchable_files = re.compile(r'\.txt$')
top_dir          = '/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data'
print(dir_walk(root=top_dir, ignore=hidden_files, search=searchable_files))