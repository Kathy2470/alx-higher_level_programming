#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Print sorted names from directory
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Print only names that do not start with __
    for name in sorted(names):
        print(name)
