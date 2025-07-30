def print_number_triangle_ascending(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# Example usage for n = 5
print_number_triangle_ascending(5)