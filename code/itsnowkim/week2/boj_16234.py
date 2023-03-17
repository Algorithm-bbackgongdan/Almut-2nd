# 인구이동
"""
국경 열 수 있는지 check 
조건에 맞게 인구 이동 (graph update)
count 증가시킴
위 행위 반복
"""
import sys
from collections import deque

# input
N, L, R  = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

count = 0

# 움직일 수 있는 방향 상하좌우
d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]

# dfs
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    # 현재 노드를 방문하지 않은 경우
    if visited_graph[x][y] == 0:
        # 해당 노드 방문 처리
        visited_graph[x][y] = 1
        # 해당 노드의 상하좌우 확인
        for i in range(4):
            nx = x + d_x[i]
            ny = y + d_y[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            # 이동이 가능한 경우만 호출
            thr = abs(graph[nx][ny] - graph[x][y])
            if L <= thr <= R:
                dfs(nx, ny)
        return True
    return False

# 가능한 모든 시작점 리턴
def check():
    starting_point = []
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                starting_point.append((i,j))
    
    return starting_point

# 연결된 블럭 순회
def calculate_bfs(starting_point):
    x, y = starting_point
    queue = deque([(x, y)])
    people = 0
    count = 0
    visited = [[False] * N for _ in range(N)]
    cordinates = []

    while queue:
        x, y = queue.popleft()
        cordinates.append((x,y))
        people += graph[x][y]
        count += 1
        visited[x][y] = True

        for i in range(4):
            nx = x + d_x[i]
            ny = y + d_y[i]

            # graph 범위 밖을 벗어나는 경우 제외
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 이미 방문한 경우 제외
            if visited[nx][ny]:
                continue
            # 국경이 열려 있는 경우만 queue에 포함
            thr = abs(graph[x][y] - graph[nx][ny])
            if L <= thr <= R:
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    updated = int(people / count)

    return cordinates, updated

res = 0

while True:
    visited_graph = [[0]*N for _ in range(N)]
    starting_points = check()
    solutions = []
    if len(starting_points) == N*N:
        break
    for point in starting_points:
        cordinates, updated = calculate_bfs(point)
        solutions.append((cordinates, updated))

    # cordinates에 있는 값들 평균값으로 업데이트
    for cordinates, sol in solutions:
        for x, y in cordinates:
            graph[x][y] = sol
    
    res += 1

print(res)