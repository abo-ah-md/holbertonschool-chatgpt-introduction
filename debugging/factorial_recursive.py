#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    
    Raises:
        RecursionError: If n is too large.
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <non-negative-integer>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        result = factorial(num)
        print(result)
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)
    except RecursionError:
        print("Number too large, recursion depth exceeded.")
        sys.exit(1)
