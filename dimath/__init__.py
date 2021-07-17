"""
This package provides access to many math functions and constants from many areas of mathematics.\n

Functions:\n

gcd -> Greatest Common Divisor.\n
lcm -> Least Common Multiple.\n
isCoprime -> Determines if two numbers are co-prime.\n
triangelNumber -> Find nth triangle number.\n
primeFactors -> Finds the prime factors of a integer.\n
tau -> Finds the number of divisors of an integer.\n
properDivisors -> Finds the proper divisors of an integer.\n
isAmicablePair -> Determines if a pair of integers are amicable.\n
fibonacci -> Finds the nth fibonacci number.\n
factorial -> Finds the factorial of n.\n
isPalindrome -> Determines if a number (or string) is a palindrome.\n
randomNDigitNumber -> Generates a random number with n digits.\n
mean / average / avg -> Finds the average of a list.\n
median -> Finds the median of a list.\n
mode -> Finds the mode of a list.\n
setRange -> Finds the range of a list.\n
clamp -> Clamps a number between two values.\n
clamp01 -> Clamps a number between 0 and 1.\n
lerp / linearInterpolation -> Linearly interpolates between two numbers, given a percentage.\n
"""

__version__ = "0.0.0.7"
__author__ = "Antonio DiMaggio"

import random


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
    """

    :param n:
    :return int:
    """
    return n * (n + 1) // 2


def primeFactors(n: int) -> list:
    """

    :param n:
    :return:
    """
    a = []
    left, right = 2, n
    rightSquare = int(n ** 0.5) + 1
    while left < rightSquare:
        checkedAll = True
        for i in range(left, rightSquare):
            if right % i == 0:
                left = i
                a.append(left)
                right //= left
                rightSquare = int(right ** 0.5) + 1
                checkedAll = False
                break
        if checkedAll:
            break

    a.append(right)
    return a


# Number of divisors of an integer.
def tau(n: int):
    """

    :param n:
    :return:
    """
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
    """

    :param n:
    :return:
    """
    a = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            a.append(i)
    return a


def isAmicablePair(a: int, b: int) -> bool:
    """

    :param a:
    :param b:
    :return:
    """
    return a != b and sum(properDivisors(a)) == b and sum(properDivisors(b)) == a


