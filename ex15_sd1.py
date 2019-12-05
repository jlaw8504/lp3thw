# improt the argv function from sys module
from sys import argv

# parse the command-line arguments
script, filename = argv

# create a file class called txt using the open function
txt = open(filename)

# print out a formatted string referencing filename
print(f"Here's your file {filename}:")
# print out the results of calling the read method from
# the txt instance of the file class
print(txt.read())

# print out string
print("Type the filename again:")
# prompt user with > for input
file_again = input("> ")

# create another file class instance named txt_again
txt_again = open(file_again)

# print out the results of calling the read method from
# the txt_again instance of the file class
print(txt_again.read())
