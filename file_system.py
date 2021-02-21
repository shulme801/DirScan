#!/usr/bin/env python3


import os
import re

def dir_walk(**kwargs):
    '''
    DOCSTRING: This function is invoked with 0-3 arguments, as passed in via the dictionary "kwargs".  It unpacks the kwargs dict.  It then performs a top-down, recursive search of a directory tree (rooted at the "root" argumemt).
    It bulds a list (called "file_list") of all the files found in the directory tree that match the "include_file" argument.  It ignores directories that match the "ignore" argument.
    The function returns the file_list. 

    If the "root" argument is omitted, the function uses the current working directory as the root.  If the "ignore"  argument is omitted, the function searches all 
    directories in the tree.  If the "include_files" argument is omitted, all files in the tree are returned.
    '''

    top_dir        = kwargs.get("root")
    ignore         = kwargs.get("ignore")
    include_files   = kwargs.get("search")

    if (not(os.path.isdir(top_dir))):
        top_dir = os.getcwd()

    if ignore == "":
        ignore = re.compile(r'\n') #we will ignore no directory names...directory names cannot contain a newline, so this pattern will never match

    if include_files == "":
        include_files = re.compile(r'.') # Any file name should match


    file_list = []
    for root, dirs, files in os.walk(top_dir, topdown=True):   
        dirs[:] = [d for d in dirs if not ignore.match(d)]
        
        for file in files:
            if (include_files.search(file)): 
                #append the file name to the list
                file_list.append(os.path.join(root,file))

    return(file_list)
    