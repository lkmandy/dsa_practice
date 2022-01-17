#!/bin/python3
# Exercise Link: https://bit.ly/3fAkKeS
# Given an array of integers, calculate the ratios of its elements that are 
# positive, negative, and zero. Print the decimal value of each fraction on 
# a new line with 6 places after the decimal.

from decimal import Decimal as d

def plusMinus(arr):
    status = {'positives': 0, 'negatives': 0, 'zeros': 0}
    
    for number in arr:
        if number > 0:
            status['positives'] += 1
        elif number < 0:
            status['negatives'] += 1
        else:
            status['zeros'] += 1

    
    arraySize = len(arr)
    
    for i in status:
        n = d(str(status[i]/arraySize)).quantize(d('.000000'))
        print(n)
           
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)