#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max_value, min_value = arr[0], arr[0]
    total_sum = 0
    for value in arr:
        total_sum += value
        if max_value < value:
            max_value = value
        if min_value > value:
            min_value = value
    print(total_sum - max_value, total_sum - min_value)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
