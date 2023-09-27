filename: str = input('Введите имя файла с расширением ')

try:
    with open(filename, encoding='utf-8') as f:
        content: str = f.read()
except FileNotFoundError:
    print('?')
else:
    print(content.lower().count('the '))
