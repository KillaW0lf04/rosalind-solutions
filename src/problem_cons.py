"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""

from utils import read_fasta, generate_profile, generate_consensus, PROFILE_INDEX

if __name__ == '__main__':

    data = read_fasta('data/rosalind_cons.txt')

    profile = generate_profile(data)

    print generate_consensus(profile)

    # Print out the profile index
    for key in ['A', 'C', 'G', 'T']:
        print '%s: %s' % (key, ' '.join('%d' % s for s in profile[PROFILE_INDEX[key]]))
