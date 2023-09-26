from random import choice


all_slice = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
win_slice = f'{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}'
my_slice: str = input('Введите выигрушную комбинацию: ')
count: int = 1
while my_slice != win_slice:
    print(f'{win_slice}', end=' ')
    count += 1
    win_slice = f'{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}{choice(all_slice)}'
print(f'\n{count}')
