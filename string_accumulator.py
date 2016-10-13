# In the following function, the variable vowels is an accumulator.

def collect_vowels(s):
    """ (str) -> str

    Return the vowels from s. Do not treat the letter y as a vowel.

    >>>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>>> collect_vowels('xyz')
    ''
    """

    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels


print("The string 'Happy Anniversary!' contains the vowels " + collect_vowels('Happy Anniversary!') + ".")
print("The string 'xyz' contains no vowels" + collect_vowels('xyz') + ".")
