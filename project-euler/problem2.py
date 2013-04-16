#!/usr/bin/env python

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fib():
    a,b = 1,2
    while True:
        yield a
        a,b = b, a+b


def fib_at_most(max):
    generator = fib()
    while True:
        yield generator.next()
        b = generator.next()
        if b > max: return
        yield b


def filter_even(iterable):
    return (i for i in iterable if (i % 2 == 0))


def test():
    answer = sum(filter_even(fib_at_most(4)))
    assert(answer is 2)


def answer():
    return sum(filter_even(fib_at_most(4000000)))


def main():
    test()
    print answer()


if __name__ == "__main__":
    import sys
    sys.exit(main())
