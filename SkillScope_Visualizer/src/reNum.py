# Arithmetic Operations
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    """Return the remainder of a divided by b."""
    return a % b

def exponentiate(a, b):
    """Raise a to the power of b."""
    return a ** b

def floor_divide(a, b):
    """Return the floor division of a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a // b

# Comparison Operations
def equal(a, b):
    """Check if two numbers are equal."""
    return a == b

def not_equal(a, b):
    """Check if two numbers are not equal."""
    return a != b

def greater_than(a, b):
    """Check if a is greater than b."""
    return a > b

def less_than(a, b):
    """Check if a is less than b."""
    return a < b

def greater_than_or_equal(a, b):
    """Check if a is greater than or equal to b."""
    return a >= b

def less_than_or_equal(a, b):
    """Check if a is less than or equal to b."""
    return a <= b

# Bitwise Operations
def bitwise_and(a, b):
    """Perform bitwise AND on two numbers."""
    return a & b

def bitwise_or(a, b):
    """Perform bitwise OR on two numbers."""
    return a | b

def bitwise_xor(a, b):
    """Perform bitwise XOR on two numbers."""
    return a ^ b

def bitwise_not(a):
    """Perform bitwise NOT on a number."""
    return ~a

def left_shift(a, b):
    """Perform bitwise left shift on a number."""
    return a << b

def right_shift(a, b):
    """Perform bitwise right shift on a number."""
    return a >> b

# Mathematical Functions
import math

def square_root(a):
    """Return the square root of a number."""
    if a < 0:
        return "Error: Negative value cannot have a real square root"
    return math.sqrt(a)

def power(a, b):
    """Return a raised to the power of b."""
    return math.pow(a, b)

def logarithm(a, base=10):
    """Return the logarithm of a number with a specified base."""
    if a <= 0:
        return "Error: Logarithm undefined for non-positive values"
    return math.log(a, base)

def factorial(a):
    """Return the factorial of a number."""
    if a < 0:
        return "Error: Factorial not defined for negative numbers"
    return math.factorial(a)

# Rounding Functions
def round_number(a, digits=0):
    """Round a number to the nearest specified digits."""
    return round(a, digits)

def ceil(a):
    """Return the smallest integer greater than or equal to a."""
    return math.ceil(a)

def floor(a):
    """Return the largest integer less than or equal to a."""
    return math.floor(a)

# Trigonometric Functions
def sine(a):
    """Return the sine of a number (in radians)."""
    return math.sin(a)

def cosine(a):
    """Return the cosine of a number (in radians)."""
    return math.cos(a)

def tangent(a):
    """Return the tangent of a number (in radians)."""
    return math.tan(a)

def radians(a):
    """Convert degrees to radians."""
    return math.radians(a)

def degrees(a):
    """Convert radians to degrees."""
    return math.degrees(a)

# Exponential and Logarithmic Functions
def exp(a):
    """Return e raised to the power of a."""
    return math.exp(a)

# Constants
def pi():
    """Return the value of pi."""
    return math.pi

def e():
    """Return the value of Euler's number."""
    return math.e