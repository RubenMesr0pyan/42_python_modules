import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        filename: str = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        try:
            fil: typing.TextIO = open(filename)
            text: str = fil.read()
            print("---")
            if text:
                print(text, end="" if text.endswith("\n") else "\n")
            print("---")
            fil.close()
            print(f"File '{filename}' closed.")
        except OSError as err:
            print(f"Error opening file '{filename}': {err}")
        except UnicodeDecodeError as err:
            print(f"Error reading file '{filename}' (invalid encoding): {err}")
