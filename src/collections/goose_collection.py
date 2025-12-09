class GooseCollection:
    def __init__(self):
        self._geese = []

    def add(self, goose):
        self._geese.append(goose)

    def remove(self, goose):
        self._geese.remove(goose)

    def __getitem__(self, index):
        return self._geese[index]

    def __iter__(self):
        return iter(self._geese)

    def __len__(self):
        return len(self._geese)

    def __repr__(self):
        return f"GooseCollection -> {len(self)} зверей, делающих 'га-га-га' :D"