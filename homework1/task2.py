"""
This program plays around with data types (int, float, string, boolean) and uses pytest to test for expected outcomes when 
mixing data types. 
"""
def add(x,y):
    return x + y

def is_equivalent(data1,data2):
    return type(data1) == type(data2)
