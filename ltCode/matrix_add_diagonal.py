#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_diag_sum = 0
    second_diag_sum = 0
    for i in range(len(arr)):
        first_diag_sum = first_diag_sum + arr[i][i]
        second_diag_sum = second_diag_sum + arr[i][(len(arr)-1)-i]
    return abs(first_diag_sum - second_diag_sum)

if __name__ == '__main__':
    input_n = int(input())
    arr = []
    for i in range(input_n):
        temp_arr = [int(x) for x in input().split()]
        arr.append(temp_arr)
    print(diagonalDifference(arr))





