#!/bin/python3

import os
import sys


def simpleArraySum(ar):
    result = 0
    for element in ar:
        result += element
    return result


def simpleArraySum2(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum2(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

