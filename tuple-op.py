# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 50)

# 1. Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 2. Slicing
print("Slice (index 1 to 3):", my_tuple[1:4])

# 3. Loop through tuple
print("All elements:")
for item in my_tuple:
    print(item)

# 4. Check if an item exists
print("Is 20 in tuple?", 20 in my_tuple)

# 5. Length of tuple
print("Length of tuple:", len(my_tuple))

# 6. Count occurrences of a value
print("How many times 20 appears:", my_tuple.count(20))

# 7. Find index of first occurrence
print("Index of 30:", my_tuple.index(30))

# 8. Convert tuple to list to modify
temp_list = list(my_tuple)
temp_list.append(60)
my_tuple = tuple(temp_list)
print("Modified tuple:", my_tuple)
