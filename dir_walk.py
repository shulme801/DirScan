#!/usr/bin/env python3

import os

def dir_walk(dir):
    cwd = os.getcwd()

    #we shall store all the file names in this list
    file_list = []

    for root, dirs, files in os.walk(cwd):
        for file in files:
            #append the file name to the list
            file_list.append(os.path.join(root,file))
    return(file_list)
#print all the file names
for name in dir_walk("/Volumes/Hulme_Local_Extended/src/Python/DirScan/test_data"):
    print(name)