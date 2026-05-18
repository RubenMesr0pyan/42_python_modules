import random


def gen_player_achievements() -> set:
    achiv_list = {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable',
        'Sharp Mind', 'Boss Slayer'}

    rnd = random.randint(0, len(achiv_list))
    ply = random.sample(list(achiv_list), rnd)
    return set(ply)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    ply_1 = gen_player_achievements()
    ply_2 = gen_player_achievements()
    ply_3 = gen_player_achievements()
    ply_4 = gen_player_achievements()
    print(f"Player Alice: {ply_1}\n")
    print(f"Player Grno: {ply_2}\n")
    print(f"Player Chach: {ply_3}\n")
    print(f"Player Vzgo: {ply_4}\n")
    print("Track unique achievements among all the players\n")
    print(ply_1.union(ply_2, ply_3, ply_4), "\n")
    print("Find achievements shared by all players\n")
    print(ply_1.intersection(ply_2, ply_3, ply_4))
    print("For each player, spot the achievements no one else has\n")
    print("Player Alice: \n")
    print(ply_1.difference(ply_2, ply_3, ply_4))
    print("Player Grno: \n")
    print(ply_2.difference(ply_1, ply_3, ply_4))
    print("Player Chach: \n")
    print(ply_3.difference(ply_2, ply_1, ply_4))
    print("Player Vzgo: \n")
    print(ply_4.difference(ply_2, ply_3, ply_1), "\n")
    all_shared_achiv = ply_1 | ply_2 | ply_3 | ply_4
    print("For each player, list the missing achievements to have them all\n")
    print(f"Player Alixe mising: {all_shared_achiv.difference(ply_1)}\n")
    print(f"Player Grno mising: {all_shared_achiv.difference(ply_2)}\n")
    print(f"Player Chach mising: {all_shared_achiv.difference(ply_3)}\n")
    print(f"Player Vzgo mising: {all_shared_achiv.difference(ply_4)}\n")
