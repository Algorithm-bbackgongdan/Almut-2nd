# 실패 후 구글링 => 나중에 다시 풀어보기

import sys
from collections import deque

read = sys.stdin.readline

r, c = map(int, read().split())

board = [[0 for _ in range(c)] for _ in range(r)]
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(r)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))  #
edges = []  # 간선 (다리)
island = []  # 섬이 될 수 있는 좌표 (x좌표, y좌표, 섬번호)
visited = [[False for _ in range(c)] for _ in range(r)]


def isin(y, x):
    if -1 < y < r and -1 < x < c:
        return True
    return False


# bfs 로 섬 하나 만들기
def bfs(visited, sy, sx, k):
    q = deque()
    q.append((sy, sx))

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if not isin(ny, nx):
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    board[ny][nx] = k
                    q.append((ny, nx))
                    island.append((ny, nx, k))


# 전체 보드판에서 섬 생성
# 전체 보드 순회하면서 조건에 맞을때만 bfs
def make_board():
    visited = [[False for _ in range(c)] for _ in range(r)]
    k = 1
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                board[i][j] = k
                island.append((i, j, k))
                bfs(visited, i, j, k)  # 섬 하나 생성
                k += 1

    return k


# 섬 간 다리 만들기
def make_bridge(sy, sx, k):
    q = deque()

    for dy, dx in d:
        q.append((sy, sx))
        visited = [[False for _ in range(c)] for _ in range(r)]
        visited[sy][sx] = True
        dist = [[0 for _ in range(c)] for _ in range(r)]  # 다리 길이

        while q:
            y, x = q.popleft()

            # 한 방향으로만 직진
            ny = y + dy
            nx = x + dx

            if not isin(ny, nx):
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

                elif board[ny][nx] != k and dist[y][x] >= 2:
                    edges.append((dist[y][x], k, board[ny][nx]))


# union-find
def find_parent(a):
    if parent[a] < 0:
        return a
    parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return False
    parent[b] = a
    return True


n = make_board() - 1
for y, x, k in island:
    make_bridge(y, x, k)
parent = [-1 for _ in range(n + 1)]


edges.sort()
total, cnt = 0, 0

for w, a, b in edges:
    if union_parent(a, b):
        total += w
        cnt += 1
        if cnt == n - 1:
            break
if cnt == n - 1:
    print(total)
else:
    print(-1)
