def say_hi():
    return "Hello, World!"


def test_say_hi():
    assert say_hi() == "Hello, World!"


print(say_hi())
test_say_hi()