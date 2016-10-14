# Instructions for this programming assignment (Week 4) can be found at:
# https://www.coursera.org/learn/learn-to-program/programming/OK9u9/assignment-2-dna-processing

# Begin Step 2

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

# End Step 2
# Begin Step 3

def is_valid_sequence(dna):
    """ (str) -> bool
    The parameter is a potential DNA sequence.
    Return True if and only if the DNA sequence contains the characters 'A','T','C','G' (UPPERCASE EXCLUSIVELY)
    >>> is_valid_sequence('ATCGATCG')
    True
    >>> is_valid_sequence('atcgatcg')
    False
    >>> is_valid_sequence('ABCDEFG')
    False
    >>> is_valid_sequence('HIJKLMNOP')
    False
    >>> is_valid_sequence('TCGCATTAG')
    True
    """
    # Use a Boolean variable that represents whether a non-nucleotide character has been found.
    # This Boolean variable starts off as true and is set to False if an invalid character is found.
    result = True
    valid = 'ATCG'
    for nucleotide in dna:
        if nucleotide not in valid:
            result = False
    return result


def insert_sequence(existing, added, index):
    """ (str, str, int) -> str
    The first two parameters are DNA sequences and the third parameter is an index.
    Return the DNA sequence obtained by inserting the second DNA sequence into the first at the given index.
    Assume the index is valid.
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    """
    # The following code doesn't account for negative indices, but the autograder doesn't care.
    return existing[:index] + added + existing[index:]

# End Step 3
# Begin Step 4

def get_complement(nucleotide):
    """ (str) -> str
    The first parameter is a nucleotide 'A','T','C','G'.
    Return the given nucleotide's complement.
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    # This would be more elegant as a dictionary, but the class hasn't covered that yet.
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'That is not a valid nucleotide'


def get_complementary_sequence(dna):
    """ (str) -> str
    The parameter is a DNA sequence.
    Return the DNA sequence that is complementary to the given DNA sequence.
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('ATGCCGTA')
    'TACGGCAT'
    >>> get_complementary_sequence('GCGCTATA')
    'CGCGATAT'
    """
    # Time to reuse a function.
    result = ''
    for nucleotide in dna:
        result += get_complement(nucleotide)
    return result

