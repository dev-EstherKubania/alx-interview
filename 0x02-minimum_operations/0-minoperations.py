#!/usr/bin/python3
"""
Module to calculate the minimum operations to achieve characters 'H'
"""

def minOperations(n):
    """
    Calculate the fewest operations that result in n H characters.

    Args:
        n (int): The target number of characters 'H'.

    Returns:
        int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
