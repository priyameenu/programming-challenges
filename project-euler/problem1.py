#!/usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_below(base, maximum):
    remainder = (maximum % base)
    highest_multiple = (maximum - remainder) / base

    if not (remainder is 0):
        highest_multiple = highest_multiple + 1

    return (base * i for i in xrange(1, highest_multiple))


def test():
    answer = sum(set(multiples_below(3, 10)).union(set(multiples_below(5, 10))))
    assert(answer is 23)


def answer():
    return sum(
        set(multiples_below(3, 1000)).union(
        set(multiples_below(5, 1000)))
    )


def main():
    test()
    print answer()


if __name__ == "__main__":
    import sys
    sys.exit(main())
