"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""


def occurrences(s, t):
    if len(t) > len(s):
        return None

    results = []

    for i, _ in enumerate(s):
        if s[i:i + len(t)] == t:
            results.append(i + 1)

    return results


if __name__ == '__main__':

    with open('data/rosalind_subs.txt') as f:
        s = f.readline().rstrip()
        t = f.readline().rstrip()

    print ' '.join("%s" % s for s in occurrences(s, t))