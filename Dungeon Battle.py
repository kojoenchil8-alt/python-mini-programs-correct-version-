import random
import time


def create_enemy(level):
    """Generate a random enemy scaled to the player's current floor level."""
    enemies = [
        {"name": "Goblin Scout", "hp": 25 + (level * 5), "atk": 6 + level, "gold": 12},
        {"name": "Shadow Slime", "hp": 30 + (level * 6), "atk": 5 + level, "gold": 15},
        {"name": "Skeleton Knight", "hp": 40 + (level * 8), "atk": 8 + level, "gold": 22},
        {"name": "Stone Golem", "hp": 55 + (level * 10), "atk": 10 + level, "gold": 30}
    ]
    return random.choice(enemies).copy()


def battle_enemy(player, enemy):
    """Handle the battle between the player and the enemy."""
    print(f"\nA wild {enemy['name']} appears!")
    time.sleep(1)

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | Enemy HP: {enemy['hp']}")
        action = input("Choose your action (attack/run/defend): ").lower()

        if action == "attack":
            damage = random.randint(player["atk"] - 2, player["atk"] + 2)
            enemy["hp"] -= damage
            print(f"You attack the {enemy['name']} for {damage} damage!")

            if enemy["hp"] <= 0:
                print(f"You defeated the {enemy['name']}!")
                player["gold"] += enemy["gold"]
                print(f"You found {enemy['gold']} gold! Total gold: {player['gold']}")
                return True

            enemy_damage = random.randint(enemy["atk"] - 2, enemy["atk"] + 2)
            player["hp"] -= enemy_damage
            print(f"The {enemy['name']} attacks you for {enemy_damage} damage!")

        elif action == "defend":
            enemy_damage = random.randint(enemy["atk"] - 2, enemy["atk"] + 2)
            enemy_damage = max(0, enemy_damage - player.get("defense", 0))
            player["hp"] -= enemy_damage
            print(f"You defend and take {enemy_damage} damage!")

        elif action == "run":
            print("You run away safely!")
            return False

        else:
            print("Invalid action. Please choose 'attack', 'run', or 'defend'.")

        time.sleep(0.5)

    if player["hp"] <= 0:
        print("You have been defeated!")

    return False


def play_dungeon_battle():
    """Run the full 5-floor dungeon battle game."""
    player = {
        "hp" : 60,
        "max_hp": 60,
        "atk": 10,
        "gold": 20,
        "potions": 2,
        "floor": 1
    }
    print("\n=== Mini Dungeon Survival ===")
    print("You have 5 floors to conquer. Defeat enemies and survive!")

    while player["floor"] <= 5 and player["hp"] > 0:
        print(f"\n--- Floor {player['floor']} ---")
        enemy = create_enemy(player["floor"])
        survived = battle_enemy(player, enemy)

        if not survived:
            break

        player["floor"] += 1
        if player["floor"] <= 5:
            print(f"You advance to floor {player['floor']}!")
            player["hp"] = min(player["max_hp"], player["hp"] + 10)
            print(f"Your HP is restored to {player['hp']}.")

    if player["hp"] > 0:
        print("\nCongratulations! You have conquered the dungeon!")

    if __name__ == "__main__":
        play_dungeon_battle()