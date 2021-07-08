import dimaggio.math


def main():
    a, b = 27, 33
    print(dimaggio.math.gcd(a, b))
    print(dimaggio.math.lcm(a, b))
    print(dimaggio.math.isCoprime(a, b))


if "__main__" == __name__:
    main()
