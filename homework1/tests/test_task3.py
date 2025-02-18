from homework1.task3 import *

# testing w/ pytest
class TestClass:

    def test_determine_number_1(self):
        assert determine_number(9) == "You entered a positive number."

    def test_determine_number_2(self):
        assert determine_number(-8) == "You entered a negative number."

    def test_determine_number_3(self):
        assert determine_number(0) == "You entered zero."
    
    def test_determine_number_4(self):
        assert determine_number(0.5) == "You entered a positive number."
    
    def test_determine_number_5(self):
        assert determine_number(-100.23) == "You entered a negative number."

    def test_generate_prime_nums(self):
        assert generate_prime_nums() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_find_sum_100(self):
        assert find_sum_100() == 5050