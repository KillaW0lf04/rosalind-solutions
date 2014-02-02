from utils import reverse_complement, gc_content, distance


def test_reverse_complement():
    assert reverse_complement('ATCG') == 'CGAT'
    assert reverse_complement('AAAA') == 'TTTT'
    assert reverse_complement('GACT') == 'AGTC'


def test_gc_content():
    assert gc_content('ACGT') == 0.5
    assert gc_content('ATAT') == 0
    assert gc_content('GCGC') == 1

    # GC Content in a sequence should be the same in its reverse complement
    s = 'ACGATACGAGCCATT'
    assert gc_content(s) == gc_content(reverse_complement(s))


def test_distance():
    assert distance('GCAT', 'GCAT') == 0
    assert distance('GCAT', 'ATGA') == 4
    assert distance('GCAT', 'GACT') == 2
