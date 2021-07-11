"""
This module provides access to many math functions and constants from many areas of mathematics.
Constants:
...

Functions:
gcd -> Greatest Common Divisor.
lcm -> Least Common Multiple.
isCoprime -> Are two numbers co-prime.
triangelNumber -> Find nth triangle number.
"""


# Number Theory --------------------------------------------------------------------------------------------------------
def gcd(a: int, b: int) -> int:
    """
    Greatest Common Divisor.

    Returns the greatest common divisor of two integers.

    :param a: int
    :param b: int
    :return: int
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Least Common Multiple

    Returns the lowest multiple of two integers.

    :param a: int
    :param b: int
    :return: int
    """
    return a * b // gcd(a, b)


def isCoprime(a: int, b: int) -> bool:
    """
    Takes two integers and determines whether or not they are co-prime with one another.

    :param a: int
    :param b: int
    :return: bool
    """
    return 1 == gcd(a, b)


def triangleNumber(n: int) -> int:
    return n * (n + 1) // 2


def primeFactors(n: int) -> list:
    if n == 1:
        return [0]
    a = []
    nSquare = int(n ** 0.5)
    for i in range(2, nSquare + 1):
        if n % i == 0:
            a.append(i)
            return a + primeFactors(int(n / i))
    a.append(n)
    return a


# Number of divisors of an integer.
def tau(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    pFactors = primeFactors(n)
    a = []
    j = -1
    for i in pFactors:
        if j != i:
            j = i
            a.append(pFactors.count(i))
    divisors = 1
    for i in a:
        divisors *= i + 1
    return divisors


def properDivisors(n: int) -> list:
    a = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            a.append(i)
    return a


def isAmicablePair(a: int, b: int) -> bool:
    return a != b and sum(properDivisors(a)) == b and sum(properDivisors(b)) == a


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def factorial(n: int) -> int:
    if 0 == n:
        return 1
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


# Vector Calculus ------------------------------------------------------------------------------------------------------
class vector(object):
    def __init__(self, *elements: list):
        self._elements = list(map(float, elements))

    def __str__(self):
        return ("(" + ("{}, " * (len(self._elements) - 1)) + "{})").format(*self._elements)

    def __len__(self):
        return len(self._elements)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __neg__(self):
        return self.negate()

    def add(self, other):
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)]*len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] += other._elements[i]
        return vector(*a)

    def subtract(self, other):
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)]*len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] -= other._elements[i]
        return vector(*a)

    def multiply(self, other):
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)]*len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] *= other._elements[i]
        return vector(*a)

    def divide(self, other):
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)]*len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] /= other._elements[i]
        return vector(*a)

    def negate(self):
        a = self._elements.copy()
        for i in range(len(self)):
            a[i] = -self._elements[i]
        return vector(*a)

    def magnitude(self) -> float:
        a = self._elements.copy()
        for i in range(len(self)):
            a[i] *= self._elements[i]
        return sum(a) ** 0.5

    def normalized(self):
        return self / self.magnitude()

    @staticmethod
    def dotProduct(a, b) -> float:
        if not isinstance(a, vector) or not isinstance(b, vector):
            raise TypeError("dotProduct must be called on two objects of type vector!")
        if len(a) != len(b):
            raise ValueError("Vectors are not of equal length!")

        a, b = a._elements.copy(), b._elements
        for i in range(len(a)):
            a[i] *= b[i]
        return sum(a)

    @staticmethod
    def crossProduct(a: list, b: list) -> list:
        pass

    @staticmethod
    def distance(a, b) -> float:
        a = a - b
        a = a * a
        return sum(a._elements) ** 0.5
