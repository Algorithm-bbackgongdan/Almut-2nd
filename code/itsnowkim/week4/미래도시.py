INF = int(1e9)

# 노드의 개수 및 간선의 개수
n, m = map(int, input().split())
# 2차원 그래프 만들고, 값 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X, 최종 목적지 K
x,k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 진행
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1
if distance >= INF:
    print('-1')
# 도달할 수 있다면, 최단 거리
else:
    print(distance)