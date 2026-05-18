def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    formated = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{formated} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{formated} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{formated} seeds: {quantity} square meters")
    else:
        print("Unknown unit type")
