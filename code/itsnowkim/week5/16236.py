from collections import deque
INF=1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size=2
now_x,now_y=0,0
for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            now_x, now_y = i,j
            array[i][j] = 0

# 방향
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# 모든 위치의 '최단거리' 만 계산하는 BFS 함수
def bfs():
    # 값이 -1 이라면 도달할 수 없다는 의미
    dist = [[-1]*n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며, 거리는 0
    q = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        for i,j in directions:
            nx,ny = x+i, y+j
            if 0<= nx and nx <n and 0<=ny and ny<n:
                if dist[nx][ny] == -1 and array[nx][ny]<=now_size:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 고르는 함수
def find(dist):
    x,y = 0,0
    min_dist=INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 경우
            if dist[i][j] != -1 and 1<=array[i][j] and array[i][j]<now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    # 먹을 수 없는 물고기가 없을 경우
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

result = 0
ate = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    if value==None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate+=1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            ate=0
            now_size+=1

