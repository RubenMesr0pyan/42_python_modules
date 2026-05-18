#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    tmp: int = int(temp_str)
    if tmp >= 0 and tmp <= 40:
        return tmp
    elif tmp > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    in1 = "25"
    print(f"Input data is '{in1}'")
    try:
        print(f"Temperature is now {input_temperature(in1)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    in2 = "abc"
    print(f"Input data is '{in2}'")
    try:
        print(f"Temperature is now {input_temperature(in2)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    in3 = "100"
    print(f"Input data is '{in3}'")
    try:
        print(f"Temperature is now {input_temperature(in3)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    in4 = "-50"
    print(f"Input data is '{in4}'")
    try:
        print(f"Temperature is now {input_temperature(in4)}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
