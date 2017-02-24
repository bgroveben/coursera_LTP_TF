### Type dict ###
# Dictionary

# The general form of a dictionary is:
# {key1: value1, key2: value2, ..., keyN: valueN}

# Keys must be unique, values may be duplicated:
grades_dict = {'A1': 80, 'A2': 90, 'A3': 90}
print()
print(grades_dict)
print()
# In the example above, the keys 'A1', 'A2', 'A3' are unique.
# The values 80, 90, 90 are not unique.

### How To Modify Dictionaries ###
# Dictionaries are mutable, meaning that they can be modified.
# There are a series of operations and methods you can apply to dicitionaries which are outlined below.

# object in dict:  Checks whether object is a key in dict.
print('A1' in grades_dict)
print(80 in grades_dict)
print()

# len(dict):  Returns the number of keys in dict.
print(len(grades_dict))
print()

# del dict[key]:  Removes a key and its associated value from dict.
grades_dict = {'A1': 80, 'A2': 70, 'A3': 90}
del grades_dict['A1']
print(grades_dict)
print()

# dict[key] = value:  If key does not exist in dict, adds key and its associated value to dict.
#                     If key exists in dict, updates dict by setting the value associated with key to value.
grades_dict = {'A1': 80, 'A2': 70, 'A3': 90}
grades_dict['A4'] = 70
print(grades_dict)
print()


### Accessing Inforamtion From Dictionaries ###
# Dictionaries are unordered.
# The order that the key-value pairs are added to the dictionary has no effect on the order in which they are accessed.
grades_dict = {'A1': 80, 'A2': 70, 'A3': 90}
for grade in grades_dict:
    print(grade)
print()

# The for-loop above printed out the keys of the dictionary.
# It is also possible to print out the values.
for grade in grades_dict:
    print(grades_dict[grade])
print()

# Finally, both the keys and the values can be printed.
for grade in grades_dict:
    print(grade, grades_dict[grade])
print()


## Empty dictionaries:
empty_dict = {}
print(empty_dict)
print()

## Heterogeneous dictionaries:
# A dictionary can have keys of different types.
# For example, one key canbe of type int and another of type str:
heterogeneous_dict = {'apple': 1, 3: 4}
print(heterogeneous_dict)
print()

## Immutable Keys
# The keys of a dictionary must be immutable.
# Lists, dicts, and other mutable types cannot be used as keys.

# => heterogeneous_dict[[1, 2]] = 'banana'
# >>> TypeError: unhashable type: 'list'

# If you want to use a sequence as a key, use a tuple instead:
heterogeneous_dict[(1, 2)] = 'banana'
print(heterogeneous_dict)
print()
