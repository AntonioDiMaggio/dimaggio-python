import dimath
import time


def main():
    n = 1241565235040102350236121
    t1 = time.time()
    print(dimath.primeFactors(n))
    print(time.time() - t1)


if "__main__" == __name__:
    main()
