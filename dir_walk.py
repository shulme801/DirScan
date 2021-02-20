#!/usr/bin/env python3

import os

cwd = os.getcwd()

#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(cwd):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    print(name)