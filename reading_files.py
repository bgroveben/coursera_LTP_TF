## Reading Files

# Information stored in files can be accessed using Python using the open() command.
# When you are done using the file, you need to close() it.

# The form of open is open(filename, mode), where mode is 'r' (reading), 'w' (writing), or 'a' (appending)

# Let's open a file called in_flanders_fields.txt for reading:
flanders_file = open('in_flanders_fields.txt', 'r')

# If the file is saved in the same directory as your program, then you can simply write the name of the file.
# If the file is in a different directory, you must provide the path to it.

# To close a file, enter the command:
flanders_file.close()

# There are four standard ways to read from a file. Some use these methods:

# readline(): Read and return the next line from the file, including the newline character (if it exists).
#             Return the empty string if there are no more lines left in the file.
# This method is used when you want to process only part of a file.
flanders_file = open('in_flanders_fields.txt', 'r')
flanders_poem = ''
print()
print("Reading files -- the readline() approach: ")
print()
line = flanders_file.readline()
while line != "":
    flanders_poem = flanders_poem + line
    line = flanders_file.readline()  # it's a while loop, so be careful
print(flanders_poem)
print()
flanders_file.close()

# readlines(): Read and return all lines in a file in a list.
#              The lines include the newline character.
# This method is used when you want to examine each line of a file by index.
print()
print("Reading files -- the readlines() approach: ")
print()
flanders_file = open('in_flanders_fields.txt', 'r')
flanders_poem = ''
flanders_list = flanders_file.readlines()
for line in flanders_list:
    flanders_poem = flanders_poem + line
print(flanders_poem)
flanders_file.close()
print()

# read(): read the whole file as a single string.
# This method is used when you want to read the whole file at once and use it as a single string.
print()
print("Reading files -- the read() approach: ")
print()
flanders_file = open('in_flanders_fields.txt', 'r')
flanders_poem = flanders_file.read()
print(flanders_poem)
flanders_file.close()
print()

# The for line in file approach.
# This method is used when you want to process every line in the file one at a time.
print("Reading files -- the for line in lines approach: ")
print()
flanders_file = open('in_flanders_fields.txt', 'r')
flanders_poem = ''
for line in flanders_file:
    flanders_poem = flanders_poem + line
print(flanders_poem)
print()
flanders_file.close()


# There are different approaches and methods you can use when reading files.
# This example will print out the first stanza:
flanders_file = open("in_flanders_fields.txt", "r")
print("First stanza only: ")
print()
line = flanders_file.readline()
line = flanders_file.readline()
line = flanders_file.readline()
while line != '\n':
    print(line)
    line = flanders_file.readline()
flanders_file.close()
print()

# This example reads the file as one big string:
flanders_file = open('in_flanders_fields.txt', 'r')
print("Here's the poem as a single string: ")
print()
print(flanders_file.readlines())
print()
