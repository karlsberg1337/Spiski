import random

numbers = [random.randint(1, 101) for _ in range(10)]

x = random.randint(1, 101)

if x in numbers:
    print(numbers.index(x))
else:
    print('-1')
