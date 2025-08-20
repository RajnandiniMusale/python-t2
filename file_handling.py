










# Writing data into a file
f = open("sample.txt", "w")   # open file in write mode
f.write("Hello, this is the first line.\n")
f.write("This is the second line.\n")
f.write("This is the third line.\n")
f.close()

# Reading entire file using read()
f = open("sample.txt", "r")
print("Reading full file using read():")
print(f.read())
f.close()

# Reading line by line using readline()
f = open("sample.txt", "r")
print("\nReading file using readline():")
print(f.readline())   # first line
print(f.readline())   # second line
print(f.readline())   # third line
f.close()
