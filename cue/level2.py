#!/usr/bin/env python

"""
The Cue Programming Challenge
Level 2

`factorize` function derived from:
http://glowingpython.blogspot.ca/2011/07/prime-factor-decomposition-of-number.html
"""

from itertools import chain


def fibonacci(curr=1, next=2):
    while True:
        yield curr
        curr, next = next, curr+next

def factorize(number):
    if number < 2: return

    for i in chain([2], xrange(3, number+1, 2)):
        s = 0

        while (number % i) is 0:
            number /= i
            s += 1
            yield i * s
            if number is 1: return


def primes(iterable):
    for i in iterable:
        factors = factorize(i)
        num = factors.next()
        try:
            factors.next()
        except StopIteration:
            if num != i: return
            yield i


def first_larger_fibonacci_prime(number):
    fib_buffer = lambda fib: [fib.next(), fib.next()]

    fib = fibonacci()
    curr, next = fib_buffer(fib)
    while next < number:
        curr, next = fib_buffer(fib)

    return primes(fibonacci(curr,next)).next()


def test():
    assert(list(primes([3,4,5,6])) == [3,5])
    assert(list(factorize(4)) == [2, 4])
    assert(list(primes(factorize(12))) == [2, 3])
    assert(first_larger_fibonacci_prime(10) is 13)


def main():
    test()
    part1_answer = first_larger_fibonacci_prime(217000)
    part2_answer = sum(primes(factorize(part1_answer+1)))
    print "Part1: %d" % part1_answer
    print "Part2: %d" % part2_answer


if __name__ == "__main__":
    import sys
    sys.exit(main())
