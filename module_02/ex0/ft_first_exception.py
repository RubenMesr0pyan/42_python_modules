#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
