#!/usr/bin/env python3
"""
Module to demonstrate type annotations in Python
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)
