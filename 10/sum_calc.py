while True:
    try:

        print(f'Результат сложения {int(input("Введите первое число ")) + int(input("Введите второе число "))}')
        if input('нажмите ввод чтобы продолжить '):
            break
    except ValueError:
        print('Вы ввели не число')
