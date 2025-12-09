import random

from collections.player_collection import PlayerCollection
from collections.goose_collection import GooseCollection
from collections.balance_dict import CasinoBalance
from entities.player import Player
from entities.goose import Goose, WarGoose, HonkGoose
from entities.chip import Chip


class Casino:
    def __init__(self):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balance = CasinoBalance()

    def register_player(self, name: str):
        p = Player(name)
        self.players.add(p)
        self.balance[p.name] = p.balance
        return p

    def register_goose(self, goose):
        self.geese.add(goose)

    def event_player_bet(self):
        player = random.choice(self.players)
        bet = random.randint(5, 20)
        player.change_balance(-bet)
        self.balance[player.name] = player.balance
        print(f"{player.name} делает ставку {bet}")

    def event_player_win(self):
        player = random.choice(self.players)
        win = random.randint(10, 40)
        player.change_balance(win)
        self.balance[player.name] = player.balance
        print(f"{player.name} выигрывает {win}")

    def event_goose_attack(self):
        goose = random.choice([g for g in self.geese if isinstance(g, WarGoose)])
        player = random.choice(self.players)
        print(goose.attack(player))
        self.balance[player.name] = player.balance

    def event_goose_honk(self):
        goose = random.choice([g for g in self.geese if isinstance(g, HonkGoose)])
        msg = goose.special_honk(self.players)
        print(msg)
        for p in self.players:
            self.balance[p.name] = p.balance

    def event_steal(self):
        goose = random.choice(self.geese)
        player = random.choice(self.players)
        stolen = random.randint(1, 10)
        player.change_balance(-stolen)
        print(f"{goose.name} крадёт {stolen} у {player.name}")
        self.balance[player.name] = player.balance

    def simulate_step(self):
        events = [
            self.event_player_bet,
            self.event_player_win,
            self.event_goose_attack,
            self.event_goose_honk,
            self.event_steal,
        ]
        random.choice(events)()
