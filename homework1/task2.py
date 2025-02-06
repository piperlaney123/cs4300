def add(x,y):
    return x + y

def is_equivalent(data1,data2):
    return type(data1) == type(data2)

class TestClass:
    # test int and int
    def test1(self):
        assert is_equivalent(1,2) == True

    # test int and bool
    def test2(self):
        assert is_equivalent(1, False) == False

    # test bool and bool
    def test3(self):
        assert is_equivalent(False, True) == True

