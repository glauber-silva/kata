#!/bin/python3
"""
Colleen is having a birthday! She will have a cake with one candle
for each year of her age. When she blows out the candles, she’ll only be able to blow out the tallest ones.

Find and print the number of candles she can successfully blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake.
The second line contains space-separated integers, where each integer describes the height of candle .
"""
import sys


def search_greater (arr):
    greater = arr[0]
    greater_index = 0
    for i in range(1, len(arr)):
        if arr[i] > greater:
            greater = arr[i]
            greater_index = i
    return greater_index


def order(arr):
    new_arr = []
    for i in range(len(arr)):
        greater = search_greater(arr)
        new_arr.append(arr.pop(greater))
    print('new array', new_arr)
    return new_arr


def birthday_cake_candles(n, arr):
    # Complete this function
    ordered_arr = order(arr)
    candles = 1
    for i in range(len(ordered_arr)):
        if ordered_arr[i] == ordered_arr[i+1]:
            candles += 1
        else:
            return candles
    return candles

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthday_cake_candles(n, ar)
print(result)