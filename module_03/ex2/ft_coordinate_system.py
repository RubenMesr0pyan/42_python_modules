import math


def get_player_pos() -> tuple:
    while True:
        input_cords: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        cords: list = input_cords.split(",")
        if len(cords) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(cords[0])
        except ValueError as e:
            print(f"Error on parameter '{cords[0]}': {e}")
            continue
        try:
            y = float(cords[1])
        except ValueError as e:
            print(f"Error on parameter '{cords[1]}': {e}")
            continue
        try:
            z = float(cords[2])
        except ValueError as e:
            print(f"Error on parameter '{cords[2]}': {e}")
            continue
        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    first_cords: tuple = get_player_pos()
    X, Y, Z = first_cords
    print(f"It includes: X={X}, Y={Y}, Z={Z}")
    dis_to_center = (X**2 + Y**2 + Z**2)**0.5
    print(f"Distance to center: {dis_to_center}")
    print("Get a second set of coordinates")
    second_cords: tuple = get_player_pos()
    X2, Y2, Z2 = second_cords
    dis_bt2 = math.sqrt((X2 - X)**2 + (Y2 - Y)**2 + (Z2 - Z)**2)
    print(f"Distance between the 2 sets of coordinates: {dis_bt2}")
