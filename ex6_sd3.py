# the other instances of formatting strings used variables that were not
# strings. To prove it, I'll use the function type to print out the 
# type of each variable used in a formatted string

# recreate the variables from ex6
types_of_people = 10
x = f"There are {types_of_people} type of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
hilarious = False

# print type of each variable
print("types_of_people:", type(types_of_people))
print("x:", type(x))
print("binary:", type(binary))
print("do_not:", type(do_not))
print("y:", type(y))
print("hilarious:", type(hilarious))
