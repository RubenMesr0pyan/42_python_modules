from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.cap import HealCapability
from ex1.trans_cap import TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        c = creature
        if not isinstance(c, TransformCapability):
            raise Exception(f"Invalid Creature '{c.name}'"
                            f" for this aggressive strategy")
        print(c.transform())
        print(c.attack())
        print(c.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        c = creature
        if not isinstance(c, HealCapability):
            raise Exception(f"Invalid Creature '{c.name}'"
                            f"for this defensive strategy")
        print(c.attack())
        print(c.heal())
