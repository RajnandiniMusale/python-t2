n = int(input("Enter the value of n: "))
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1

print("Sum of even numbers up to", n, "is:", sum)
