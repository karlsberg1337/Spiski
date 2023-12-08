import random

n = int(input('Введите число: '))

numbers = [random.randint(1, 100) for _ in range(n)]

print(numbers[::2])
