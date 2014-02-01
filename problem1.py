from collections import Counter

if __name__ == '__main__':

    with open('data/rosalind_dna.txt', mode='r') as f:
        sequence = f.read()

    counts = Counter(sequence)

    print '%d %d %d %d' % (counts['A'], counts['C'], counts['G'], counts['T'])
