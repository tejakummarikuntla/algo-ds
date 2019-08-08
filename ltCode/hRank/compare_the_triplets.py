#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = 0
    score_b = 0

    for i in range(len(a)):

        if a[i] > b[i]:
            score_a = score_a + 1
        if a[i] < b[i]:
            score_b = score_b + 1
    return [score_a, score_b]


if __name__ == '__main__':
    in_a = [int(x) for x in input().split()]
    in_b = [int(x) for x in input().split()]

    res_arr = compareTriplets(in_a, in_b)
    print(res_arr[0], res_arr[1])

