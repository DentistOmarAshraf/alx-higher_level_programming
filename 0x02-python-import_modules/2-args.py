#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    if ac - 1 == 0:
        print("{:d} arguments.".format(ac - 1))
    elif ac - 1 == 1:
        print("{:d} argument:".format(ac - 1))
    else:
        print("{:d} arguments:".format(ac - 1))
    for i in range(1, ac):
        print("{:d}: {:s}".format(i, argv[i]))
