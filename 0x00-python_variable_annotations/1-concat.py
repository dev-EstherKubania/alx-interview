#!/usr/bin/env python3
"""
Module to demonstrate type annotations in Python
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
