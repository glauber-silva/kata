#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    diag1, diag2, diff = 0,0,0
    for i in range(1, len(a)+1):
        diag1+= a[i - 1][i - 1]
        print("DIAG 1 : ", a[i - 1][i - 1])
        diag2+= a[i-1][-i]
        print("DIAG 2 : ", a[i-1][-i])

    return abs(diag1-diag2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
