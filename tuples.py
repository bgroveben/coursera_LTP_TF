### TUPLES ###

# Tuples are immutable sequences, meaning that they cannot be modified.
# Other than the immutabily thing, tuples behave in pretty much the same way as lists.
# In your interpreter/shell/IDLE/REPL thingy, enter the commands:
# => dir(tuple)
# => dir(list)
# and compare the methods listed at the end (hint: tuples have only two, lists have 9).

# Tuples use parentheses instead of square brackets:
example_list  = ['a', 3, -0.2]
example_tuple = ('a', 3, -0.2)

# Once created, items in lists and tuples are accessed using the same notation:
print()
print(example_list[0])
print(example_tuple[0])
print()

# Slicing can be used with both lists and tuples:
print(example_list[:2])
print(example_tuple[:2])
print()

# I know you want to, so go ahead and try to modify a tuple:
# => example_tuple[0] = 'b'
# >>> TypeError: 'tuple' object does not support item assignment

# A for loop can be used to iterate over the values in a tuple:
for item in example_tuple:
    print(item)
print()

# A tuple can be passed as an argument to the built-in function len():
print(len(example_tuple))
print()

# It is also possible to iterate over the indices of a tuple:
for i in range(len(example_tuple)):
    print(example_tuple[i])
print()
