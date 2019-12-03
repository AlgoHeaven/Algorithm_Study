#1. 평균
def Mean(n, x):
    denominator = n
    numerator = 0

    for i in range(len(x)):
        numerator += x[i]

    return numerator / denominator

#2. 중앙값
def Median(n, x):
    #먼저 오름차순 정렬
    for i in range(len(x)-1):
        min_idx = i
        for j in range(i, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    
    if n%2 == 0:
        return (x[int(len(x)/2) - 1] + x[int(len(x)/2)]) / 2
    else:
        return x[int(len(x)/2)]

#3. 최빈값
def Mode(x):
    n = len(x)
    min_value = x[0]
    for i in range(1, n):
        if min_value > x[i]:
            min_value = x[i]


    for i in range(len(x)):
        if x.count(x[i]) == x.count(x[0]):  #모든 원소가 같은 빈도일 시 원소 중 최소값 반환
            return min_value
        else:   #가장 많은 빈도의 원소가 존재하는 경우
            return #정현, 근오형의 고견을 구합니다...


n = 10
x = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

print(Mean(n, x))
print(Median(n, x))
print(Mode(x))