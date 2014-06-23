#!/usr/bin/env python3

from sys import argv

def testing(args):
    for i in range(len(args)):
        print("Number %d is %s" % (i, args[i]))
    print("")

testing(argv)

testing(["yo","whats","up"])

testing(["Ahead","of","the","game"])

testing(argv[0:2])

testing(argv[0::2])
