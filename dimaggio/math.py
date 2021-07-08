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
    return sum(list(range(n + 1)))


def primeFactors(n) -> []:
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
def tau(n):
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


# Vector Calculus ------------------------------------------------------------------------------------------------------
class vector(object):
    # TODO: Maybe vectors need to be of equal length.
    @staticmethod
    def add(a: list, b: list) -> list:
        if isinstance(b, int) or isinstance(b, float):
            b = [b for i in range(len(a))]
            
        for i in range(min(len(a), len(b))):
            a[i] += b[i]
        return a[:min(len(a), len(b))]

    @staticmethod
    def subtract(a: list, b: list) -> list:
        if isinstance(b, int) or isinstance(b, float):
            b = [b for i in range(len(a))]
            
        for i in range(len(b)):
            b[i] = -b[i]
        return vector.add(a, b)

    @staticmethod
    def multiply(a: list, b: list) -> list:
        if isinstance(b, int) or isinstance(b, float):
            b = [b for i in range(len(a))]
            
        for i in range(min(len(a), len(b))):
            a[i] *= b[i]
        return a[:min(len(a), len(b))]

    @staticmethod
    def divide(a: list, b: list) -> list:
        if isinstance(b, int) or isinstance(b, float):
            b = [b for i in range(len(a))]
            
        for i in range(min(len(a), len(b))):
            a[i] /= b[i]
        return a[:min(len(a), len(b))]

    @staticmethod
    def negate(a: list) -> list:
        for i in range(len(a)):
            a[i] = -a[i]
        return a

    @staticmethod
    def magnitude(a: list) -> float:
        for i in range(len(a)):
            a[i] *= a[i]
        return sum(a) ** 0.5

    @staticmethod
    def normalized(a: list) -> list:
        return vector.divide(a, vector.magnitude(a.copy()))

    @staticmethod
    def dotProduct(a: list, b: list) -> float:
        for i in range(min(len(a), len(b))):
            a[i] *= b[i]
        a = a[:min(len(a), len(b))]
        return sum(a)

    @staticmethod
    def crossProduct(a: list, b: list) -> list:
        pass

    @staticmethod
    def distance(a: list, b: list) -> float:
        a = vector.subtract(a, b)
        a = vector.multiply(a, a)
        return sum(a) ** 0.5
