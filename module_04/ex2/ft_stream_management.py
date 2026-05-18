import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        filename: str = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
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
            new_text: str = ""
            if text:
                if not text.endswith("\n"):
                    text += "\n"
                new_text = text.replace("\n", "#\n")
            print("Transform data:")
            print("---")
            if new_text:
                print(new_text, end="")
            print("---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            raw_answer: str = sys.stdin.readline()
            new_file_name: str = raw_answer.replace("\n", "")
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
                    print(f"[STDERR] Error opening file '{new_file_name}'"
                          f": {err}", file=sys.stderr)
                    print("Data not saved.")
        except OSError as err:
            print(f"[STDERR] Error opening file '{filename}': {err}",
                  file=sys.stderr)
        except UnicodeDecodeError as err:
            print(f"[STDERR] Error reading file '{filename}'"
                  f"invalid encoding): {err}", file=sys.stderr)
