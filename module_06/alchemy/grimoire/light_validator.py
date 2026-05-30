def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    res = light_spell_allowed_ingredients()
    for elem in res:
        if elem in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
