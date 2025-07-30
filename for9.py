def print_alphabet_triangle_ascending(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

# Example usage for n = 5
print_alphabet_triangle_ascending(5)