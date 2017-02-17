def count_matches(s1, s2):
    """
    Return the nimber of positions in s1 that contain the
    same character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    """
    num_matches = 0  # accumulator
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            # num_matches = num_matches + 1  same as num_matches += 1
            num_matches += 1
    return num_matches

print(count_matches('ate', 'ape'))
print(count_matches('head', 'hard'))
print(count_matches([1,2,3],[5,2,3]))


## Corresponding Elements

# Two lists are parallel if they have the same length and the items at each index are somehow related.
# The items at the same index are said to be at corresponding positions.
