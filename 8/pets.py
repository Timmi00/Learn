def describe_pet(
        animal_type: str,
        pet_name: str = 'None',
                 ):
    print(f"\nI have a {animal_type}. ")
    print(
        f"My {animal_type}'s name is {pet_name.title()}"
        )


describe_pet('hamster')
describe_pet(animal_type='dog', pet_name='willie')
