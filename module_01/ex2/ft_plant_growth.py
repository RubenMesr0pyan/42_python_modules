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

    rose: Plant = Plant("rose", 25, 30)
    height_at_start = rose.height
    for i in range(1, 8):
        rose.age()
        rose.grow()
        print(f"=== Day {i} ===")
        rose.show()
    print(f"Growth this week: {rose.height - height_at_start:.1f}cm")
