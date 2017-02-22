import tkinter.filedialog
import grade

# I still need to find or create a file 'grades.txt' with an 'id' column and 'grade' column.

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')

a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename, 'w')

# 1. Read the grades into a list.
grades = grade.read_grades(a1_file)

# 2. Count the number of grades per range.
range_counts = grade.count_grade_ranges(grades)

# print(range_counts)

# 3. Write the histogram to the file.
grade.write_histogram(range_counts, a1_histfile)

# 4. Close the files
a1_file.close()
a1_histfile.close()

"""
Histogram buckets as follows:

0-9:   index 0
10-19: index 1
20-29:       2
...
90-99:       9
100:   index 10
"""
