# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
# mymodule/math_utils.py

"""
This module contains basic mathematical utility functions.
"""

def add(x, y):
    """
    Adds two numbers together.

    """
    return x + y

def subtract(x, y):
    """
    Subtracts one number from another.

    """
    return x - y

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b