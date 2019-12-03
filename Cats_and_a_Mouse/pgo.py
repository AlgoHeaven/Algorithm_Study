#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    
    l = []

    if abs(z-x) == abs(z-y):
        l.append("Mouse C")

    else:
        if abs(z-x) < abs(z-y):
            l.append("Cat A")
        else:
            l.append("Cat B")

    # 람다 시도 했는데, 람다 잘 몰라서 안됨..;;
    # print(list(map(lambda i: "Cat A" if abs(z-x) < abs(z-y) else "Cat B" if abs(z-x) > abs(z-y) else "Mouse C", x,y,z)))

    print(l)
    return ' '.join(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
