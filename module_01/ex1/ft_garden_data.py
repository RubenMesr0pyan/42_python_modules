#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}:"
              f" {self.height}cm, {self.age} days old")


if __name__ == "__main__":

    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 80, 45)
    cactus: Plant = Plant("cactus", 15, 120)
    rose.show()
    sunflower.show()
    cactus.show()
