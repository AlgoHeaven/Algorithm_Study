def mean(N, X, W):
    numerator = 0
    denominator = 0
    for i in range(len(X)):
        numerator += X[i] * W[i]
        denominator += W[i]

    mode = numerator / denominator

    return mode

N = 5
X = [10, 40, 30, 50, 20]
W = [1, 2, 3, 4, 5]

print(mean(N, X, W))