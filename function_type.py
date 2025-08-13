# 1. Normal Function
def greet():
    print("Hello, world!")

# 2. Function with Parameters
def add(a, b):
    return a + b

# 3. Default Arguments
def greet_person(name="Guest"):
    print("Hello,", name)

# 4. Keyword Arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 5. Variable Number of Arguments (*args)
def add_all(*args):
    return sum(args)

# 6. Variable Number of Keyword Arguments (**kwargs)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 7. Lambda Functions
square = lambda x: x * x
add_lambda = lambda a, b: a + b

# -----------------------------
# OUTPUT SECTION
# -----------------------------
print("\n1. Normal Function:")
greet()

print("\n2. Function with Parameters:")
print("5 + 3 =", add(5, 3))

print("\n3. Default Arguments:")
greet_person("Riya")
greet_person()  # uses default

print("\n4. Keyword Arguments:")
student_info(age=21, name="Riya")

print("\n5. *args (Variable Positional Arguments):")
print("Sum of numbers:", add_all(1, 2, 3, 4, 5))

print("\n6. **kwargs (Variable Keyword Arguments):")
show_info(name="Riya", age=21, city="Pune")

print("\n7. Lambda Functions:")
print("Square of 5:", square(5))
print("Add using lambda (3 + 7):", add_lambda(3, 7))

# Using lambda in map, filter, sort
nums = [1, 2, 3, 4, 5]
print("\nSquares using map:", list(map(lambda x: x**2, nums)))
print("Even numbers using filter:", list(filter(lambda x: x % 2 == 0, nums)))

pairs = [(1, 4), (2, 1), (3, 3)]
pairs.sort(key=lambda x: x[1])
print("Sorted by second element using lambda:", pairs)
