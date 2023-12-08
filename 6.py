import random

numbers = [random.randint(1, 100) for _ in range(10)]

for i in numbers:
    if numbers.count(i) > 1:
        print(i)
