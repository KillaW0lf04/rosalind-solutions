from collections import Counter


GENETIC_CODE = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': None,     'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': None,     'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': None,     'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}


def nt2aa(s):
    aa_sequence = ''

    for i in xrange(len(s)/3):
        codon = s[i * 3: (i + 1) * 3]
        value = GENETIC_CODE[codon]

        if not value:
            return aa_sequence
        else:
            aa_sequence += value


def distance(s1, s2):
    return sum([1 for c1, c2 in zip(s1, s2) if c1 != c2])


def gc_content(sequence):
    count = Counter(sequence)

    return (count['G'] + count['C']) / float(len(sequence))


def read_fasta(path):

    sequences = {}

    current_id = None
    current_seq = None

    with open(path) as f:

        data = f.readline()
        while data:

            if data.startswith('>'):
                if current_id:
                    sequences[current_id] = current_seq

                current_id = data[1:].rstrip()
                current_seq = ''
            else:
                current_seq += data.rstrip()

            data = f.readline()

    # Add any left over sequence data
    if current_id:
        sequences[current_id] = current_seq

    return sequences


def reverse_complement(s):

    inverse = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
        '\n': '',
    }

    complement = ''
    for N in s:
        complement = inverse[N] + complement

    return complement