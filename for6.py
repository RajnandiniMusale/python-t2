import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))
cos_x = 1
sign = -1
for i in range(2, n + 1, 2):
    term = (x**i) / math.factorial(i)
    cos_x += sign * term
    sign *= -1
print(f"The approximate value of cos({x}) is: {cos_x}")