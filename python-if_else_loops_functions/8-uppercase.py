#!/usr/bin/python3
def uppercase(str):
    for i in str:
        kodu = ord(i)
        if kodu >= 97 and kodu <= 122:
            kodu = kodu - 32
        print("{:c}".format(kodu), end="")
    print("")
