from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    res = dark_spell_allowed_ingredients()
    for elem in res:
        if elem in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
