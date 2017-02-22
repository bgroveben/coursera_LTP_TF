def shift_left(L):
    """
    (list) -> list

    Shift each item in list L one position to the left and
    shift the first item to the last position.

    Precondition: len(L) > 1

    >>> print(shift_left([1, 2, 3]))
    [2, 3, 1]
    """
    first_item = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]
    L[-1] = first_item
    return L

my_list = [1,2,3]
print(shift_left(my_list))


def shift_right(L):
    """
    (list) -> list

    Shift each item in list L one position to the right and
    shift the last item to the first position.

    Precondition: len(L) > 1

    >>> print(shift_right([1, 2, 3]))
    [3, 1, 2]
    """
    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    L[0] = last_item
    return L

my_list = [1,2,3]
print(shift_right(my_list))
