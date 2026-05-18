#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name.capitalize()}:"
              f" {round(self.height, 2)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    garden: list[Plant] = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in garden:
        print("Created: ", end="")
        i.show()