def fibonacci(n: int) -> int:
    """

    :param n:
    :return:
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def factorial(n: int) -> int:
    """

    :param n:
    :return:
    """
    if 0 == n:
        return 1
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def isPalindrome(a) -> bool:
    """

    :param a:
    :return:
    """
    a = str(a)
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True


def randomNDigitNumber(n: int) -> int:
    """

    :param n:
    :return:
    """
    if n <= 0:
        return 0
    return int("".join([random.choice(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")) for i in range(n)]))


def mean(a: list) -> float:
    """

    :param a:
    :return:
    """
    return sum(a) / len(a)


def average(a: list) -> float:
    """

    :param a:
    :return:
    """
    return mean(a)


def avg(a: list) -> float:
    """

    :param a:
    :return:
    """
    return mean(a)


def median(a: list) -> float:
    """

    :param a:
    :return:
    """
    a = sorted(a)
    if len(a) % 2 == 0:
        return (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2
    return a[len(a) // 2]


def mode(a: list) -> float:
    """

    :param a:
    :return:
    """
    b = {}
    for i in range(len(a)):
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 0

    m = a[0]
    count = 0
    for i in b.keys():
        if count < b[i]:
            m = i
            count = b[i]
    return m


def setRange(a: list) -> float:
    """

    :param a:
    :return:
    """
    return max(a) - min(a)


def clamp(n: float, minimum: float, maximum: float) -> float:
    """

    :param n:
    :param minimum:
    :param maximum:
    :return:
    """
    if maximum < n:
        return maximum
    elif n < minimum:
        return minimum
    else:
        return n


def clamp01(n: float) -> float:
    """

    :param n:
    :return:
    """
    return clamp(n, 0, 1)


def lerp(a: float, b: float, p: float) -> float:
    """

    :param a:
    :param b:
    :param p:
    :return:
    """
    p = clamp01(p)
    return a + (b - a) * p


def linearInterpolation(a: float, b: float, p: float) -> float:
    """

    :param a:
    :param b:
    :param p:
    :return:
    """
    return lerp(a, b, p)


# Vector Calculus ------------------------------------------------------------------------------------------------------
class vector(object):
    """

    """
    def __init__(self, *elements: list):
        """

        :param elements:
        """
        self._elements = list(map(float, elements))

    def __str__(self):
        """

        :return:
        """
        return ("(" + ("{}, " * (len(self._elements) - 1)) + "{})").format(*self._elements)

    def __len__(self):
        """

        :return:
        """
        return len(self._elements)

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        return self.add(other)

    def __sub__(self, other):
        """

        :param other:
        :return:
        """
        return self.subtract(other)

    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        return self.multiply(other)

    def __truediv__(self, other):
        """

        :param other:
        :return:
        """
        return self.divide(other)

    def __neg__(self):
        """

        :return:
        """
        return self.negate()

    def add(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)] * len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] += other._elements[i]
        return vector(*a)

    def subtract(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)] * len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] -= other._elements[i]
        return vector(*a)

    def multiply(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)] * len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] *= other._elements[i]
        return vector(*a)

    def divide(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other, vector) and float(other):
            other = vector(*[float(other)] * len(self))
        if len(self) != len(other):
            raise ValueError("Vectors are not of equal length!")

        a = self._elements.copy()
        for i in range(len(self)):
            a[i] /= other._elements[i]
        return vector(*a)

    def negate(self):
        """

        :return:
        """
        a = self._elements.copy()
        for i in range(len(self)):
            a[i] = -self._elements[i]
        return vector(*a)

    def magnitude(self) -> float:
        """

        :return:
        """
        a = self._elements.copy()
        for i in range(len(self)):
            a[i] *= self._elements[i]
        return sum(a) ** 0.5

    def normalized(self):
        """

        :return:
        """
        return self / self.magnitude()

    @staticmethod
    def dotProduct(a, b) -> float:
        """

        :param a:
        :param b:
        :return:
        """
        if not isinstance(a, vector) or not isinstance(b, vector):
            raise TypeError("dotProduct must be called on two objects of type vector!")
        if len(a) != len(b):
            raise ValueError("Vectors are not of equal length!")

        a, b = a._elements.copy(), b._elements
        for i in range(len(a)):
            a[i] *= b[i]
        return sum(a)

    @staticmethod
    def crossProduct(a: list, b: list):
        """

        :param a:
        :param b:
        :return:
        """
        pass

    @staticmethod
    def distance(a, b) -> float:
        """

        :param a:
        :param b:
        :return:
        """
        a = a - b
        a = a * a
        return sum(a._elements) ** 0.5

    @staticmethod
    def lerp(a, b, p):
        """

        :param a:
        :param b:
        :param p:
        :return:
        """
        if not isinstance(a, vector) or not isinstance(b, vector):
            raise TypeError(f"Cannot linearly interpolate between objects of type: '{type(a).__name__}' and"
                            f"'{type(b).__name__}'.")
        if len(a) != len(b):
            raise ValueError("Vectors are not of equal length!")

        v = []
        for i in range(len(a)):
            v.append(lerp(a._elements[i], b._elements[i], p))

        return vector(*v)

    @staticmethod
    def linearInterpolation(a, b, p):
        """

        :param a:
        :param b:
        :param p:
        :return:
        """
        return vector.lerp(a, b, p)

    @staticmethod
    def mean(a):
        """

        :param a:
        :return:
        """
        # First get transpose of elements
        b = [[row._elements[i] for row in a] for i in range(len(a[0]))]

        # Then get the mean of vector elements.
        v = []
        for i in b:
            v.append(mean(i))

        return vector(*v)

    @staticmethod
    def average(a):
        """

        :param a:
        :return:
        """
        return vector.mean(a)

    @staticmethod
    def avg(a):
        """

        :param a:
        :return:
        """
        return vector.mean(a)

    @staticmethod
    def median(a):
        """

        :param a:
        :return:
        """
        # First get transpose of elements
        b = [[row._elements[i] for row in a] for i in range(len(a[0]))]

        # Then get the mean of vector elements.
        v = []
        for i in b:
            v.append(median(i))

        return vector(*v)

    @staticmethod
    def mode(a):
        """

        :param a:
        :return:
        """
        # First get transpose of elements
        b = [[row._elements[i] for row in a] for i in range(len(a[0]))]

        # Then get the mean of vector elements.
        v = []
        for i in b:
            v.append(mode(i))

        return vector(*v)
