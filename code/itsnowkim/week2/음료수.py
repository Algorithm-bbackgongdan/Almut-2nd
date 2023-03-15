# 음료수 얼려 먹기 - 입력이 주어질 때 생성되는 아이스크림의 총 개수는?
"""
입력
00110
00011
11111
00000
출력
3
"""

import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# dfs 정의
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 방문하지 않은 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 해당 노드의 상하좌우 확인
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)




