import sys
from collections import defaultdict
from heapq import heappush, heappop


def makeGraph(edges):
    graph = defaultdict(list)

    for v1, v2, cost in edges:
        graph[v1].append((v2, cost))

    return graph


def solution(n, m, edges, src, dest):
    graph = makeGraph(edges)
    dist = [float("inf")] * (n + 1)
    minHeap = [(0, src)]  # 출발점으로 초기화
    visited = set([])
    path = [[] for _ in range(n + 1)]  # path[i]: 출발점이 src, 도착점이 i인 최단 경로
    path[src] = [src]

    # dist 초기화
    dist[src] = 0

    while minHeap:
        cost, vertex = heappop(minHeap)

        if vertex in visited:
            continue

        visited.add(vertex)

        for adjacent, cost in graph[vertex]:
            if adjacent in visited:
                continue

            if dist[adjacent] > dist[vertex] + cost:
                dist[adjacent] = dist[vertex] + cost
                path[adjacent] = path[vertex] + [adjacent]
                heappush(minHeap, (dist[adjacent], adjacent))

    return dist[dest], path[dest]


n = int(input())
m = int(input())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
src, dest = map(int, sys.stdin.readline().split())

dist, path = solution(n=n, m=m, edges=edges, src=src, dest=dest)

print(dist)
print(len(path))
print(" ".join(map(str, path)))
