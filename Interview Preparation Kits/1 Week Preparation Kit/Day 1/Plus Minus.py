#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    plus, minus, zero = 0, 0, 0
    for item in arr:
        if item > 0:
            plus += 1
        elif item == 0:
            zero += 1
        else:
            minus += 1
    print(plus / total)
    print(minus / total)
    print(zero / total)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
