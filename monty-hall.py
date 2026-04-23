from random import random 

def create_game() -> int:
    #Escoge la puerta ganadora
    return int(random() * 3)

def play_change(n:int = 1000) -> float:    
    # Jugamos monty-hall con la estrategia de SI cambiar la puerta
    wins = 0
    for _ in range(n):
        winning_door = create_game()
        player_choice = int(random() * 3)
        # Monty abre una puerta que no es la ganadora ni la elegida por el jugador
        monty_choice = next(door for door in range(3) if door != winning_door and door != player_choice)
        # El jugador cambia a la otra puerta que no es la elegida ni la abierta por Monty
        player_choice = next(door for door in range(3) if door != player_choice and door != monty_choice)
        if player_choice == winning_door:
            wins += 1
    return wins / n

    
def play_stay(n:int = 1000)->float:
    # Juega monty-hall con la estrategia de NO cambiar la puerta
    wins = 0
    for _ in range(n):
        winning_door = create_game()
        player_choice = int(random() * 3)
        # Monty abre una puerta que no es la ganadora ni la elegida por el jugador
        monty_choice = next(door for door in range(3) if door != winning_door and door != player_choice)
        # El jugador no cambia su elección
        if player_choice == winning_door:
            wins += 1
    return wins / n

def main():
    success_change = play_change()
    success_stay   = play_stay()
    print(f"{success_change=} {success_stay=}")

if __name__ == "__main__":    
    main()