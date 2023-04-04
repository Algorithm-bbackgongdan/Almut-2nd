import sys

INF = int(1e9)

# 입력 받기
v, e = map(int, sys.stdin.readline().split())
graph = [[INF] * (v+1) for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 플로이드 와샬 알고리즘 수행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최소 사이클 길이 찾기
answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

# 출력
if answer == INF:
    print("-1")
else:
    print(answer)
