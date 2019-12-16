from sys import argv

script, filename = argv

print(f"We are going to read {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print(f"Opening {filename}...")
target = open(filename)

print(target.read())
target.close()
