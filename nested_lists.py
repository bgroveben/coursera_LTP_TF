# Lists can contain items of any type, including other lists.
# These are called nested lists.

grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]
print()
print("grades[0]: ")
print(grades[0])
print()
print("grades[1]: ")
print(grades[1])
print()
print("grades[2]: ")
print(grades[2])
print()

# To access a nested item, first select the sublist, and then treat the result as a regular list.
# For example, to access 'Assignment 1', we can first get the sublist and then use it as we would a regular list:

sublist = grades[0]
print("sublist: ")
print(sublist)
print()
print("sublist[0]: ")
print(sublist[0])
print()
print("sublist[1]: ")
print(sublist[1])
print()

# Both sublist and grades[0] contain the memory address of the ['Assignment 1', 80] nested list.
# We can access the items inside the nested lists like this:

print("grades[0][0]: ")
print(grades[0][0])
print()
print("grades[0][1]: ")
print(grades[0][1])
print()
print("grades[1][0]: ")
print(grades[1][0])
print()
print("grades[1][1]: ")
print(grades[1][1])
print()
print("grades[2][0]: ")
print(grades[2][0])
print()
print("grades[2][1]: ")
print(grades[2][1])
print()
