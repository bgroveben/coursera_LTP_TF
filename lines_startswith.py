def lines_startswith1(file, letter):
    """
    (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have the new line removed.

    Precondition: len(letter) == 1

    >>> cat_file = open('cat.txt', 'r')
    >>> print(lines_startswith1(cat_file, 't'))
    ['the']
    """
    matches = []

    for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    return matches

cat_file = open('cat.txt', 'r')
print(lines_startswith1(cat_file, 't'))
print(lines_startswith1(cat_file, 'b'))


def lines_startswith2(file, letter):
    """
    (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have the new line removed.

    Precondition: len(letter) == 1

    >>> cat_file = open('cat.txt', 'r')
    >>> print(lines_startswith2(cat_file, 't'))
    ['the']
    """
    matches = []

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

    return matches

cat_file = open('cat.txt', 'r')
print(lines_startswith2(cat_file, 't'))
print(lines_startswith2(cat_file, 'b'))
