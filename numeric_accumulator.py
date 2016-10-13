# In the following function, the variable num_vowels is an accumulator.

def count_vowels(s):
    """ (str) -> int

    Return the number of vowels in s. Do not treat the letter y as a vowel.

    >>>> count_vowels('Happy Anniversary!')
    5
    >>>> count_vowels('xyz')
    0
    """

    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels


print("'Happy Anniversary!' has " + str(count_vowels('Happy Anniversary!')) + " vowels.")
print("'xyz' has " + str(count_vowels('xyz')) + " vowels.")
