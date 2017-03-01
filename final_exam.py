# Code for the final exam questions

print()

def f(x):
    y = x * 3
    return y - x

print(f(10))
print()


start = 'L'
middle = 8
end = 'R'
print(start + str(middle) + end)
print()


def larger_of_smallest(L1, L2):
    """
    (list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the smallest value in L2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    """

    return max(min(L1), min(L2))

print(larger_of_smallest([1, 4, 0], [3, 2]))
print(larger_of_smallest([4], [9, 6, 3]))
print()


def same_length(L1, L2):
    """
    (list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements
    """

    return len(L1) == len(L2)

print(same_length([1,2,3], [1,2,3]))
print(same_length([1,2,3], [1,2,]))
print()


def moogah(a, b):
    """
    (str, int) -> str
    """

def frooble(L):
    """
    (list of str) -> int
    Precondition: L has at least one element.
    """


def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
   ['a', 'c', 'e', 'g', 'i']
   '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n

    return result

print(gather_every_nth([0, 1, 2, 3, 4, 5], 3))
print(gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2))
print()


def get_keys(L, d):
    """
    (list, dict) -> list

    Return a new list containing all of the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    """
    result = []
    for k in L:
        if k in d:
            result.append(k)

    return result

print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))
print()


def are_lengths_of_strs(L1, L2):
    """
    (list of int, list of str) -> bool

    Return True if and only if all of the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    """
    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):
            result = False

    return result

print(are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef']))
print()


def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2

    return collection

L1 = [1, 2, 3]
print(double_values(L1))
d = {0: 10, 1: 20, 2: 30}
print(double_values(d))
# s = '123'
# print(double_values(s))
# t = (1, 2, 3)
# print(double_values(t))
# d2 = {1: 10, 2: 20, 3: 30}
# print(double_values(d2))
print()

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

print(get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]]))
print()


def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] = d[c] + 1


letter_counts = {'i': 0, 'r': 5, 'e': 1}
add_to_letter_counts(letter_counts, 'eerie')
print(letter_counts)
print()
