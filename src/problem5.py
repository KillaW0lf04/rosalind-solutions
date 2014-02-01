"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has
the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling
is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by
some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates
the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where
"xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind
allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on
absolute error below.
"""

from collections import Counter


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

if __name__ == '__main__':
    sequences = read_fasta('data/rosalind_gc.txt')

    max_gc = 0
    max_id = None

    for id, s in sequences.items():
        gc = gc_content(s)

        if gc > max_gc:
            max_gc = gc
            max_id = id

    print max_id
    print max_gc * 100