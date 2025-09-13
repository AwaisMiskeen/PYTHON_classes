
f = open("file.txt")
print(f.readline)
f.close()

# the same can be written using "with statement" like this:

with open("file.txt") as f:
    print(f.read())

# you don't have explicitly close the file
