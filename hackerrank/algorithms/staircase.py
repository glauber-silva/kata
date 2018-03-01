"""
Consider a staircase of size n = 4:
   #
  ##
 ###
####

Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size using # symbols and spaces.

Note: The last line must have spaces in it.
"""
#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

