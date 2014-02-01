from collections import Counter


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