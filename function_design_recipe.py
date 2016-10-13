# The function design recipe has six steps.

"""
1. Examples
    -- What should your function do?
    -- Type a couple of example function calls.
    -- Pick a name for the function; basically a short answer to "What does your function do?"

2. Type Contract
    -- What are the parameter types?
    -- What type of value is returned?

3. Header
    -- Pick meaningful parameter names.

4. Description
    -- Mention every parameter in your description.
    -- Describe the return value.

5. Body
    -- The body of the function is the part that transforms input into (desired) output.

6. Test
    -- Run the examples.
"""

# Walk-through of an example program that converts degrees Fahrenheit to degrees Celsius.

"""
1. Examples
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0

2. Type Contract
    (number) -> number

3. Header
    def convert_to_celsius(fahrenheit):

4. Description
    Return the number of celsius degrees equivalent to fahrenheit degrees.

5. Body
    return (fahrenheit - 32) * 5/9

6. Test
    print(convert_to_celsius(32))
    print(convert_to_celsius(212))
"""

# Now to put it all together into a working example:

def convert_to_celsius(fahrenheit):
    """ (number) -> float

    Return the number of celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0

    """
    return (fahrenheit - 32) * 5/9  ## You can change 5/9 to 5//9 (floor division) if you want the result to be an integer.


print(convert_to_celsius(32))
print(convert_to_celsius(212))
