# create and write to a file
f = open("seek_example.txt", "w")
f.write("Hello World!\n")
f.write("Python File Handling Example.\n")
f.close()

# open file for reading
f = open("seek_example.txt", "r")

# tell() -> shows current position of file pointer
print("Initial position:", f.tell())

# read first 5 characters
data = f.read(5)
print("Data read:", data)
print("Position after reading 5 chars:", f.tell())

# move pointer back to beginning using seek()
f.seek(0)
print("Position after seek(0):", f.tell())

# read again from beginning
print("Reading again:", f.readline())

# move pointer to 6th byte
f.seek(6)
print("Position after seek(6):", f.tell())
print("Data from position 6:", f.read())

f.close()
