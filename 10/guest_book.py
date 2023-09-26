filename: str = 'guest_book.txt'
with open(filename, 'w') as file_object:
    n: str = input('Введите свое имя: ')
    while n:
        file_object.write(f'{n}\n')
        n = input('Введите свое имя: ')
