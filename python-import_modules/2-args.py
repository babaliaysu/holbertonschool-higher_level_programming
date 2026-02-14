#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Arqumentlərin sayını tapırıq (skriptin adını çıxmaqla)
    n = len(sys.argv) - 1

    # Birinci sətri çap edirik
    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))

    # Hər bir arqumenti mövqeyi ilə çap edirik
    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
