#!/usr/bin/env python3


import os
import re
from collections import defaultdict

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

def count_all_occurrences(word_list, file_list):
    """Returns # of times the words in word_list occur in files of file_list

       Returns a dict whose keys are the words in the word_list argument, 
       and whose values are the count of the times the word appeared in 
       the files in the file_list argument """


    totals_by_word = []
    #initialize a tuple of (word,0) for each word, and store it in the list 'totals_by_word'
    for word in word_list: 
        temp = (word,0)
        totals_by_word.append(temp)
    
    running_totals = defaultdict(list)
    final_totals   = defaultdict(list)
    word_total     = 0

    #now, create a dictionary-like object. For each word, you'll have a list that contains the number of 
    #occurrences of that word, found in each file.
    for k,v in totals_by_word:
        running_totals[k].append(v)

    
    # The following code counts the occurences of every word in every file,
    # one file at a time, and stores that occurrence count in running_totals[word].

    for file in file_list:
        try:
            file_name = open(file,"r") 
        except EOFError as ex:
            print("Caught the EOF error when opening file {0}".format(str(file)))
            raise ex
        except IOError as eio:
            print("Caught the IOError when opening file {0}".format(str(file)))
            raise eio
        except:
            print("Caught an unknown error!")
        else:
            target_text = file_name.read()
            for word in word_list:
                word_occurrences = re.findall(word, target_text)
                running_totals[word].append(len(word_occurrences))
            file_name.close()

    for word in word_list:
        word_total    = sum(running_totals[word])
        final_totals[word].append(word_total)

    return(final_totals)



        


    