"""
This program calculates the final price of a product after applying a given discount percentage inside of a function named calculate_discount;
the function accepts any numeric type for price and discount. pytest cases are used to test functionality. 
"""

# returns the final price of an item based on discount. receives any numeric values for price, discount: duck typing 
# discount given in form of percentage
def calculate_discount(price, discount):
    return round((price - (price * (discount / 100))), 2)



