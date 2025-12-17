import random

from src.collections.player_collection import PlayerCollection
from src.collections.goose_collection import GooseCollection
from src.collections.balance_dict import CasinoBalance
from src.entities.player import Player
from src.entities.goose import Goose, WarGoose, HonkGoose
from src.entities.chip import Chip
from src.exceptions import InsufficientPlayersError, InsufficientGeeseError, InsufficientWarGeeseError, InsufficientHonkGeeseError, PlayerAlreadyExistsError


class Casino:
    def __init__(self):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balance = CasinoBalance()


    def register_player(self, name: str):
        # Проверяем, не зарегистрирован ли уже игрок с таким именем
        if name in [p.name for p in self.players]:
            raise PlayerAlreadyExistsError(name)
        p = Player(name)
        self.players.add(p)
        self.balance[p.name] = p.balance
        return p


    def register_goose(self, goose):
        self.geese.add(goose)


    def event_player_bet(self):
        if not self.players:
            raise InsufficientPlayersError("ставка")
        player = random.choice(self.players)
        bet = random.randint(5, 20)
        player.change_balance(-bet)
        self.balance[player.name] = player.balance
        print(f"{player.name} делает ставку {bet}")


    def event_player_win(self):
        if not self.players:
            raise InsufficientPlayersError("выигрыш")
        player = random.choice(self.players)
        win = random.randint(10, 40)
        player.change_balance(win)
        self.balance[player.name] = player.balance
        print(f"{player.name} выигрывает {win}")


    def event_goose_attack(self):
        war_geese = [g for g in self.geese if isinstance(g, WarGoose)]
        if not war_geese:
            raise InsufficientWarGeeseError()
        if not self.players:
            raise InsufficientPlayersError("атака гуся")
        goose = random.choice(war_geese)
        player = random.choice(self.players)
        print(goose.attack(player))
        self.balance[player.name] = player.balance


    def event_goose_honk(self):
        honk_geese = [g for g in self.geese if isinstance(g, HonkGoose)]
        if not honk_geese:
            raise InsufficientHonkGeeseError()
        if not self.players:
            raise InsufficientPlayersError("крик гуся")
        goose = random.choice(honk_geese)
        msg = goose.special_honk(self.players)
        print(msg)
        for p in self.players:
            self.balance[p.name] = p.balance


    def event_steal(self):
        if not self.geese:
            raise InsufficientGeeseError("кража")
        if not self.players:
            raise InsufficientPlayersError("кража")
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
