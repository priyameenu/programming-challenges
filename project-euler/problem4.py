#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

FIXME: Still WIP
"""


def filter_positive(iterable):
    return (i for i in iterable if i > 0)


def filter_palindrome(iterable):
    for number in filter_positive(iterable):
        number = str(number)
        left, right = number[:len(number)/2], number[(len(number)/2):]
        print "%s,%s" % (left, right)
        if left == right: yield number


def largest_palindrome_from_n_digit_product(n):
    try:
        multiplier = int("9"*n)
        return filter_palindrome(xrange(multiplier**2, -1, -1)).next()
    except StopIteration:
        pass


def test():
    pass


def answer():
    pass


def main():
    test()
    print answer()


if __name__ == "__main__":
    import sys
    sys.exit(main())
