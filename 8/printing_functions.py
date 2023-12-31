def print_models(unprinted_designs: list,
                 complete_models: list,
                 ):
    while unprinted_designs:
        current_design: str = unprinted_designs.pop()
        print(f'Printing model: {current_design.upper()}')
        complete_models.append(current_design)


def show_completed_models(completed_models: list):
    print('\nThe followed models have been printed: ')
    for completed_model in completed_models:
        print(completed_model.upper())
