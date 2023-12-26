name = input("What is your name?\n")

# use variable here
print("Hello", name)

# concatenation
print("Hello " + name + ", your name has " + str(len(name)) + " characters")

# f strings
print(f"Hello {name}, your name has {len(name)} characters")
