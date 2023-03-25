import sys
from collections import deque

sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
d = ["d", "l", "r", "u"]
res = 0


def solution(n, m, x, y, r, c, k):
    global flag
    global answer

    def dfs(a, b, route, direction):
        global flag
        global answer

        # 종료조건 : dfs 횟수 == k
        if len(route) == k:
            if board[a][b] == "e":
                flag = True
                answer = direction
            return

        # 탈출조건 : 현재위치 기준 남은 거리 > 주어진 남은 거리
        if abs(a - (r - 1)) + abs(b - (c - 1)) > k - len(route):
            return

        if flag:
            return

        # dfs 재귀
        else:
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if 0 <= na < n and 0 <= nb < m:
                    dfs(na, nb, route + [(na, nb)], direction + d[i])

    answer = ""
    board = [[0] * m for _ in range(n)]
    board[x - 1][y - 1] = "s"  # 출발지점
    board[r - 1][c - 1] = "e"  # 도착지점
    flag = False
    answer = ""

    # s(출발지점) 부터 bfs

    if (k - (abs(x - r) + abs(y - c))) < 0 or (k - (abs(x - r) + abs(y - c))) % 2 == 1:
        return "impossible"

    dfs(x - 1, y - 1, [], "")

    return answer
