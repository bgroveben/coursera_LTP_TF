def make_pairs1(list1, list2):
    """
    (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with the string from the corresponding
    position of list1 and the int from the corresponding position of list 2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs1(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    """
    pairs = []
    inner_list = []
    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

print(make_pairs1(['A', 'B', 'C'], [1, 2, 3]))



def make_pairs2(list1, list2):
    """
    (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with the string from the corresponding
    position of list1 and the int from the corresponding position of list 2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs2(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    """
    pairs = []
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

    return pairs

print(make_pairs2(['A', 'B', 'C'], [1, 2, 3]))
