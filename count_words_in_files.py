#!/usr/bin/env python3


import os
import re

def dir_walk(**kwargs):
    """Returns a list of files in a dir tree whose name matches a reg ex
    
    This function is invoked with 0-3 arguments, as passed in via the 
    dictionary "kwargs".  It unpacks the kwargs dict.  It then performs 
    a top-down, recursive search of a directory tree (rooted at the 
    "root" argumemt).

    It bulds a list (called "file_list") of all the files found in 
    he directory tree that match the "include_file" argument.  
    It ignores directories that match the "ignore" argument.
    The function returns this file_list. 

    If the "root" argument is omitted, the function uses the current 
    working directory as the root.  
    If the "ignore"  argument is omitted, the function searches all 
    directories in the tree.  If the "include_files" argument is 
    omitted, all files in the tree are returned.
    """

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

def count_occurrences(word,in_file):
    """Returns number of times 'word' appears in 'in_file'"""
    
    occurrence_count = 0

    try:
        file_name = open(in_file,"r") 
    except EOFError as ex:
        print("Caught the EOF error when opening file {0}".format(str(in_file)))
        raise ex
    except IOError as eio:
        print("Caught the IOError when opening file {0}".format(str(in_file)))
        raise eio
    else:
        target_text = file_name.read()
        word_list = re.findall(word, target_text)
        occurrence_count += len(word_list)
        file_name.close()
    return(occurrence_count)

def count_all_occurrences(word_list, file_list):
    """Returns # of times the words in word_list occur in files of file_list

       Returns a dict whose keys are the words in the word_list argument, 
       and whose values are the count of the times the word appeared in 
       the files in the file_list argument """


    words_and_counts = {}
    
    for word in word_list:
        count = 0
        for file in file_list:
            count += count_occurrences(word,file)
        words_and_counts[word] = count

    return(words_and_counts)


        


    