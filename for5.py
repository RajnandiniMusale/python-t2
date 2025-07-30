import math

n = int(input("Enter a number: "))
sum_series = 1
for i in range(1, n + 1):
    sum_series += 1 / math.factorial(i)
print(f"The sum of the series is: {sum_series}")