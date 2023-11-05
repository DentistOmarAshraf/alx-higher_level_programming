#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    if ac == 1:
        print("{:d}".format(0))
    else:
        res = 0
        for i in range(1, ac):
            res += int(argv[i])
        print("{:s}".format(str(res)))
