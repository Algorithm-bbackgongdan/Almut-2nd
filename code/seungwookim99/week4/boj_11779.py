# 최소비용 구하기 2
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
paths = [""] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, str(start)))
    distance[start] = 0
    paths[start] = str(start)
    while q:
        dist, now, path = heapq.heappop(q)
        if dist > distance[now]:  # 이미 방문함
            continue
        for i in graph[now]:  # 인접 간선 체크
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                paths[i[0]] = path + " " + str(i[0])
                heapq.heappush(q, (cost, i[0], paths[i[0]]))
    return


dijkstra(start)

print(distance[end])
print(len(paths[end].split(" ")))
print(paths[end])
