import dimath
import time


def main():
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


if "__main__" == __name__:
    main()
