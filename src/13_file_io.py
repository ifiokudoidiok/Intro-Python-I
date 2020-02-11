"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
# <-- absolute dir the script is in
script_dir = os.path.dirname(os.path.realpath(__file__))
# print(script_dir)
rel_path = "/foo.txt"
abs_file_path = script_dir+rel_path
# print(abs_file_path)
with open(abs_file_path) as f:
    read_data = f.read()
    print(read_data)

# with open('src/foo.txt', 'r') as f:
#     read_data = f.read()
# print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new_path = script_dir+"/bar.txt"
with open(new_path, "w") as f:
    f.write("Today is Cyber safe day!\n")
    f.write("What better way to celebrate\n")
    f.write("than to download the first security hand book in Africa?")


with open(new_path) as f:
    read_data = f.read()
    print(read_data)

