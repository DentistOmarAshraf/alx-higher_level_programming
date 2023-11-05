#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    import calculator_1
    opr = ["+", "/", "*", "-"]
    func = []
    for i in dir(calculator_1):
        if i[0:2] == "__":
            continue
        func.append(i)
    for i in range(len(opr)):
        if (argv[2] == opr[i]):
            f_name = func[i]
            if f_name == "div" and int(argv[3]) == 0:
                print("Error: can't divide on zero")
                exit(1)
            import importlib
            opt = getattr(calculator_1, f_name)
            res = opt(int(argv[1]), int(argv[3]))
    print("{:s} {:s} {:s} = {:d}".format(argv[1], argv[2], argv[3], res))
    exit(0)
    if i == len(opr) - 1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
