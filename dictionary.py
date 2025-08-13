# Creating dictionary
student = {
    "name": "Riya",
    "age": 20,
    "marks": 85
}

# Accessing values
print("Name:", student["name"])  # Direct access
print("Age using get:", student.get("age"))

# Adding / Updating
student["city"] = "Pune"  # Add
student["marks"] = 90     # Update
print("Updated dict:", student)

# Keys, Values, Items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Removing elements
student.pop("age")       # Remove by key
student.popitem()        # Remove last inserted
print("After removal:", student)

# Merging dictionaries
extra_info = {"gender": "Female", "hobby": "Reading"}
student.update(extra_info)
print("After merge:", student)

# Clearing dictionary
student.clear()
print("After clear:", student)
