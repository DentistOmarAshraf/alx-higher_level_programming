#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    print("{:d} argument:".format(ac - 1))
    if ac > 1:
        for i in range(1, ac):
            print("{:d}: {:s}".format(i, argv[i]))
