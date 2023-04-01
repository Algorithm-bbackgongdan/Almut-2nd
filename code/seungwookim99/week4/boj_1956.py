# 운동
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(v + 1):
    graph[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(v + 1):
    for i in range(v + 1):
        for j in range(v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_value = INF
for i in range(1, v):
    for j in range(i + 1, v + 1):
        min_value = min(min_value, graph[i][j] + graph[j][i])
if min_value == INF:
    min_value = -1
print(min_value)
