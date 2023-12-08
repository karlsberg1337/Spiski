import random

numbers = [random.randint(1, 101) for _ in range(10)]

sum = 0
multiply = 1

for i in numbers:
    sum += i
    multiply *= i

print(sum, multiply)
