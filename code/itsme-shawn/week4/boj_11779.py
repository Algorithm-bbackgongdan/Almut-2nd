import heapq as hq
import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = dict()

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b, w = map(int, read().split())
    graph[a].append((b, w))

start, end = map(int, read().split())

MAX = int(1e9)
distance = [MAX] * (n + 1)
path_node = [0] * (n + 1)


def dijkstra(start):
    q = []  # (시작정점으로부터의 거리, 노드번호) 를 저장할 최소 힙
    # pop 시 거리가 작은 순으로 pop 됨

    # 시작점 세팅
    distance[start] = 0  # 시작점의 거리는 0
    hq.heappush(q, (0, start))  # 힙에 시작점 push

    while q:
        dist, cur = hq.heappop(q)  # 최소 힙에서 (거리,노드번호) pop

        # 현재 노드가 처리되지 않은 노드여야함
        if dist <= distance[cur]:  # pop한 노드의 거리 <= 최단거리 테이블 상에 기록된 거리
            for i in graph[cur]:  # i[0] : 인접노드번호, i[1] : 거리
                cost = dist + i[1]  # 현재노드를 거쳐갈 경우의 거리 계산
                if cost < distance[i[0]]:  # 새롭게 계산한 거리가 작을때만 갱신
                    distance[i[0]] = cost  # 거리테이블 갱신
                    path_node[i[0]] = cur  # 이전노드 정보 저장
                    hq.heappush(q, (cost, i[0]))  # 갱신 노드의 거리와 노드번호를 heap 에 push


dijkstra(start)


print(distance[end])


path = [end]
now = end
while now != start:  # path_node를 역추적해나가면서 경로 얻음
    now = path_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(" ".join(map(str, path)))
