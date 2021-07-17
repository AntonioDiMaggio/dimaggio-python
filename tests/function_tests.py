import dimath
import time


def main():
    """
    j = 100
    a = [0 for i in range(j)]
    for i in range(j):
        computeTime1 = 0.0
        computeTime2 = 0.0
        while computeTime2 <= computeTime1:
            n = dimath.randomNDigitNumber(a[i])
            n = int(str(n) + str(n)[::-1])
            t1 = time.time()
            dimath.isPalindrome(n)
            computeTime1 += time.time() - t1

            t1 = time.time()
            str(n) == str(n)[::-1]
            computeTime2 += time.time() - t1
            a[i] += 1

    print(dimath.mean(a))
    print(dimath.median(a))
    print(dimath.mode(a))
    print(a)
    print((computeTime1, computeTime2))
    """
    a = [1, 2, 2, 3, 4, 5, 6]
    b = [dimath.factorial(i) for i in range(7)]
    c = [dimath.fibonacci(i) for i in range(7)]
    vec1 = dimath.vector(*a)
    vec2 = dimath.vector(*b)
    vec3 = dimath.vector(*c)
    print(a)
    print(b)
    print(c)
    n = 100.5
    print(dimath.setRange(a))
    print(dimath.mode(a))
    print(dimath.clamp(n, 0, 100))
    print(dimath.clamp(n, 100, 101))
    print(dimath.clamp01(n))
    print(dimath.lerp(1, 3, 0))
    print(dimath.linearInterpolation(100, 525, 1))
    print(dimath.vector.lerp(vec1, vec2, 0.5))
    print(dimath.vector.mean([vec1, vec2, vec3]))
    print(dimath.vector.median([vec1, vec2, vec3]))
    print(dimath.vector.mode([vec1, vec2, vec3]))
    print(vec1.normalized())
    print(vec1)


if "__main__" == __name__:
    main()
