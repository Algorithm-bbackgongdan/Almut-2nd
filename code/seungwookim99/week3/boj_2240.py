import sys

T, W = map(int, sys.stdin.readline().rstrip().split(' '))
Jadu = [[0, 0] for _ in range(T + 1)]
for i in range(T):
    tree = int(sys.stdin.readline().rstrip())
    Jadu[i + 1][tree - 1] = 1

# (T + 1) * (W + 1) 2차원 리스트
DP = [[0] * (W + 1) for _ in range(T + 1)]

# 초기화
for w in range(W + 1):
    DP[T][w] = Jadu[T][w % 2]

for t in range(T - 1, -1, -1):
    for w in range(W, -1, -1):
        DP[t][w] = Jadu[t][w % 2] + max(DP[t + 1][w:])

print(DP[0][0])