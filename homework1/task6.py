"""
This program reads a file and counts the number of words in it using metaprogramming techniques to dynamically generate function names for pytest 
test cases based on the filenames of the text files. Pytest is also used to verify the word count for each text file. 

metaprogramming: "programming technique where a program can modify or generate code at runtime. It allows developers to write code that can analyze, 
modify, or create other code. In other words, metaprogramming is a way of writing programs that manipulate programs."
- https://dev.to/karishmashukla/a-practical-guide-to-metaprogramming-in-python-691

"""

import string
import os

# counts words in a txt file; receives a file object, returns word count 
def count_words_in_file(filename):

    word_count = 0
    # since using with, dont have to explicitly close file
    with open(filename, "r") as file:
        for line in file:
            for word in line.split(): # split spaces
                if word not in string.punctuation: # ignore punctuation 
                    word_count += 1

    return word_count


# set and change to appropriate directory
directory = os.getcwd() + "/txt_files"
os.chdir(directory)


# go through all txt files to execute all tests
for file in os.listdir(directory):
    # get word count
    word_count = count_words_in_file(file)
    # dynamically create appropriate func name according to txt file being counted
    # add test before file name so pytest will register it and test it
    # also splitting at . because thats not a valid func name
    func_name = "test_" + file.split(".")[0]

    # create the test function dynamically
    # have to pass in the file and word count for word counting func & test
    # note that this func begins with _ ; this is bc we dont want pytest to test this func. 
    # ((i guess i could have named it w/o test but the naming convention makes sense to me))
    def _test_func(file=file, expected_word_count=word_count):
        assert count_words_in_file(file) == expected_word_count

    # globals() func in python: returns a dictionary representing the current global symbol table... ie, variables, functions, etc
    # we need to be sure that the dynamically created functions are defined in the global scope so pytest can see them 
    # attach the dynamically made function to the global scope
    globals()[func_name] = _test_func