from homework1.task2 import *

class TestClass:
    # testing is_equivalent func
    # test int and int 
    def test1(self):
        assert is_equivalent(1,2) == True

    # test int and bool 
    def test2(self):
        assert is_equivalent(1, False) == False

    # test bool and bool 
    def test3(self):
        assert is_equivalent(False, True) == True

    # test int and float 
    def test4(self):
        assert is_equivalent(2, 3.6) == False

    # test string and bool 
    def test5(self):
        assert is_equivalent("hello!", False) == False

    # testing add func
    # test adding int and int
    def test6(self):
        assert type(add(2,2)) == int
        assert add(2,2) == 4
    
    # test adding float and float
    def test7(self):
        assert type(add(3.4, 9.5)) == float
        assert add(3.4, 9.5) == 12.9

    # test adding float and int
    def test8(self):
        assert type(add(1.2, 9)) == float
        assert add(1.2, 9) == 10.2