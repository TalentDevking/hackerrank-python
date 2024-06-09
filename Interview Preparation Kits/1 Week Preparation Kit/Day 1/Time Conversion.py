#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[8] == 'A':
        if s[0] == '1' and s[1] == '2':
            return '00' + s[2:8]
        return s[:8]
    if s[0] == '1' and s[1] == '2':
        return s[:8]
    return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
