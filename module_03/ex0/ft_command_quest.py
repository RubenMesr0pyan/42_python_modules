import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in sys.argv[]:
            print(f"Argument {i}: {sys.argv[i]}")
print(f"Total arguments: {len(sys.argv)}")
