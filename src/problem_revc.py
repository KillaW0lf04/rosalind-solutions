"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then
taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

from utils import reverse_complement


if __name__ == '__main__':

    with open('data/rosalind_revc.txt') as f:
        sequence = f.read()

    print reverse_complement(sequence)