#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argumenrs:".format(x))
    else:
        print("{} arguments:".format(x))
    for y in range(x):
        print("{}: {:s}".format(y + 1, argv[y + 1]))
