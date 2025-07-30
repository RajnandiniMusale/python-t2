def print_alphabet_triangle_descending(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

# Example usage for n = 5
print_alphabet_triangle_descending(5)