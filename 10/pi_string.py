file_name: str = 'pi_digits.txt'
with open(file_name) as file_object:
    lines: list = file_object.readlines()

pi_string: str = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
