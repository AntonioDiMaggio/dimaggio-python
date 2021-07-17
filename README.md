# DiMath (Python)
> Updated: 7/10/2021

![Repository Workflow Status](https://github.com/AntonioDiMaggio/dimaggio-python/actions/workflows/python-package.yml/badge.svg)

## Description
The DiMath API is a collection of math functions and classes that I have found useful during my software engineering endeavors.

## Example
```python
import dimath

def main():
    # dimath implements a large variety of math functions. Here we can use dimath to
    # populate a list with the first 8 values of the Fibonacci sequence.
    fib = [dimath.fibonacci(i) for i in range(8)]
    
    # We can then use the list to construct an 8-dimensional vector.
    vec1 = dimath.vector(*fib)
    print(vec1)
    
    # We can also construct a vector by providing an arbitrary number of parameters.
    vec2 = dimath.vector(1, 2, 3, 4, 5, 6, 7, 8)
    print(vec2)
    
    # Note, any value that can be cast to a float can be passed to the vector
    # constructor without problem.
    vec3 = dimath.vector(1, 2.0, "3", True)
    print(vec3)

    # And of course we can perform common vector functions.
    print(dimath.vector.distance(vec1, vec2))
    print(dimath.vector.dotProduct(vec1, vec2))
    print(vec3.normalized().magnitude())


if "__main__" == __name__:
    main()
```
**OUTPUT:**
```
(0.0, 1.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0)
(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
(1.0, 2.0, 3.0, 1.0)
6.4031242374328485
218.0
1.0
```

## Functions
* gcd
* lcm
* isCoprime
* triangleNumber
* primeFactors
* tau
* properDivisors
* isAmicablePair
* fibonacci
* factorial
* isPalindrome
* randomNDigitNumber
* mean / average / avg
* median
* mode
* setRange
* clamp
* clamp01
* lerp / linearInterpolation

## Classes
### Vector
#### Methods
* add
* subtract
* multiply
* divide
* negate
* magnitude
* normalized

#### Static Methods
* dotProduct
* distance
* lerp / linearInterpolation
* mean / average / avg
* median
* mode