def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


# formula to copy: 3/(1+(8/(5-1)) 
print("Here is a puzzle.")

what = divide(3, add(1, divide(8, subtract(5, 1))))

print("That becomes: ", what, "Can you do it by hand?")
