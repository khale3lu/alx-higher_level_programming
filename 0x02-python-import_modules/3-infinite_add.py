#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv:
            result += int(arg)
            print(result)
