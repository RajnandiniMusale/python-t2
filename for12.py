def print_repeating_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print()

# Example usage for n = 5
print_repeating_number_triangle(5)