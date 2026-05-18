#!/usr/bin/env python3
class PlantError(Exception):
    def __init__(self, message: str = "Invalid plant name"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(p1: str, p2: str, p3: str) -> None:
    print("Opening watering system")
    try:
        water_plant(p1)
        water_plant(p2)
        water_plant(p3)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "lettuce", "Carrots")
    print()
    print("Cleanup always happens, even with errors!")
