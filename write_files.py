# Write files

# Writing to a file within a Python program:
# In order to write to a file, we use file.write(str).
# This method writes a string to a file.
# The method write() works like Python's print() function, except it does not add a newline ("\n") character.

# File dialogs:

# Module tkinter has a submodule called filedialog. We import it like this:
import tkinter.filedialog

# Function askopenfilename() asks the user to select a file to open:
tkinter.filedialog.askopenfilename()

# This function returns the full path to the file, so we can use that when we call the function open() to open that file.
from_filename = tkinter.filedialog.askopenfilename()

# Function asksaveasfilename() asks the user to select a file to save to, and provides a warning if the file already exists.
to_filename = tkinter.filedialog.asksaveasfilename()

### Example ###

# Below is a program that copies a file, but puts "Copy" as the first line of the copied file.
# First prompt the user to pick a file, then open the file that we want to read from and get the contents:
from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()

# Now we can open the file we want to write to and write the contents:
to_file = open(to_filename, 'w')
to_file.write('Copy\n')  # we have to add the newline ourselves
to_file.write(contents)  # now write the contents of the file
to_file.close()
