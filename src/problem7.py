"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a
dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""


def prob(k, m, n):
    # calculate the inverse of
    # n with n
    # n with m/2
    # m/2 with m/2

    total = float(k + m + n)
    total_m = total - 1

    prob = (n/total * (n - 1)/total_m) + \
           (n/total * m/total_m * 1/2.0) + \
           (m/total * 1/2.0 * n/total_m) + \
           (m/total * 1/2.0 * (m - 1)/total_m * 1/2.0)

    return 1 - prob


if __name__ == '__main__':
    print prob(15, 30, 27)
