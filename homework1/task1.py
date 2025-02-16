"""
This program prints a string on the console and uses pytest to verify the output.
"""

def say_hi():
    return "Hello, World!"


def test_say_hi():
    assert say_hi() == "Hello, World!"


print(say_hi())
test_say_hi()