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


class Flower(Plant):
    def __init__(self, color: str, name: str, height: float, days: int,
                 increase: float) -> None:
        super().__init__(name, height, days, increase)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if (self._is_blooming):
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, trunk_diameter: float, name: str, height: float,
                 days: int, increase: float) -> None:
        super().__init__(name, height, days, increase)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name.capitalize()} now produces a shade"
              f" of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, harvest_season: str,
                 name: str, height: float, days: int, increase: float) -> None:
        super().__init__(name, height, days, increase)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("red", "rose", 15.0, 10, 0.8)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n")
    print("=== Tree")
    car = Tree(5.0, "Oak", 200.0, 365, 1.0)
    car.show()
    print("[asking the oak to produce shade]")
    car.produce_shade()
    print("\n")
    print("=== Vegetable")
    tomato = Vegetable("April", "Tomato", 5.0, 10, 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
