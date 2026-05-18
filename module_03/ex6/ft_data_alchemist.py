import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    list_of_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {list_of_players}")
    player_name_cap = [name.capitalize() for name in list_of_players]
    print(f"New list with all names capitalized: {player_name_cap}")
    only_upper = [name for name in list_of_players if name.istitle()]
    print(f"New list of capitalized names only: {only_upper}")
    scoredict = {name: random.randint(1, 1000) for name in player_name_cap}
    print(f"Score dict: {scoredict}")
    score_sum = sum(scoredict.values())
    average_score = round(score_sum / len(scoredict), 2)
    print(f"Score average is {average_score}")
    high_scores = {
        name: score for name, score in scoredict.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")
