import random

number = random.randint(3, 20)
print(number)

# def get_unique_numbers(text):
#     unique = ''
#     for number in text:
#         if number in unique:
#             continue
#         else:
#             unique += number
#         return unique

text = ''
for x in range(1, number):
    for y in range(1, number):
        if number % (x + y) == 0:
            text += f"{x}{y}"

print(text)
