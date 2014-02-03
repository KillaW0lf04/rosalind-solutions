"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing
all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

if __name__ == '__main__':

    with open('data/rosalind_rna.txt', 'r') as f:
        sequence = f.read()

    print sequence.replace('T', 'U')