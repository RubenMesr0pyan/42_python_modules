import sys


def parser(input_line: list) -> dict:
    inventory: dict = {}
    for elem in input_line[1:]:
        parts = elem.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{elem}'")
            continue
        name = parts[0]
        quantity = parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(quantity)
        except ValueError:
            print(f"Quantity error for '{name}': "
                  f"invalid literal for int() with base 10: '{quantity}'")
            continue
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = parser(sys.argv)
    if len(inventory) > 0:
        print(f"Got inventory: {inventory}")
        item_list = list(inventory.keys())
        print(f"Item list: {item_list}")
        total_qty = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: {total_qty}")
        for item in inventory.keys():
            percentage = round((inventory[item] / total_qty) * 100, 1)
            print(f"Item {item} represents {percentage:.1f}%")
        most_abundant = ""
        most_qty = -1
        least_abundant = ""
        least = -1
        for item in inventory.keys():
            qty = inventory[item]
            if most_qty == -1 or qty > most_qty:
                most_abundant = item
                most_qty = qty
            if least == -1 or qty < least:
                least_abundant = item
                least = qty
        print(f"Item most abundant: {most_abundant} with quantity {most_qty}")
        print(f"Item least abundant: {least_abundant} with quantity {least}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
