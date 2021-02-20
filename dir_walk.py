#!/usr/bin/env python3

import os
import re

def dir_walk(dir):
    cwd = os.getcwd()

    #we will store all the file names in this list
    file_list = []

    for root, dirs, files in os.walk(cwd):
        for file in files:
            #append the file name to the list
            file_list.append(os.path.join(root,file))
    return(file_list)
#print all the file names

def test_unpacking(**kwargs):
    #kwargs is a dict

    ignore   = kwargs.get("ignore")
    search   = kwargs.get("search")

    print(ignore)
    ignotus = ignore.search('Volumes/Hulme_Local_Extended/src/Python/DirScan/.git/packed-refs')
    if ignotus:
        print('match found: ',ignotus.group())
    else:
        print('match not found')

    
    
# for name in dir_walk("/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data"):
#     print(name)
hidden_files     = re.compile(r'/\.\w+')
searchable_files = re.compile(r'\.txt$')
test_unpacking(ignore=hidden_files,search=searchable_files)
# x = re.compile(hidden_files)
# m = x.search('/Volumes/Hulme_Local_Extended/src/Python/DirScan/.git/packed-refs')
# if m:
#         print('match found: ',m.group())
# else:
#         print('match not found')


# 