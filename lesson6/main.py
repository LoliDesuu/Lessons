import random

number = random.randint(3, 21)
print(number)

for x in range(1, number):
    for y in range(1, number):
        if number % (x + y) == 0:
            text = {f"{x}{y}"}
    print(text)
