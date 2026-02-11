#!/usr/bin/python3
# ASCII əlifbasını çap edən proqram (q və e olmadan)

for i in range(97, 123):
    if chr(i) not in ("q", "e"):
        print("{}".format(chr(i)), end="")
