import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = int(1e9)

# input
n, m = map(int, input().split())
islands = [set() for _ in range(8)]  # 해안가 좌표 저장
B = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
bridges = [[INF] * 8 for _ in range(8)]
num = 2


def inside_boundary(y, x):
    return (0 <= y < n) and (0 <= x < m)


def bfs(y, x):
    q = deque([])
    q.append((y, x))
    visited[y][x] = True
    B[y][x] = num
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inside_boundary(ny, nx) and B[ny][nx] == 1 and not visited[ny][nx]:
                q.append((ny, nx))
                B[ny][nx] = num
                visited[ny][nx] = True
            elif inside_boundary(ny, nx) and B[ny][nx] == 0:  # 인접한 곳이 바다라면 해안가
                islands[num].add((y, x))
    return


def bridge_from_a_to_b(a, b, colwise):
    (ay, ax), (by, bx) = a, b
    cnt = 0
    if colwise:  # 세로 다리
        for i in range(1, (by - ay)):
            ay += 1
            if not inside_boundary(ay, ax) or B[ay][ax] != 0:
                return INF
            cnt += 1
    else:  # 가로 다리
        for i in range(1, (bx - ax)):
            ax += 1
            if not inside_boundary(ay, ax) or B[ay][ax] != 0:
                return INF
            cnt += 1
    return cnt


def get_all_bridge(a, b):
    a_beach, b_beach = list(islands[a]), list(islands[b])

    for ay, ax in a_beach:
        for by, bx in b_beach:
            if ay != by and ax != bx:
                continue
            elif ay == by:  # 가로 방향 일치
                if ax < bx:
                    bridge = bridge_from_a_to_b((ay, ax), (by, bx), False)
                else:
                    bridge = bridge_from_a_to_b((by, bx), (ay, ax), False)
            elif ax == bx:  # 세로 방향 일치
                if ay < by:
                    bridge = bridge_from_a_to_b((ay, ax), (by, bx), True)
                else:
                    bridge = bridge_from_a_to_b((by, bx), (ay, ax), True)

            # bridge 길이 갱신
            if bridge > 1:
                bridges[a][b] = min(bridges[a][b], bridge)
                bridges[b][a] = min(bridges[b][a], bridge)
    return


# start
for i in range(n):
    for j in range(m):
        if B[i][j] == 0:
            continue
        if B[i][j] == 1:
            bfs(i, j)
            num += 1

# 임의의 두 섬을 잇는 최소비용의 다리 구하기
for a, b in combinations([x for x in range(2, num)], 2):
    get_all_bridge(a, b)

# kruskal 알고리즘 으로 최소 신장 트리 찾기
parents = [0] * 8
for i in range(8):
    parents[i] = i

edges = []
for i in range(2, num):
    for j in range(2, num):
        if i < j and bridges[i][j] != INF:
            edges.append((bridges[i][j], i, j))

edges.sort()


def find_parent(i):
    if parents[i] != i:
        parents[i] = find_parent(parents[i])
    return parents[i]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return


result = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

parent_node = find_parent(2)
for i in range(3, num):
    if find_parent(i) != parent_node:
        result = -1

print(result)
