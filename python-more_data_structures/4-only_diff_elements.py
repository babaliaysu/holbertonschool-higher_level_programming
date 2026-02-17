#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ferq1 = set_1 - set_2
    ferq2 = set_2 - set_1
    return ferq1 | ferq2
