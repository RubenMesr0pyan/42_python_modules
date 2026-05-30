from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    res = validate_ingredients(ingredients)
    if "VALID" in res:
        return (f"Spell recorded: {spell_name} ({res})")
    return (f"Spell rejected: {spell_name} ({res})")
