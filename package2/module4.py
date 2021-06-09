from ..package1.module1 import add_two_numbers, multiply_two_numbers

def multiply_then_add(a, b, c):
    sum_val = add_two_numbers(a, b)
    result = multiply_two_numbers(sum_val, c)
    return result 
