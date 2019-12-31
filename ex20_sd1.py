# import argv funciton from sys module
from sys import argv

# parse script (but don't use) and input_file from command line
script, input_file = argv

# define print_all function with one input
def print_all(f):
    # print out whole file in variable f
    print(f.read())

# define rewind function with one input
def rewind(f):
    # reset file object position to beginning line
    f.seek(0)

# define print_a_line function with one input
def print_a_line(line_count, f):
    # print out line_count variable and current line in file object
    print(line_count, f.readline())

# open the input_file specified by the user in the command line
# argument
current_file = open(input_file)

# print out a message to the user that script will print 
# the entire contents of the file
print("First let's print the whole file:\n")

# call print_all function on current_file to print the entire file
print_all(current_file)

# print out a message to the user that script will rewind file
# object position so we can print out file line by line from 
# the beginning of the file
print("Now let's rewind, kind of like a tape.")

# call rewind file to reset file object position to beginning
rewind(current_file)

# print message to user that script will print three lines of file
print("Let's print three lines:")

# define current_line variable as 1
current_line = 1
# call print_a_line function with current_line and current_file
# variables as input
print_a_line(current_line, current_file)

# increment current_line variable by one
current_line = current_line + 1
# call print_a_line function with current_line and current_file
# variables as input
print_a_line(current_line, current_file)

# increment current_line variable by one
current_line = current_line + 1
# call print_a_line function with current_line and current_file
# variables as input
print_a_line(current_line, current_file)
