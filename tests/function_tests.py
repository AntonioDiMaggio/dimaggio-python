import dimaggio.math


def main():
    assert dimaggio.math.gcd(27, 33) == 3
    assert dimaggio.math.lcm(27, 33) == 297
    assert dimaggio.math.isCoprime(27, 33) is False
    assert dimaggio.math.gcd(3, 5) == 1
    assert dimaggio.math.lcm(3, 5) == 15
    assert dimaggio.math.isCoprime(3, 5) is True


if "__main__" == __name__:
    main()
