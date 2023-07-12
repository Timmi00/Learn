responses: dict = {}
polling_active = True
while polling_active:
    name: str = input("\nWhat is your name? ")
    response: str = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat: str = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---POOL RESULTS---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
