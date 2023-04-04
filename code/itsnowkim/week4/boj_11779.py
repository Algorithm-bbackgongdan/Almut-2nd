import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# 경로를 담는 배열
route = [0] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y,z))

S,E = map(int, input().split())

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 거리는 0, 맨 뒤는 경로를 담는 리스트
    heapq.heappush(q, (0, start))
    distance[start] = 0
    route[start] = [start]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

                route[i[0]] = route[now] + [i[0]]
                heapq.heappush(q,(cost, i[0]))

dijkstra(S)

print(distance[E])
print(len(route[E]))
print(' '.join(str(e) for e in route[E]))