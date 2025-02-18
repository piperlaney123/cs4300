from homework1.task4 import *

# testing w/ pytest
class TestClass:
    # int and int
    def test_calculate_discount_1(self):
        assert calculate_discount(100,50) == 50

    # float and int
    def test_calculate_discount_2(self):
        assert calculate_discount(305.69, 24) == 232.32

    # float and float
    def test_calculate_discount_3(self):
        assert calculate_discount(34.79, 12.67) == 30.38