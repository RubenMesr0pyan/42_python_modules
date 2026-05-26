from ex0.factory import FlameFactory, AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def tournament(opponents: list):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = []
    for fact, strat in opponents:
        fighters.append((fact.create_base(), strat))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            f1, s1 = fighters[i]
            f2, s2 = fighters[j]
            print("\n* Battle *")
            print(f"{f1.describe()}")
            print("vs.")
            print(f"{f2.describe()}")
            print("now fight!")
            try:
                if not s1.is_valid(f1):
                    raise Exception(f"Invalid Creature '{f1.name}' "
                                    "for this strategy")
                if not s2.is_valid(f2):
                    raise Exception(f"Invalid Creature '{f2.name}' "
                                    "for this strategy")
                s1.act(f1)
                s2.act(f2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    tournament([(FlameFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())])

    print("\nTournament 1 (error)")
    tournament([(FlameFactory(), AggressiveStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())])

    print("\nTournament 2 (multiple)")
    tournament([(AquaFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy()),
                (TransformCreatureFactory(), AggressiveStrategy())])
