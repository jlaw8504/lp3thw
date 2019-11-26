# Set the formatter string variable to four braces
formatter = "{} {} {} {}"

# print out 1, 2, 3, 4 by formatting the formatter string
print(formatter.format(1, 2, 3, 4))
# print out one, two , three, four by formatting the formatter string
print(formatter.format("one", "two", "three", "four"))
# print out True False False True by formatting the formatter string
print(formatter.format(True, False, False, True))
# print out the four braces of the formatter string four times by
# formatting the formatter string with the formatter string 
print(formatter.format(formatter, formatter, formatter, formatter))
# print out Try your Own text here Maybe a poem Or a song about fear
# by formatting the formatter string
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
