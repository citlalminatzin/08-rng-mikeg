
def create_game()->int:
    """Escoge la puerta ganadora"""
    ...

def play_change(n:int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    ...
def play_stay(n:int = 1000)->float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    ...

def main():
    success_change = play_change()
    success_stay   = play_stay()
    print(f"{success_change=} {success_stay=}")


if "__name__" == "__main__":
    main()