### Inverting a Dictionary ###

## Switching Keys and Values ##

# Dictionaries have keys that are unique and each key has a value associated with it.
# Here is a dict mapping fruit to their colors:
fruit_to_color = {'watermelon': 'green', 'pomegranate': 'red', 'peach': 'orange', 'cherry': 'red',
                  'pear': 'green', 'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}
print()
print(fruit_to_color)
print()

# To invert the dictionary, or to switch the mapping to be colors to fruit, here is one approach:
color_to_fruit1 = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    color_to_fruit1[color] = fruit

print(color_to_fruit1)
print()

# The resulting dictionary is missing some fruit.
# This has happened because colors, which are keys, are unique.
# When assignments happen later that use the same color, the earlier entries are replaced.
# One way to fix this is to map colors to a list of fruit.

## Mapping A Key To A List ##
# For the example above, we need to consider two cases when adding a color and a fruit to the dictionary.
# 1. If the color is not a key in the dictionary, add it with its value being
#    a single element in a list consisting of the fruit.
# 2. If the color is already a key, append the fruit to the list of fruit associated with that key.
color_to_fruit2 = {}
for fruit in fruit_to_color:
    # What color is the fruit?
    color = fruit_to_color[fruit]
    if not (color in color_to_fruit2):
        color_to_fruit2[color] = [fruit]
    else:
        color_to_fruit2[color].append(fruit)

print(color_to_fruit2)
print()
