"""
This program calculates the final price of a product after applying a given discount percentage inside of a function named calculate_discount;
the function accepts any numeric type for price and discount. pytest cases are used to test functionality. 
"""

# returns the final price of an item based on discount. recieves any numeric values for price, discount: duck typing 
# discount given in form of percentage
def calculate_discount(price, discount):
    return round((price - (price * (discount / 100))), 2)

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

