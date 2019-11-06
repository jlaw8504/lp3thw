# Sets types_of_people variable to 10
# sets x to formatted string referencing
# the types_of_people variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

# sets binary variable to binary string
# sets do_not varialbe to don't string
# sets y variable to formatting string
# referencing binary and do_not variables 
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x varible then print y variable
print(x)
print(y)

# print formatted string that references x and
# then print formatted string that references y
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set hilarious variable to False (a boolean variable)
# set joke_evaluation to string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# print formatted string using .format method
print(joke_evaluation.format(hilarious))

# set w variable to string and set e variable to string
w = "This is the left side of..."
e = "a string with a right side."

# print string resulting from joining w and e
print(w + e)
