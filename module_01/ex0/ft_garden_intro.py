def display_plant() -> None:
    name: str = "Rose"
    age_days: int = 30
    height_cm: int = 25

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name.capitalize()}")
    print(f"Height: {height_cm}cm")
    print(f"Age: {age_days} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    display_plant()
