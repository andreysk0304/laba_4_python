class Player:
    def __init__(self, name: str, balance: int = 100):
        self.name = name
        self.balance = balance


    def change_balance(self, amount: int):
        self.balance += amount

    def __repr__(self):
        return f"Игрок {self.name} имеет {self.balance} монет"