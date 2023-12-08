import random

rl = [random.randint(1, 100) for _ in range(10)]

print("первый список:", rl)

maxt = rl.index(max(rl))
mint = rl.index(min(rl))

rl[maxt], rl[mint] = rl[mint], rl[maxt]

print("второй список:", rl)
