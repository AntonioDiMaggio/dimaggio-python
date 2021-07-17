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
dimath.**gcd**(a, b)\
dimath.**lcm**(a, b)\
dimath.**isCoprime**(a, b)\
dimath.**triangleNumber**(n)\
dimath.**primeFactors**(n)\
dimath.**tau**(n)\
dimath.**properDivisors**(n)\
dimath.**isAmicablePair**(a, b)\
dimath.**fibonacci**(n)\
dimath.**factorial**(n)\
dimath.**isPalindrome**(a)\
dimath.**randomNDigitNumber**(n)\
dimath.**mean**(a) / dimath.**average**(a) / dimath.**avg**(a)\
dimath.**median**(a)\
dimath.**mode**(a)\
dimath.**setRange**(a)\
dimath.**clamp**(n, minimum, maximum)\
dimath.**clamp01**(n)\
dimath.**lerp**(a, b, p) / dimath.**linearInterpolation**(a, b, p)

## Classes
### Vector
#### Methods
dimath.**_vector_**.**add**(_self, other_)\
dimath.**_vector_**.**subtract**(_self, other_)\
dimath.**_vector_**.**multiply**(_self, other_)\
dimath.**_vector_**.**divide**(_self, other_)\
dimath.**_vector_**.**negate**(_self_)\
dimath.**_vector_**.**magnitude**(_self_)\
dimath.**_vector_**.**normalized**(_self_)

#### Static Methods
dimath.**_vector_**.**dotProduct**(_a, b_)\
dimath.**_vector_**.**distance**(_a, b_)\
dimath.**_vector_**.**lerp**(_a, b, p_) / dimath.**linearInterpolation**(_a, b, p_)\
dimath.**_vector_**.**mean**(_a_) / dimath.**average**(_a_) / dimath.**avg**(_a_)\
dimath.**_vector_**.**median**(_a_)\
dimath.**_vector_**.**mode**(_a_)