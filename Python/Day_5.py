#!/bin/python3
#Loops

import math
import os
import random
import re
import sys

def multiplication(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

if __name__ == '__main__':
    n = int(input().strip())
    multiplication(n)
