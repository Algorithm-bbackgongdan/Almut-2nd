# 42860 - 조이스틱
greedy? 문제라고 하는데 사실 brute force 로 풀었다.

핵심은 다음과 같다.
>커서가 위치한 칸에서 원하는 알파벳을 만들 때 까지 최소 이동 횟수는 정해져 있다. 따라서, 좌우로 이동할 최소 횟수만 구하면 된다.

좌우로 이동하는 최소 횟수는 단순히 오른쪽으로 끝까지 쭉 가거나, 왼쪽으로 쭉 가서 돌아오는 경우가 있다.
추가로 고려해야 하는 것은 "어느 지점까지 갔다가, 왔던 길을 되돌아와서 목표 지점까지 가는 경우" 이다. 따라서 for loop을 돌면서 이러한 경우를 체크해 주었고, 매번 minimum 값을 갱신해 주어 최종적으로 가지고 있는 minimum값은 전체의 minimum값이 된다.

# 67259 - 경주로 건설
이런 문제를 풀기 위해서는 두 가지 방법이 존재한다.
1. dfs 로 접근하는 방법 (시간 초과의 위험이 있지만 정답은 맞음)
2. bfs + dp 로 접근하는 방법 (좀 더 어렵지만 항상 맞음)

## 첫 번째 방법
나는 처음에 dfs로 접근했다. 역시나 알고리즘상으로는 문제가 없지만, 시간초과가 나왔다.

```python
# 경주로 건설
from copy import deepcopy

def in_board(x, y, N):
    if 0<=x and x<=N and 0<=y and y<=N:
        return True
    return False

def solution(board):
    global answer
    answer = int(1e9)
    # 방향 배열
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    # 도착점
    N = len(board)-1
    # visited
    visited = deepcopy(board)

    def dfs(curr_x, curr_y, cost, curr_dir, visited):
        global answer
        # 도착했는지 체크
        # print('cost',cost)
        if (curr_x, curr_y) == (N, N):
            # 최솟값 업데이트
            answer = min(answer, cost)
            return
        
        # 이미 최솟값보다 넘었을 경우 중단
        if cost > answer:
            return
        
        # 방향에 따라 dfs 호출
        for dir_index, next_dir in enumerate(directions):
            x,y =next_dir
            nx, ny = curr_x+x, curr_y+ y
            # 보드 내에 존재하지 않으면 패스
            if not in_board(nx, ny, N):
                continue
            
            # 해당 지점이 벽, visited 여부
            if board[nx][ny]==1 or visited[nx][ny]==1:
                continue
            
            # 방향이 달라졌을 경우 cost 추가로 발생
            visited[nx][ny] = 1
            if curr_dir == dir_index:
                dfs(nx, ny, cost+100, dir_index, visited)
            else:
                dfs(nx, ny, cost+100+500, dir_index, visited)
            visited[nx][ny] = 0
    
    # 맨 처음 시작하는 방향 정해줘야 함
    dfs(0,0,0,3,visited)
    dfs(0,0,0,1,visited)
    
    return answer
```


## 두 번째 방법
두 번째 방법인 bfs + dp 로 접근했다. (선종형의 코드 참고)
https://school.programmers.co.kr/questions/30355
좋은 예시도 있다.

```python
# 경주로 건설

from collections import deque

def in_board(x, y, N):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    return False

def solution(board):
    # 무한 초기화
    INF = int(1e9)
    # 보드 길이는 n*n
    N = len(board)
    # 방향 배열 - 처음 방향은 오른쪽으로 가거나, 아래로 가거나 둘 중 하나
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # cost 배열
    costmap = [[INF for _ in range(N)] for _ in range(N)]
    costmap[0][0] = 0

    # q 초기화 - (x, y, cost, direction)
    q = deque([(0, 0, 0, 1), (0, 0, 0, 3)])

    while q:
        curr_x, curr_y, curr_cost, curr_dir = q.popleft()

        for dir_index, dir in enumerate(directions):
            x, y = dir
            nx, ny = curr_x+x, curr_y+y

            # 보드 내에 존재하며, 이동할 수 있는 경우만 고려
            if in_board(nx, ny, N) and board[nx][ny] == 0:
                # 이전 방향과 같은 경우와 다른 경우 두 가지 고려.
                if (curr_dir==dir_index) and (curr_cost+100 <= costmap[nx][ny]): # 방향이 같음
                    q.append((nx,ny,curr_cost+100,dir_index))
                    costmap[nx][ny] = curr_cost+100
                elif curr_cost+600 <= costmap[nx][ny]+200: # 이전 진행방향과 다른 방향임. 
                # 현재 위치에서 회전을 하느냐, 직전 위치에서 직진해서 현재 위치에 도달했느냐 고려
                    q.append((nx,ny,curr_cost+600,dir_index))
                    costmap[nx][ny] = curr_cost+600

    return costmap[N-1][N-1]
```

