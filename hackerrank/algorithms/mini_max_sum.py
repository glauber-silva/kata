# !/bin/python3
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
 Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

Each integer is in the inclusive range [1 . . . 10^9] .

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by
summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:

    If we sum everything except , our sum is .
    If we sum everything except , our sum is .
    If we sum everything except , our sum is .
    If we sum everything except , our sum is .
    If we sum everything except , our sum is .


"""

import sys
def miniMaxSum(arr):
    # Complete this function
    x = sum(arr)
    print(x-(max(arr)), x-(min(arr)))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
