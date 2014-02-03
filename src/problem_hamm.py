"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number
of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

from utils import distance


if __name__ == '__main__':

    with open('data/rosalind_hamm.txt') as f:
        s1 = f.readline()
        s2 = f.readline()

    print distance(s1, s2)
