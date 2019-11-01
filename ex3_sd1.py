# print out text announcing the counting of the chickens
print("I will now count my chickens:")

# print out Hens then a space then divid 30 by 6 to get 5
# then add 25 to 5 to get 30, then print 30 next to Hens
print("Hens", 25 + 30 / 6)
# print out Roosters, then multiply 25 by 3 to get 75
# then take the modulus of 75 and 4, which is 3
# then subtract 3 from 100, which is 97
# then print 97 after Roosters
print("Roosters", 100 - 25 * 3 % 4)

# print out text announcing the counting of the eggs
print("Now I will count the eggs:")

# *sigh, pulls out pen and paper*
# 4 modulo 2 is 0, 1 divided by 4 is 0.25 (fractional egg?)
# then from left to right, 3 plus 2 is 5
# five plus 1 is 6, six minus 5 is 1
# one plus 0 (from the modulo operation) is 1
# one minus 0.25 (from the division operation) is 0.75
# 0.75 plus 6 is 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# print text asking if mathematical statement is true
print("Is it true that 3 + 2 < 5 -7?")

# 3 plus 2 is 5, 5 minus 7 (intentinally omitting space here?)
# is -2, so evaluating the statement that 5 is less than -2
# which is false, so it prints False 
print(3 + 2 < 5 - 7)

# prints out text and then the answer to 3 plus 2, which is 5
print("What is 3 + 2?", 3 + 2)
# prints out text and then the answer to 5 minus 7, which is -2
print("What is 5 - 7?", 5 - 7)

#print out text statement
print("Oh, that's why it's False.")

# print out yet another text statement
print("How about some more.")

# print out text then result of 5 greater than -2, which is True
print("Is it greater?", 5 > -2)
# print out the text then result of 5 greater than or equal to -2
# which is True
print("Is it greater or equal?", 5 >=-2)
# print out text statment and then the reslut of 5 less than or
# equal to -2, which is False
print("Is it less or equal?", 5 <= -2)
