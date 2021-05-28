"""This class reverse list and iterates on it"""
class Reverse_iter():
    def __init__(self, list):
        self.list = list
        self.index = len(list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.list[self.index]
        else:
            raise StopIteration()

iterator = Reverse_iter([1,3,5,7,9,11,13,15,17,19])
for i in iterator:
    print(i)
# OUTPUT : 19 17 15 13 11 9 7 5 3 1

"""Program that takes filename(s) as arguments and prints
all the names which are longer than 40 characters"""
import os
from pathlib import Path

def fourty_characters(list, length = 40):
    return(name for name in list if len(name) > length)

def files_from_directory(directory):
    filenames = []
    for roots, dirs, files in os.walk(directory):
        for filename in files:
            filenames.append(os.path.join(roots,filename))
    return filenames

directory = "wiki_articles\\"
names = files_from_directory(directory)
result = fourty_characters(names,40)
for i in result:
    print(i)
#OUTPUT:wiki_articles\ml_frameworks\tensorflow.txt
#wiki_articles\programming_languages\compiled\c++.pdf
#wiki_articles\programming_languages\compiled\java.txt
#wiki_articles\programming_languages\interpreted\python.txt
#wiki_articles\programming_languages\interpreted\r.docx


"""
Generates all paths in directory tree
"""
def findfiles(directory):
    filenames = []
    for roots, dirs, files in os.walk(directory):
        for filename in files:
            filenames.append(os.path.join(roots,filename))
    return filenames

directory = "wiki_articles\\"
all_paths = findfiles(directory)
for file in all_paths:
    print(file)
""" OUTPUT
wiki_articles\ml_frameworks\pytorch.txt
wiki_articles\ml_frameworks\tensorflow.txt
wiki_articles\programming_languages\compiled\c++.pdf
wiki_articles\programming_languages\compiled\java.txt
wiki_articles\programming_languages\interpreted\python.txt
wiki_articles\programming_languages\interpreted\r.docx
"""

"""
Program that takes integer n and a filename and splits
the file into multiple small files with each have n lines
"""
def split_file(n,file):
    generator = (file_line for file_line in file.readlines())
    flag = 1
    while True:
        with open("output.{}.txt".format(flag),"w") as fw:
            for i in range(n):
                try:
                    fw.write(next(generator))
                except StopIteration:
                    print("You get the end of a file")
                    return
            flag += 1
    

with open("java.txt","r") as f:
    split_file(2,f)
    """2 new files with 2 and 1 line of text as output"""

"""
Program that compute all lines of python script ignoring empty and comment lines
(Including docstrings)
"""

def files_from_directory(directory, extensions):
    for roots, dirs, files in os.walk(directory):
        for filename in files:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                yield os.path.join(roots, filename)


def compute_lines(directory, extensions = ['.py']):
    count = 0
    generator = files_from_directory(directory, extensions)
    for file in generator:
        with open(file, 'r') as f:
            for string in f.readlines():
                if not(string[0] == '#' or string == ' '):
                    count += 1
    return count

total = compute_lines('C:\\Users\\andrl\\OneDrive\\Рабочий стол\\Allcodes')
print(total)
#OUTPUT: 80
