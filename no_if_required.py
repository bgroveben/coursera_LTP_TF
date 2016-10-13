# Booleans are your friend.
# Why do this:

def is_even(num):
    """ (int) -> bool
    Return whether number is even.
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(1))
print(is_even(2))


# When you can do this:

def is_even_bool(num):
    """ (int) -> bool
    Return whether number is even.
    >>> is_even_bool(1)
    False
    >>> is_even_bool(2)
    True
    """
    return num % 2 == 0

print(is_even_bool(1))
print(is_even_bool(2))
