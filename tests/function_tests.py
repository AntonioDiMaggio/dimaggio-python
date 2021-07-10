from dimaggio.math import vector


def main():
    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = a + b
    print(a, b, c)

    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = a - b
    print(a, b, c)

    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = a * b
    print(a, b, c)

    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = a / b
    print(a, b, c)

    a = vector(1, 2, 3).negate()
    b = vector(4, 5, 6).magnitude()
    c = vector(1, 2, 3).normalized()
    print(a, b, c)

    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = vector(1, 2, 3)
    print(vector.dotProduct(a, b))
    print(a, b, c)

    a = vector(1, 2, 3)
    b = vector(4, 5, 6)
    c = vector(1, 2, 3)
    print(vector.distance(a, b))
    print(a, b, c)


if "__main__" == __name__:
    main()
