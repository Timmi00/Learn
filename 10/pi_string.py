file_name: str = 'programming.txt'
with open(file_name) as file_object:
    lines: str = file_object.read()
    print(lines)


pi_string: str = ''
for line in lines:
    print(f'{line}', end='')
    pi_string += line
print(pi_string)

# birthday: str = input()
# if birthday in pi_string:
#     print('yes')
# else:
#     print('no')
