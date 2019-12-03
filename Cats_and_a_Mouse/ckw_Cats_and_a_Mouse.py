# (가정)
# 가정 1)쥐는 움직이지 않고 고양이는 일정한 속도로 움직인다.
# 가정 2)단, 고양이들이 동시에 쥐를 잡는 경우에 쥐는 도망칠 수 있다.
# 가정 3)x, y -> 고양이 A, B   //   z -> 쥐 C

# (목표)
# 가장 먼저 쥐를 잡게 되는 고양이를 구하기.

# (출력예시)
# A와 B 중 먼저 C를 잡는 고양이를 print.
# 단, 동시에 쥐를 잡으면 C를 print.
##################################################################
import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    answer = []

    if abs(x-z) > abs(y-z):
        answer.append('Cat B')
    elif abs(x-z) < abs(y-z):
        answer.append('Cat A')        
    elif abs(x-z) == abs(y-z):
        answer.append('Mouse C')
    

    return answer[0]
    

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
