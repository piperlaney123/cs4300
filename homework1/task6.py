"""
This program reads a file and counts the number of words in it using metaprogramming techniques to dynamically generate function names for pytest 
test cases based on the filenames of the text files. Pytest is also used to verify the word count for each text file. 

metaprogramming: "programming technique where a program can modify or generate code at runtime. It allows developers to write code that can analyze, 
modify, or create other code. In other words, metaprogramming is a way of writing programs that manipulate programs."
- https://dev.to/karishmashukla/a-practical-guide-to-metaprogramming-in-python-691

in this case, we're using metaprogramming for dynamic code generation. we'll use exec() function -- dynamic execution of Python programs 
"""

import string

def count_words_in_file(filename):

    word_count = 0
    # since using with, dont have to explicitly close file
    with open("task6_read_me.txt", "r") as file:
        for line in file:
            for word in line.split():
                if word not in string.punctuation:
                    word_count += 1

    return word_count


#print(count_words_in_file("task6_read_me.txt"))

