from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(fact1, fact2):
    print("Testing battle")
    fighter1 = fact1.create_base()
    fighter2 = fact2.create_base()
    print(fighter1.describe())
    print("vs.")
    print(fighter2.describe())
    print("fight!")
    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    test_factory(flame_fact)
    test_factory(aqua_fact)
    test_battle(flame_fact, aqua_fact)
