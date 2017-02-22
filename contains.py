def contains1(value, lst):
    """
    (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains1('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """
    # intialize found value to False, change it to True if we find the value in the list of lists.
    found = False
    for sublist in lst:
        if value in sublist:
            found = True

    return found

print(contains1('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))


def contains2(value, lst):
    """
    (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains2('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """
    # intialize found value to False, change it to True if we find the value in the list of lists.
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True

    return found

print(contains2('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))
