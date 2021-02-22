# DirScan Project

This project extends the final assignment of the excellent Udemy course "The Complete Python Developer Certification Course", by Imtiaz Ahmad.

The project extends -- and, I hope, improves upon -- Section 6 assignment 1 by

* Defining 3 utility functions, each of which has a specific job, and which are packaged in a python module.
  * **dir_walk** performs a top-down, recursive scan of a directory tree. It returns a list of all the files it encounters that match a regular expression.  It ignores directories that match another regular expression.  The directory tree to be scanned and the two regular expressions are arguments to this function.  
  * **count_occurrences** returns the number of times a word occurs in a single file.
  * **count_all_occurrences** calls **count_occurrences** for each word in a word list and file in a list of files.

These functions are imported into the driver program **search_text_files.py**.
This driver program allows the user to search for a list of words in all text files contained in a directory tree.  The driver program is invoked from the command line.  It takes command line arguments for

* The root of the directory tree
* List of words to search for in the text files in that directory tree

search_text_files.py prints, for each word specified on the command line, the number of time it was found in the text files in the directory tree.
