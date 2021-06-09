"""Another module."""

from ..package1.module1 import add_two_numbers, multiply_two_numbers 

def multiply_then_add(a, b, c):
    """Multiplies then adds.

    Args:
        a (int): First number to sum.
        b (int): Second number to sum.
        c (int): Multiplier.

    Returns:
        int: Result of sum and product.
    """
    sum_val = add_two_numbers(a, b)
    result = multiply_two_numbers(sum_val, c)
    return result 


def new_function_v2():
    """Display string for version 2.

    Returns:
        str: Describes version.
    """
    return "This is version 2."