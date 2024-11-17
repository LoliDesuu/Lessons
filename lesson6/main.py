import random
from enum import unique

number = random.randint(3, 20)
print(f"Число на первом камне: {number}")

text = ''
for x in range(1, number):
    for y in range(1, number):
        if number % (x + y) == 0:
            text += f"{x}{y}"

print(f"Число на втором камне: {text}")
