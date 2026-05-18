import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")
        try:
            fil: typing.TextIO = open(filename)
            text = fil.read()
            print("---")
            if text:
                print(text, end="" if text.endswith("\n") else "\n")
            print("---")
            fil.close()
            print(f"File '{filename}' closed.")
            new_text = ""
            if text:
                if not text.endswith("\n"):
                    text += "\n"
                new_text = text.replace("\n", "#\n")
            print("Transform data:")
            print("---")
            if new_text:
                print(new_text, end="")
            print("---")
            new_file_name = input("Enter new file name (or empty): ")
            if not new_file_name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")
                try:
                    out_fil: typing.TextIO = open(new_file_name, "w")
                    out_fil.write(new_text)
                    out_fil.close()
                    print(f"Data saved in file '{new_file_name}'.")
                except OSError as err:
                    print(f"Error saving file: {err}")
        except OSError as err:
            print(f"Error opening file '{filename}': {err}")
        except UnicodeDecodeError as err:
            print(f"Error reading file '{filename}'",
                  f" (invalid encoding): {err}")
