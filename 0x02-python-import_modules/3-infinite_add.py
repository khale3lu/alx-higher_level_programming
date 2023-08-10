#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ans = 0
    num = (len(sys.argv) - 1)
    for index in range(1, num + 1):
        ans += int(sys.argv[index])
        print("{:d}".format(ans))
