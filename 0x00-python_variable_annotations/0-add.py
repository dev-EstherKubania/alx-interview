#!/usr/bin/env python3
"""
Module to demonstrate type annotations in Python
"""


def add(a: float, b: float) -> float:
    """
    Adds two floats.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b
