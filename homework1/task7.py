"""
This program plays around with numpy and matplotlib. It uses pytest to verify its correctness.
"""
import numpy as np
import random
import matplotlib.pyplot as plt

# in this program, we'll create a random array using numpy and plot it using matplotlib.
# for pytest, we'll check array length, type, and max and min.

def create_random_array(length):
    # create array according to passed length of random numbers ranging from 1 to 10 using list comprehension 
    an_array = np.array([random.randint(1,10) for x in range(length)])
    return an_array

def count_array_length(a):
    length = 0
    for x in a:
        length += 1
    return length

def find_max(a):
    max = a[0]
    for x in range(1, len(a)):
        if a[x] > max:
            max = a[x]

    return max

def find_min(a):
    min = a[0]
    for x in range(1, len(a)):
        if a[x] < min:
            min = a[x]

    return min

def plot(a):
    plt.plot(a)
    plt.xlabel("array indices")
    plt.ylabel("array values")
    plt.title("Graph of Array")
    # save plot to output file, tried to do plt.show() but didnt work...
    plt.savefig("output_graph.jpg")





my_array = create_random_array(10)
a_length = count_array_length(my_array)
a_max = find_max(my_array)
a_min = find_min(my_array)

print(my_array)
print(a_length)
print(a_max)
print(a_min)
plot(my_array)