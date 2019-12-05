# import argv function from sys module
from sys import argv

# parse the command line using argv
script, filename = argv

# print out warning
print(f"We're going to erase {filename}.")
# print out how to kill script
print("If you don't want that , hit CTRL-C (^C).")
# print out how to proceed
print("If you do want that, hit RETURN.")

# prompt user for input, really giving them a chance
# to kill the script if they so choose
input("?")

# print out string that script is opening file
print("Opening the file...")
# use open function to generate an instance of a file
# object/class? called target
target = open(filename, 'w')

# print out string that file is being truncated
print("Truncating the file. Goodbye!")
# erase the contents of the file
target.truncate()

# print out string asking user for three lines
print("Now I'm going to ask you for three lines.")

# prompt user to enter a line
line1 = input("line 1: ")
# prompt user to enter a line
line2 = input("line 2: ")
# prompt user to enter a line
line3 = input("line 3: ")


# print out string stating file will be written to
print("I'm going to write these to the file.")

# write out line1
target.write(line1)
# write out newline character
target.write("\n")
# write out line2
target.write(line2)
# write out newline character
target.write("\n")
# write out line3
target.write(line3)
# write out newline character
target.write("\n")

# print string that says we are closing the file
print("And finally, we close it.")
# close the file
target.close()



