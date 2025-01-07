
def custom_write(file_name, string):
    with open(file_name, 'w', encoding='utf-8') as file:
        for elem in string:
            file.write(f'{elem}\n')
        file.close()
    keys = ()
    keys = list(keys)
    lines = 0
    with open(file_name, 'rb') as file:
        file_pos = 0
        for line in file:
            lines += 1
            key = lines, file_pos
            keys.append(key)
            file_pos += len(line)
        file.close()
    string_position = dict(zip(keys, info))
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


