class Chip:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other):
        return Chip(self.amount + other.amount)

    def __repr__(self):
        return f"Фишка на {self.amount} монет"
