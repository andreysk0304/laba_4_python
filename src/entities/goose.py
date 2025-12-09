class Goose:
    def __init__(self, name: str, honk_volume: int = 1):
        self.name = name
        self.honk_volume = honk_volume

    def honk(self):
        return f"{self.name} ОРЁТ с громкостью {self.honk_volume} дб"

    def __repr__(self):
        return f"{self.__class__.__name__} -> {self.name}"


class WarGoose(Goose):
    def attack(self, player):
        damage = 5 * self.honk_volume
        player.change_balance(-damage)
        return f"{self.name} атакует {player.name} и отнимает {damage} монет!"


class HonkGoose(Goose):
    def special_honk(self, players):
        effect = -self.honk_volume

        for p in players:
            p.change_balance(effect)

        return f"{self.name} устраивает крик! Все игроки теряют {abs(effect)} монет :D"