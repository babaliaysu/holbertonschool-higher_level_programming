#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    n = len(sys.argv) - 1
    for i in range(1,n+1):
        reqem = int(sys.argv[i])
        total+=reqem
    print("{:d}".format(total))
