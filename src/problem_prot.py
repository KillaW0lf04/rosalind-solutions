"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all
letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Hencefort'H',
the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

from utils import nt2aa


if __name__ == '__main__':

    with open('data/rosalind_prot.txt') as f:
        sequence = f.read()

    print nt2aa(sequence)
