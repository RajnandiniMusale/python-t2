import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
sqrt_num = math.sqrt(num)

if sqrt_num == int(sqrt_num): 
    if is_prime(int(sqrt_num)):
        print(f"The square root of {num} ({int(sqrt_num)}) is prime.")
    else:
        print(f"The square root of {num} ({int(sqrt_num)}) is not prime.")
else:
    print(f"The square root of {num} is not an integer.")