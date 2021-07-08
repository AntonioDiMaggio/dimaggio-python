import dimaggio.math


def main():
    assert dimaggio.math.gcd(27, 33) == 3
    assert dimaggio.math.lcm(27, 33) == 297
    assert dimaggio.math.isCoprime(27, 33) is False
    assert dimaggio.math.gcd(3, 5) == 1
    assert dimaggio.math.lcm(3, 5) == 15
    assert dimaggio.math.isCoprime(3, 5) is True
    assert dimaggio.math.triangleNumber(7) == 28
    print(dimaggio.math.vector.add([1, 2, 3], [1, 2, 3, 4]))
    print(dimaggio.math.vector.subtract([1, 2, 3], [1, 2, 3, 4]))
    print(dimaggio.math.vector.multiply([1, 2, 3], [1, 2, 3, 4]))
    print(dimaggio.math.vector.divide([1, 2, 3], [1, 2, 3, 4]))
    print(dimaggio.math.vector.negate([1, 2, 3]))
    print(dimaggio.math.vector.magnitude([32, 57, 23]))
    print(dimaggio.math.vector.normalized([1, 2, 3]))
    print(dimaggio.math.vector.magnitude(dimaggio.math.vector.normalized([1, 2, 3])))
    print(dimaggio.math.vector.dotProduct([32, 57, 23], [1, 2, 3, 4]))
    print(dimaggio.math.vector.distance([32, 57, 23], [1, 2, 3]))


if "__main__" == __name__:
    main()
