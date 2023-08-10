#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    str1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    str2 = "Unknown operator. Available operators: +, -, * and /"
    num = (len(sys.argv))
if num != 4:
    print("{}".formst(str1))
    exit(1)
    if sys.argv[2] not in "+-*/":
        print("{}".format(str2))
        exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            result = calculator_1.add(a, b)
            if sys.argv[2] == "-":
                result + calculator_1.sub(a, b)
                if sys.argv[2] == "*":
                    result = calculator_1mul(a, b)
                    if sys.argv[2] == "/":
                        result = calculator_1.div(a, b)

print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, result))
