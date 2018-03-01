'''
Given an array of integers, calculate which fraction of its elements are positive,
which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively.
Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains space-separated integers describing an array of numbers .

Output Format

You must print the following lines:

    A decimal representing of the fraction of positive numbers in the array compared to its size.
    A decimal representing of the fraction of negative numbers in the array compared to its size.
    A decimal representing of the fraction of zeroes in the array compared to its size.
'''

import sys


def plusMinus(arr):
    # Complete this function
    p, n, z = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1

    print("%.6f" % (p / len(arr)))
    print("%.6f" % (n / len(arr)))
    print("%.6f" % (z / len(arr)))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
