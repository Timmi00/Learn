def build_person(
        first_name: str,
        last_name: str,
        age = None
                ):
    person: dict = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician: dict = build_person('jimmi', 'hendrix', age=27)
print(musician)