**<해결방법>**
1. board를 탐색하면서 큐에 (좌표, 금액, 방향)의 형태로 집어넣습니다.
2. 현재 방향이 큐에서 꺼낸 노드의 방향과 같으면 100원 추가하여 큐에 넣고, 다르다면 600원 추가하여 큐에 넣습니다.

이전 노드에서 직진하여 현재 노드에 도달한 경우에는, 100원의 비용이 추가로 발생하므로, 비용 계산에 이를 반영하기 위해 200을 더해줍니다. 이렇게 함으로써, 이전 노드에서 직진한 경우와 회전한 경우를 비교할 수 있습니다.(우변이 +200인 이유)

## 세 번째 방법
마지막 방법은 3차원 배열을 사용한 bfs방식이다. 정확하고, 앞으로 코딩 테스트에서 가장 먼저 떠올려야 하는 방식이다.
```python
# 경주로 건설

from collections import deque

def in_board(x, y, N):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    return False

def solution(board):
    # 무한 초기화
    INF = int(1e9)
    # 보드 길이는 n*n
    N = len(board)
    # 방향 배열 - 처음 방향은 오른쪽으로 가거나, 아래로 가거나 둘 중 하나
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # cost 배열
    costmap = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]
    costmap[0][0][0] = 0
    costmap[1][0][0] = 0
    costmap[2][0][0] = 0
    costmap[3][0][0] = 0

    # q 초기화 - (x, y, cost, direction)
    q = deque([(0, 0, 0, 1), (0, 0, 0, 3)])

    while q:
        curr_x, curr_y, curr_cost, curr_dir = q.popleft()

        for dir_index, dir in enumerate(directions):
            x, y = dir
            nx, ny = curr_x+x, curr_y+y

            # 보드 내에 존재하며, 이동할 수 있는 경우만 고려
            if in_board(nx, ny, N) and board[nx][ny] == 0:
                new_cost = curr_cost+100
                if curr_dir!=dir_index: # 방향이 다른 경우 500 추가
                    new_cost += 500
                
                # 업데이트할지, 말지 결정
                if new_cost < costmap[dir_index][nx][ny]:
                        q.append((nx, ny, new_cost, dir_index))
                        costmap[dir_index][nx][ny] = new_cost
                
    return min([costmap[0][N-1][N-1],costmap[1][N-1][N-1],costmap[2][N-1][N-1],costmap[3][N-1][N-1]])
```

# prog_92343 - 양과 늑대
처음 시도는 bfs 로 접근하였지만, 단순히 그렇게 접근하면 모든 경우의 수를 순회하지 못하는 것을 알게 되었다.
핵심은 "모든 경우의 수를 어떻게 순회할 수 있도록 하는가" 인 것으로 판단하였다.

부모 노드는 무조건 먼저 방문하기 때문에 "위상 정렬" 로 접근하면 되지 않을까?

...라고 생각하다가 bfs를 돌리면서 "다음에 방문할 모든 노드를 추가해버리면 되지 않나?" 로 생각을 바꿔서 시도했는데,
간단하게 풀렸다!

그 전에 itertools에 collection 구하는 것 처럼 구현하려고도 했는데, 실제로 사용하지는 않았지만 덕분에 따로 공부하게 되어서 추가한다.
```python
def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result


print(gen_combinations([0,1,2,3,4,5],2))
```