import array

# create integer array
numbers = array.array('i', [10, 20, 30, 40, 50])

print("Original array:", numbers)

# 1. append(x) – add element at end
numbers.append(60)
print("After append:", numbers)

# 2. insert(i, x) – insert at index
numbers.insert(2, 25)
print("After insert:", numbers)

# 3. remove(x) – remove first occurrence of element
numbers.remove(40)
print("After remove 40:", numbers)

# 4. pop() – remove last element
numbers.pop()
print("After pop:", numbers)

# 5. index(x) – find index of element
print("Index of 30:", numbers.index(30))

# 6. reverse() – reverse array
numbers.reverse()
print("After reverse:", numbers)

# 7. count(x) – count how many times element occurs
print("Count of 20:", numbers.count(20))

# 8. buffer_info() – memory info (address, length)
print("Buffer info:", numbers.buffer_info())

# 9. extend() – add multiple elements
numbers.extend([70, 80, 90])
print("After extend:", numbers)

# 10. fromlist(list) – add elements from list
numbers.fromlist([100, 110])
print("After fromlist:", numbers)

# 11. tolist() – convert array to list
print("Convert to list:", numbers.tolist())
