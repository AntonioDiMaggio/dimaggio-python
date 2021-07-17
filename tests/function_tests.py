import dimath
import time


def main():
    n = dimath.randomNDigitNumber(6)
    print(n)
    print(dimath.properDivisors(n))
    print(dimath.primeFactors(n))
    print(dimath.tau(n))


if "__main__" == __name__:
    main()
