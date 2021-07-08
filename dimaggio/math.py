def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def isCoprime(a: int, b: int) -> bool:
    return 1 == gcd(a, b)
