# define the function cheese_and_crackers with two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print out the number of cheeses in your possession
    print(f"You have {cheese_count} cheeses!")
    # print out the number of boxes of crackers in your possession
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print message about party 
    print("Man that's enough for a party!")
    # print out blanket suggestion
    print("Get a blanket.\n")


# print out variable usage
print("We can just give the function numbers directly:")
# call function with two integers as input
cheese_and_crackers(20,30)


# print out variable usage
print("OR, we can use variables from our script:")
# assign integer to amount_of_cheese variable
amount_of_cheese = 10
# assign integer to amount_of_crackers variable
amount_of_crackers = 50

# call function using variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print out variable usage
print("We can even do math inside too:")
# call function with mathematical expression
cheese_and_crackers(10 + 20, 5 + 6)


# print out varible usage
print("And we can combine the two, variables and math:")
# call function with mathematical expressions combining
# integers and variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
