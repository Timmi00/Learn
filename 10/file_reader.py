file_name: str = 'pi_digits.txt'
with open(file_name) as file_object:
    lines: list = file_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())
