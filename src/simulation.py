import random
from casino import Casino
from entities.goose import WarGoose, HonkGoose, Goose


def run_simulation(steps: int = 20, seed: int | None = None):
    if seed is not None:
        random.seed(seed)

    casino = Casino()

    casino.register_player("Alice")
    casino.register_player("Bob")
    casino.register_player("Charlie")

    casino.register_goose(WarGoose("Гусяра намба ван", 2))
    casino.register_goose(HonkGoose("ГУСЫНЯ ( жена Гусяры )", 3))
    casino.register_goose(Goose("просто гусь ю-ю", 1))

    print(f"Симуляция запущена! (seed = {seed if seed is not None else 'не задан'}, steps = {steps})")
    for step in range(steps):
        print(f"\nШаг {step + 1}")
        casino.simulate_step()
    print("\nСИМУЛЯЦИЯ ОКОНЧЕНА")
