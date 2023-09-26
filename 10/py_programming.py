file_name: str = 'programming.txt'
with open(file_name) as file_object:
    lines: str = file_object.read()

print(lines.replace('love', 'c'))

