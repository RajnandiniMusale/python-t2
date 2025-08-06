# my_list=[1,2,3]
# my_list.append(4)
# print(my_list)



#list operations

# List declaration
numbers = [5, 10, 15]

# Adding elements
numbers.append(20)
numbers.insert(1, 7)

# Removing elements
numbers.remove(10)
last = numbers.pop()

# Info
print("List:", numbers)
print("Length:", len(numbers))
print("Index of 7:", numbers.index(7))
print("Count of 5:", numbers.count(5))

# Sorting and reversing
numbers.sort()
numbers.reverse()

# Final list
print("Final List:", numbers)

# Clear all
numbers.clear()
print("After clear:", numbers)
