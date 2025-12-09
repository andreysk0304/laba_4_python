class CasinoBalance:
    def __init__(self):
        self._balances = {}

    def __getitem__(self, key):
        return self._balances[key]

    def __setitem__(self, key, value):
        print(f"[LOG] Баланс {key} изменён → {value}")
        self._balances[key] = value

    def __iter__(self):
        return iter(self._balances.items())

    def __len__(self):
        return len(self._balances)

    def __repr__(self):
        return f"Баланс {self._balances} монет"