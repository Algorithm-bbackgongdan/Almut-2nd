# 섬의 개수만큼 노드 생성
# 섬끼리 연결 가능한만큼 연결 (모든 가능한 간선 연결)
# MST 만들기 - kruskal 알고리즘
# 겹치는 구간 고려는 하지 않아도 됨!
# 최종 cost 출력, MST가 불가능한 경우 -1 출력
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# step1. 섬의 개수만큼 노드 생성하기 위한 체크배열
visited = [[False] * m for _ in range(n)]
# 4 방향 체크
direction = [(-1,0),(1,0),(0,1),(0,-1)]

# 보드 밖인지 체크
def is_in(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    return True

# bsf로 섬 찾기
def bfs(x,y,mark):
    q = deque([(x,y,mark)])
    visited[x][y] = True
    graph[x][y] = mark
    
    while q:
        x,y, mark = q.popleft()
        # 해당 좌표에서 모든 방향으로 찾기
        for di,dj in direction:
            nx,ny = x+di, y+dj
            # 보드 밖이거나, 0일 경우(섬 밖일경우) 중단
            if not is_in(nx,ny) or graph[nx][ny] == 0:
                continue
            # 같은 섬일 경우.
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = mark
                visited[nx][ny] = True
                q.append((nx,ny,mark))

    return

island = 1
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and not visited[i][j]: #섬이면서, 아직 방문하지 않은 경우 탐색
            bfs(i,j,island)
            island+=1

# for g in graph:
#     print(g)

# step 2. 간선의 길이 전부 구하기 - bfs
edge=set()
def get_dist(x,y,mark):
    q = deque()
    for i in range(4):
        q.append((x,y,i,0)) # xy좌표, 방향, 거리

    while q:
        curr_x, curr_y, i, dist = q.popleft()
        # 방향대로 이동해보기
        x,y = direction[i]
        nx,ny = curr_x+x, curr_y+y
        # 보드를 벗어나거나, 같은 섬이면 중지 - 체크할 필요가 없음
        if not is_in(nx,ny) or graph[nx][ny]==mark:
            continue
        # 보드 안에 있으면서, 0을 만나는 경우 거리 업데이트하면서 q에 넣기
        if graph[nx][ny] == 0:
            q.append((nx,ny,i,dist+1))
            continue
        # 다른 섬을 만난 경우, 거리가 2이상인 경우 간선에 추가
        if graph[nx][ny] != mark and (dist)>=2:
            edge.add((dist,mark,graph[nx][ny]))

    return

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0: # 섬일 경우, 해당 지점에서 직선그어서 만나는 다른 섬과의 거리 구하기
            visited = [[False]*m for _ in range(n)]
            get_dist(i,j,graph[i][j])

edge=list(edge)
edge.sort()
# print(edge)

# step3. kruskal algorithm
parent = [i for i in range(island+1)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
res = []
# 그래프 간선 선택하기
for e in edge:
    weight, v1, v2 = e
    if find_parent(parent, v1) != find_parent(parent, v2):
        union(parent,v1,v2)
        answer += weight
        res.append(e)

# 답이 -1인 경우 출력하기
# print(island)
# print(len(res))
if len(res) != (island-2) or answer == 0:
    print(-1)
else:
    print(answer)
# print(answer)
# print(res)


