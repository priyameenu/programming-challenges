#!/usr/bin/env python

"""
The Cue Programming Challenge
Level 3

Assuming no 0's or negative numbers in input
"""

from itertools import chain, combinations


def power_set(S):
    return chain.from_iterable(combinations(S, s) for s in range(len(S) + 1))


def is_subset_sum(S):
    if len(S) < 3: return False
    S = list(S)
    S.sort()
    return sum(S[:-1]) == S[-1]


def subsets_where_largest_number_is_sum_of_rest(S):
    return filter(is_subset_sum, power_set(S))


def test():
    assert(is_subset_sum(set([3,1,2])))
    assert(is_subset_sum(set([1,2,3,6])))
    assert(not is_subset_sum(set([1,2,6])))

    assert(len(subsets_where_largest_number_is_sum_of_rest(set([1,2,3,4,6]))) == 4)

    assert(set(power_set([1,2,3])) == set([(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)]))


def answer(numbers):
    return len(subsets_where_largest_number_is_sum_of_rest(numbers))


def main():
    test()
    numbers = '3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99'
    print answer(set(map(int,numbers.split(', '))))


if __name__ == "__main__":
    import sys
    sys.exit(main())
