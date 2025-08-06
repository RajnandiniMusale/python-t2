# Two ways to create sets
set1 = {1, 2, 3, 4}                     # Method 1: Using {}
set2 = set([3, 4, 5, 6])                # Method 2: Using set() constructor

print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("\nUnion of Set1 and Set2:", set1.union(set2))

# Intersection
print("Intersection of Set1 and Set2:", set1.intersection(set2))

# Difference
print("Difference (Set1 - Set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Add an element to Set1
set1.add(10)
print("\nAfter adding 10 to Set1:", set1)

# Remove an element from Set1
set1.remove(2)
print("After removing 2 from Set1:", set1)

# Check membership
print("Is 3 in Set1?", 3 in set1)

# Length of Set1
print("Length of Set1:", len(set1))
