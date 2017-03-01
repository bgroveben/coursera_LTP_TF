d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}

total = 0
for k in d:
    total = total + k

print(total)


L = []
for k in d:
    L.append(k)

total2 = len(L)
print(total2)


L2 = []
for k in d:
    L2.extend(d[k])

total3 = len(L2)
print(total3)


total4 = 0
for k in d:
    total4 = total4 + len(d[k])

print(total4)
print()

L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
    d[item[0]] = item[1]

print(d)
print(L)
print()

def eat(d):
    """
    (dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    ENTER MISSING DESCRIPTION HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True

    >>> eat({'apple': 0, 'banana': 0})
    False
    """
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

print(eat({'apple': 0, 'banana': 1, 'pear': 0, 'peach': 0}))
print(eat({'apple': 0, 'banana': 1}))
print()


def contains(v, d):
    """
    (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.

    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    """

    found = False  # whether we have found v in a list inside d

#   for k in d:
#       if v in d[k]:
#           found = True

    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True

    return found

print(contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}))
print(contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))
print()
