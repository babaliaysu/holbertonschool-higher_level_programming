#!/usr/bin/python3
def remove_char_at(str, n):
    metn = ""
    for i in range(len(str)):
        if i != n:
            metn = metn + str[i]
    return metn
