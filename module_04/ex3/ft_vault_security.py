def secure_archive(filename: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data: str = f.read()
            return (True, data)
        elif action == "write":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Unknown action: '{action}'")
    except OSError as err:
        return (False, str(err))
    except UnicodeDecodeError as err:
        return (False, f"Decode error: {err}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    test_file = "ancient_fragment.txt"
    secure_archive(test_file, "write", "[FRAGMENT 001] Digital preservation"
                   "protocols established 2087\n[FRAGMENT 002] Knowledge must "
                   "survive the entropy wars\n[FRAGMENT 003] Every byte saved "
                   "is a victory against oblivion\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive(test_file, "read"))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_test_file.txt", "write", "Content successfully "
                         "written to file"))
