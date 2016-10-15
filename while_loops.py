def get_answer(prompt):
    """ (str) -> str
    Use the prompt to ask the user for a 'yes' or 'no' answer.
    Continue asking until the user gives a valid response.
    Return the answer.
    """
    answer = input(prompt)
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)
    return answer


def up_to_vowel(s):
    """ (str) -> str
    Return a substring of s from index 0 up to but not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    """
    # before_vowel contains all of the characters found in s[0:i].
    before_vowel = ''
    i = 0
    # Accumulate the non-vowels at the beginning of the string.
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1
    return before_vowel


def last_vowel(s):
    """ (str) -> str
    Return the last vowel in s if one exists.
    Otherwise, return None.

    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None

    """
    i = len(s) - 1
    # The first time through the loop, s[i] is examined -- if i is len(s), then it is an invalid index.
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i = i - 1  # Don't forget to decrement i, lest you throw an infinite loop.
    return None


## Loops Conditions and Lazy Evaluation
# The Problem: Print the characters of string s, up to the first vowel in s.
"""
The following attempt works when s contains one or more vowels, but throws an error when no vowels are in s.

i = 0
s = 'xyz'
while not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1

Will throw an index error when executed.
"""
# In the code above, the error occurs when s is indexed at i and i is outside the range of valid indices.
"""
To prevent this error, an additional condition is added to ensure that i is within the range of valid indices for s.

i = 0
s = 'xyz'
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1

Will not throw an error.
"""
# Because Python evaluates the and using lazy evaluation, if the first operand is False, then the expression
# evaluates to False and the second operand is not evaluated. That prevent the IndexError.
