# DirScan Project

This project extends the final assignment (Section 6 Assignment 1) of the excellent Udemy course "The Complete Python Developer Certification Course", by Imtiaz Ahmad.

The assignment was to write python code that, given a root directory and a list of words:

* walks through the directory tree, starting at the root directory
* searches each text file encountered for the words in the word list
* returns the count of occurrences for each word

## The Default Solution

The solution provided in the course follows an algorithm in which, for each word, a recursive search for file names is performed and, as files are located, they are searched for the word. This approach works, but it requires a recursive descent of the directory tree for each word, and opening/closing each file for each word.

## My Solution

My approach, I believe, reduces both processor load and file I/O:

* The code recurses down the directory tree only **once**, building a list of files to be searched as it goes.

* Once the file list is built, the code then opens each file in the list and searches that file for occurrences of each word in the list.

## Project Structure

The program "**search_text_files.py**" is the driver program.  It is invoked from the command line with at least 2 arguments.  The first is the root directory.  The second (and, optionally, other) arguments are words to be searched for (search terms).  **search_text_files.py** prints, for each search term, the total number of times it appeared in the files.

## Details

The project also:

* Defines 2 utility functions, each of which has a specific job, and which are packaged in a python module.
  
  * **dir_walk** performs a top-down, recursive scan of a directory tree. It returns a list of all the files it encounters that match a regular expression.  It ignores directories that match another regular expression.  The directory tree to be scanned and the two regular expressions are arguments to this function.  

  * **count_all_occurrences** utilizes a "[defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)" object to track the running totals of occurrences of each of the search terms.  This object has a key for each of the search words.  Each key references a list.  
    * As each file is searched for each search term, the count of occurrences in the file is appended to that word's list.  
    * When all files have been searched for all search terms, we have a dictionary with, for each search term, a list of the number of occurrences of the term in each file.  The sum() function is used on these lists to find the total number of occurrences for each search term.

## Test Data

The course provides a set of text files, containing several of the works of Shakespeare.  These are unformatted ascii text files.

## Acknowledgement

The Udemy course "The Complete Python Developer Certification Course", was produced and recorded by Imtiaz Ahmad.  The presentation and content of the course are quite good.  While my approach to this project differs from that in the course, please note that this course provided me with the tools and test data to create my own solution.

## License

Copyright 2021 Pilgrim Marine Consultants

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

No commercial use may made of the Software.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
