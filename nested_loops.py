# Nested Loops

# Bodies of Loops

# The bodies of loops can contain any statements, including other loops.
# When this occurs, this is known as a nested loop.
# Here is a nested loop involving 2 for loops.
# Run it through the Python Visualizer (http://www.pythontutor.com/visualize.html#mode=edit) for a better look:
print()
for i in range(10, 13):
    for j in range(1, 5):
        print(i, j)
print("Finished")
print()
# Notice that when i is 10, the inner loop executes in its entirety, and only after j has ranged from
# 1 through 4 is i assigned the value 11.


## Example of nested loops

def calculate_averages(grades):
    """
    (list of list of number) -> list of float

    Return a new list in which each item is the average of the grades in the
    inner list at the corresponding position od grades.

    >>> calculate_averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    """
    averages = []
    # Calculate the average of each sublist and append it to averages.
    for grades_list in grades:
        # Calculate the average of grades_list.
        total = 0
        for mark in grades_list:
            total = total + mark   # total += mark also works

        averages.append(total / len(grades_list))

    return averages

print(calculate_averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]]))
print()

# In calculate_averages(), the outer for loop iterates through each sublist in grades.
# We then calculate the average of that sublist using a nested (or inner) loop, and add the average to the accumulator.
# In this function, the accumulator is the variable averages, which becomes a new list as the values are appended.


#!# This bit of code from the lecture tripped me up because I didn't read it carefully.
# What should total return?

def mystery(quiz_list):
    for sublist in quiz_list:
        total = 0
        for num in sublist:
            total = total + num

    return total

print(mystery([[10, 20], [20], [40, 10]]))
print()

# Notice that total is reset to 0 before each inner loop, so when total is returned, it will only contain
# the sum of the items in the last sublist that is passed in.
# If we want to total over all of the sublists, we would have to initialize total to 0 before the first for loop.
