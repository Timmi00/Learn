from name_function import get_formatted_name

print('Enter q at any time to quit ')
while True:
    first: str = input('\nPlease give me a first name ')
    if first == 'q':
        break
    last: str = input('Please give me a last name ')
    if last == 'q':
        break

    formatted_name: str = get_formatted_name(first, last)
    print(f'\tNeatly formatted name: {formatted_name}')
