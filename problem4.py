"""
Given: Positive integers n>=40 and k<=5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in
each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs
(instead of only 1 pair).
"""


# Based off a fibonnaci sequence with rabbits from 2 months ago producing k rabbits
def rabbits(n, k, _cache={1: 1, 2: 1}):
    if n not in _cache:
        _cache[n] = rabbits(n - 1, k) + rabbits(n - 2, k) * k

    return _cache[n]


if __name__ == '__main__':
    print rabbits(29, 5)