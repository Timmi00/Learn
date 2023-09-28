class Emploee:
    """Base worker model"""

    def __init__(
            self,
            name: str,
            lastname: str,
            fee: int = 500,
    ):
        """Init"""
        self.name: str = name
        self.lastname: str = lastname
        self.fee: int = fee

    def give_raise(self, give: int = 500):
        self.fee += give


# my_worker = Emploee('Alex', 'Spam', 500)
# print(f'{my_worker.lastname.title()} {my_worker.name.title()} has {my_worker.fee}$')
# my_worker.give_raise()
# print(f'{my_worker.lastname.title()} {my_worker.name.title()} has {my_worker.fee}$')
