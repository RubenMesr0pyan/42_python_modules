#!/usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        increase: float
    ) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._increase = increase
        self._stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls(
            name="Unknown plant",
            height=0.0,
            days=0,
            increase=0.0
        )

    def show(self) -> None:
        self._stats._show_calls += 1
        print(
            f"{self._name.capitalize()}: "
            f"{self._height:.1f}cm, "
            f"{self._days} days old"
        )

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += self._increase

    def age(self) -> None:
        self._stats._age_calls += 1
        self._days += 1


class Flower(Plant):

    def __init__(
        self,
        color: str,
        name: str,
        height: float,
        days: int,
        increase: float
    ) -> None:
        super().__init__(name, height, days, increase)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(
                f"{self._name.capitalize()} "
                f"is blooming beautifully!"
            )
        else:
            print(
                f"{self._name.capitalize()} "
                f"has not bloomed yet"
            )


class Tree(Plant):

    def __init__(
        self,
        trunk_diameter: float,
        name: str,
        height: float,
        days: int,
        increase: float
    ) -> None:
        super().__init__(name, height, days, increase)
        self._trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self._name.capitalize()} now produces a shade "
            f"of {self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{self._trunk_diameter:.1f}cm"
        )


class Vegetable(Plant):

    def __init__(
        self,
        harvest_season: str,
        name: str,
        height: float,
        days: int,
        increase: float
    ) -> None:
        super().__init__(name, height, days, increase)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(
            f"Nutritional value: "
            f"{self._nutritional_value}"
        )


class Seed(Flower):

    def __init__(
        self,
        color: str,
        name: str,
        height: float,
        days: int,
        increase: float
    ) -> None:
        super().__init__(color, name, height, days, increase)
        self._seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds_count}")


def display_statistics(plant: Plant) -> None:
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    rose = Flower("red", "rose", 15.0, 10, 8.0)
    rose.show()

    print(f"[statistics for {rose._name.capitalize()}]")
    display_statistics(rose)

    print(f"[asking the {rose._name} to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()

    print(f"[statistics for {rose._name.capitalize()}]")
    display_statistics(rose)

    print("=== Tree")
    oak = Tree(5.0, "oak", 200.0, 365, 1.0)
    oak.show()

    print(f"[statistics for {oak._name.capitalize()}]")
    display_statistics(oak)

    print(f"[asking the {oak._name} to produce shade]")
    oak.produce_shade()

    print(f"[statistics for {oak._name.capitalize()}]")
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("yellow", "sunflower", 80.0, 45, 30.0)
    sunflower.show()

    print(f"[make {sunflower._name} grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()

    print(
        f"[statistics for "
        f"{sunflower._name.capitalize()}]"
    )
    display_statistics(sunflower)

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()

    print(f"[statistics for {anon._name.capitalize()}]")
    display_statistics(anon)
