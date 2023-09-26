def count_words(file_name):
    """ПОДСЧЕТ КОЛИЧЕСТВА СЛОВ В ФАЙЛЕ"""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)


filenames: list = [
    'alice.txt',
    'moby_dick.txt',
    'siddhartha.txt',
    'little_women.txt'
    ]
for filename in filenames:
    count_words(filename)
