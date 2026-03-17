"""A simple calculator module used as a demo for Claude Code CI/CD."""
import math


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sqrt(n: float) -> float:
    """Calculate square root of a non-negative number."""
    if n < 0:
        raise ValueError("Input must be a non-negative number")
    return n ** 0.5

def tangent(x: float) -> float:
    """Calculate tangent of an angle in radians."""
    return math.tan(x)

def sin(x: float) -> float:
    """Calculate sine of an angle in radians."""
    return math.sin(x)
