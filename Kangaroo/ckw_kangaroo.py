#두 마리의 캥거루가 수직선상에서 양의 방향으로 점프하려고 대기중.
#캥거루 1은 x1에서 시작해 v1미터씩 나아간다.
#캥거루 2는 x2에서 시작해 v2미터씩 나아간다.

#두 캥거루가 같은 횟수동안 점프한 결과 한 지점에서 만날 수 있는지 구하라(YES or NO)
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    jump_x1 = 0
    jump_x2 = 0
    
    while jump_x1 < 10000:
        if x1 < x2 and v1 < v2:
            return 'NO'

        if x1 != x2:
            jump_x1 += 1
            jump_x2 += 1
            
            x1 += v1
            x2 += v2
            continue
        elif x1 == x2:
            if jump_x1 == jump_x2:
                return 'YES'
            else:
                continue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')
    fptr.close()



