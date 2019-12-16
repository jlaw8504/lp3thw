from sys import argv

script, filename = argv

text = "This is some text to write to a file"

target = open(filename, 'w')

print(f"Writing text to {filename}.")
target.write(text)
target.close()

print(f"Opening {filename} for writing again.")
print("But I'm not going to actually write anything.")
print("I wonder if the text will disappear?")

target = open(filename, 'w')
target.close()

print("Please open {filename} to check...")

