filename: str = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents: str = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words: list = contents.split()
    num_words: int = len(words)
    print(f"The file {filename} has about {num_words} words.")
