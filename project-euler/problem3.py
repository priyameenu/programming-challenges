#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

`factorize` function derived from:
http://glowingpython.blogspot.ca/2011/07/prime-factor-decomposition-of-number.html
"""

from itertools import chain


def factorize(number):
    if number < 2: return

    for i in chain([2], xrange(3, number+1, 2)):
        s = 0

        while (number % i) is 0:
            number /= i
            s += 1
            yield i * s
            if number is 1: return


def filter_primes(iterable):
    for i in iterable:
        factors = factorize(i)
        num = factors.next()
        try:
            factors.next()
            return
        except StopIteration:
            if num != i: return
            yield i


def largest_prime_factor(number):
    factors = reversed(list(factorize(number)))
    try:
        return filter_primes(factors).next()
    except StopIteration:
        return None


def test():
    assert(largest_prime_factor(13195) is 29)


def answer():
    return largest_prime_factor(600851475143)


def main():
    test()
    print answer()


if __name__ == "__main__":
    import sys
    sys.exit(main())
