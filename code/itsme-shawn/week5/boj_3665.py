import sys
from collections import deque
from itertools import combinations

read = sys.stdin.readline

tc = int(read())

for _ in range(tc):
    n = int(read())

    graph = [[0] * (n + 1) for _ in range(n + 1)]  # 인접그래프
    degree = [0] * (n + 1)  # 진입차수
    deq = deque()

    last_ranks = list(map(int, read().split()))

    for a, b in combinations(last_ranks, 2):
        graph[a][b] = 1
        degree[b] += 1

    m = int(read())

    for _ in range(m):
        a, b = map(int, read().split())
        if graph[a][b]:
            graph[a][b] = 0
            degree[b] -= 1
            graph[b][a] = 1
            degree[a] += 1

        elif graph[b][a]:
            graph[b][a] = 0
            degree[a] -= 1
            graph[a][b] = 1
            degree[b] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            deq.append(i)

    res = []

    while deq:
        x = deq.popleft()
        res.append(x)
        for i in range(1, n + 1):
            if graph[x][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    deq.append(i)

    if len(res) == n:
        print(*res)
    else:
        print("IMPOSSIBLE")
