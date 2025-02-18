"""
This program tests if an input number is positive, negative, or zero, implements a for loop to calculate the first 10 prime numbers, 
and implements a while loop to find the sum of all numbers from 1 to 100. Additionally, it uses pytest to test for expected output.
"""
import math

# determines if number is pos, neg, or 0; recieves an number (float or int)
def determine_number(num):
    if num < 0:
        return "You entered a negative number."
    elif num > 0: 
        return "You entered a positive number."
    else:
        return "You entered zero."

# determines if number is prime; recieves an int
def is_prime(num):
    '''
    simple way to calc prime nums: divsor d of n means (n/d) is also a divisor of n. 
    if d <= sqrt(n) --> n/d >= sqrt(n) --> only need to check for divisors up to sqrt(n)
    '''
    # no nums below 2 are prime
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1): # make sure to add 1 because last num isn't inclusive 
            if num % i == 0:
                return False
            
        return True

# prints first 10 prime numbers, return list of first 10 prime numbers
def generate_prime_nums():
    prime_nums = []
    num = 0

    # find prime nums until we have the first 10 
    while len(prime_nums) < 10:
        num += 1
        if is_prime(num):
            prime_nums.append(num)
    
    print(prime_nums)
    return prime_nums

# finds sum from all numbers from 1 to 100; returns sum 
def find_sum_100():
    count = 0
    sum = 0
    while count < 100:
        count += 1
        sum += count
        
    print(sum)
    return(sum)


generate_prime_nums()
find_sum_100()

