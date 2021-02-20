#!/usr/bin/env python3

import os
import re

def dir_walk(**kwargs):

    top_dir      = kwargs.get("root")
    # ignore       = kwargs.get("ignore")
    searchable   = kwargs.get("search")

    if (not(os.path.isdir(top_dir))):
        top_dir = os.getcwd()

    print(top_dir)
    # print(ignore)
    print(searchable) #Could use the endswitch() method, but I wanted tp practice regular expressions
    file_list = []
    for root, dirs, files in os.walk(top_dir, topdown=True):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if (searchable.search(file)):
                #append the file name to the list
                file_list.append(os.path.join(root,file))
    return(file_list)
    

hidden_files     = re.compile(r'/\.\w+')
searchable_files = re.compile(r'\.txt$')
top_dir          = '/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data'
print(dir_walk(root=top_dir, ignore=hidden_files, search=searchable_files))