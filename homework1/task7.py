"""
This program plays around with numpy and matplotlib. It uses pytest to verify its correctness.
"""
import numpy as np
import random
import matplotlib.pyplot as plt

# in this program, we'll create a random array using numpy and plot it using matplotlib.
# for pytest, we'll check array length, type, and max and min.

# creates array with np; recieves length of array, returns np array
def create_random_array(length):
    # create array according to passed length of random numbers ranging from 1 to 10 using list comprehension 
    an_array = np.array([random.randint(1,10) for x in range(length)])
    return an_array

# count items in array; receives np array, returns length as int
def count_array_length(a):
    length = 0
    for x in a:
        length += 1
    return length

# finds the max value of array; receives np array, returns max value of np array
def find_max(a):
    max = a[0]
    for x in range(1, len(a)):
        if a[x] > max:
            max = a[x]

    return max

# finds the min value of array; receives np array, returns min value of np array
def find_min(a):
    min = a[0]
    for x in range(1, len(a)):
        if a[x] < min:
            min = a[x]

    return min

# plots an np array as a graph; recieves np array
def plot(a):
    plt.plot(a)
    plt.xlabel("Array indices")
    plt.ylabel("Array values")
    plt.title("Graph of Array")
    # save plot to output file, tried to do plt.show() but didnt work...
    plt.savefig("output_graph.jpg")

# test w/ pytest
class TestClass:
    test_array = create_random_array(10)
    
    # test array func
    def test_create_array_func(self):
        assert type(self.test_array) == type(np.array([1, 2, 3]))

    # test count length func with np's built-in size func
    def test_length_func(self):
        assert np.size(self.test_array) == count_array_length(self.test_array)

    # test max func with np's built-in max func
    def test_max_func(self):
        assert np.max(self.test_array) == find_max(self.test_array)

    # test min func with np's built-in min func
    def test_min_func(self):
        assert np.min(self.test_array) == find_min(self.test_array)



'''
my_array = create_random_array(10)
a_length = count_array_length(my_array)
a_max = find_max(my_array)
a_min = find_min(my_array)

print(my_array)
print(a_length)
print(a_max)
print(a_min)
plot(my_array)
'''