class PlayerCollection:
    def __init__(self):
        self._players = []

    def add(self, player):
        self._players.append(player)

    def remove(self, player):
        self._players.remove(player)

    def __getitem__(self, index):
        return self._players[index]

    def __iter__(self):
        return iter(self._players)

    def __len__(self):
        return len(self._players)

    def __repr__(self):
        return f"PlayerCollection -> {len(self)} игроков"
