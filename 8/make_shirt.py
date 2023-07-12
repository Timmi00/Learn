def make_shirt(
        size: str = 'l',
        text: str = 'I love Python',
):
    print(f'Your tshirt size : {size.upper()}\n'
          f'Your text is:'
          f'"{text}"'
          '\n------------------')


make_shirt('xs', 'I love BANANA\'S')
make_shirt(text='I love BANANA\'S', size='xs')
make_shirt()
