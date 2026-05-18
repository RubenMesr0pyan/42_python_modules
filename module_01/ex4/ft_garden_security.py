#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int,
                 increase: float) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._increase: float = increase
        self._days: int = 0
        self.set_height(height)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name.capitalize()}:"
              f" {round(self._height, 2)}cm, {self._days} days old")

    def grow(self) -> None:
        self._height += self._increase

    def age(self) -> None:
        self._days += 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name.capitalize()}:"
                  " Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    flower1: Plant = Plant("rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    flower1.show()
    flower1.set_height(25.0)
    print(f"Height updated: {int(flower1.get_height())}cm")
    flower1.set_age(30)
    print(f"Age updated: {flower1.get_age()} days")
    flower1.set_height(-7.0)
    flower1.set_age(-7)
    print("Current state: ", end="")
    flower1.show()
