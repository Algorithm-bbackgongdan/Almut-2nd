# 42860 : 조이스틱
### code
```python
def solution(name):
    answer = 0
    for i in name:
        k = ord(i)-65
        if(k <= 12):
            answer += k
        else:
            answer += k-(2*(k-13))
    
    l = len(name)-1

    for i in range(0,len(name)):
        index = i +1
        while(index < len(name) and name[index] == 'A'):
            index+=1
        # min('A'를 지나 계속 전진,'A'를 만나 왔던 길을 다시 돌아감)
        # 처음부터 오른쪽이 아니라 왼쪽으로 이동 후, 'A'를 만나면 되돌아가는 횟수
        l = min(l, i*2 + len(name) - index, (len(name)-index)*2 + i)
    
    return answer + l

  ```
## 결과
성공 (테스트케이스 구글링)
## 접근
알파벳 변경 횟수(상하)와 커서 이동 횟수(좌우)를 따로 구해 더해주는 방법을 생각했다.
알파벳 변경 횟수는 고정되어있고, 커서를 최소한의 횟수로 움직여 조이스틱 조작횟수의 최솟값을 구한다.

커서의 이동횟수의 최대값은 "len(name) -1"이다.
커서가 'A'를 만나도 계속 이동하는 최대 이동횟수와, 'A'를 만나 왔던길을 다시 돌아가는 이동 횟수를 비교하여 최솟값을 더해준다.
## 문제 회고
커서의 이동에 대한 고민이 많았던 문제였다.
몇몇 테스트케이스에서 오류가 발생하여 예외 케이스를 찾으려고 노력했으나, 문제 접근을 따르지 않는 예외 케이스를 결국 생각해내지 못해 구글링을 통해 예외 케이스를 찾을 수 있었다. ex) 예외 케이스 : "BBBBAAAAB"
# 92343 : 양과 늑대
### code
```python
 #실패 코드
from collections import deque

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
visited = [0 for i in range(18)]
queue = []
deque_q = deque(queue)

def bfs(node):
  global sheep
  global wolf
  sheep = 0
  wolf = 0
  visited[node] = 1
  queue.append([node,info[node]])
  while queue:
    u = queue.pop(0)
    if info[u[1]] == 0:
      sheep += 1
    else:
      wolf += 1
    if sheep <= wolf:
      break
    for i in range(len(edges)):
      next_node = edges[i][1]
      if edges[i][0] == u[0] and visited[next_node] == 0:
        visited[next_node] = 1
        queue.append([next_node,info[next_node]])
    queue.sort(key=lambda x:(x[1],x[0]))


def solution(info, edges):
    bfs(0)
    answer = sheep
    return answer

 #구글링 코드
def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0

	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)
  ```
## 결과
실패
## 접근
부모노드를 방문하면 자식노드를 queue에 append하는 BFS를 활용하여 문제를 풀려고 하였다. 이때 append되는 자식노드가 양인지 늑대인지에 따라 양일 때, 앞에 오도록 정렬하여 늑대의 숫자가 양보다 많거나 같아지는 순간을 최대한 뒤로 미루었다.
그래서 양과 늑대의 숫자가 같아지는 순간의 양의 숫자가 최대 양의 마리 수라고 생각하였다.

그러나 자식노드에 늑대만 있게 될 때, 어떤 늑대를 선택하는 것이 최선의 선택인지 그 늑대의 자식노드를 보기 전까지 모른다는 문제에 막혔다..

긴 시간 이 문제를 해결할려고 노력했지만, 결국 풀지 못하고 구글링을 하였다.
1. 양의 수가 늑대의 수보다 많은가? (늑대의 수가 양보다 많거나 같다면 탐색종료)
2. 부모노드를 방문한 적이 있는가?
3. 자식 노드를 처음 방문하는가?

-> 양이 늑대보다 많으면 결과 배열에 저장하고, edges 배열에 방문한 부모노드와 방문하지않은 자식노드 정보가 있을 때 자식노드를 방문하여 양과 늑대의 수를 업데이트하고 위의 과정을 반복한다.

## 문제 회고
week4의 양궁문제와 비슷하게 이번 "양과 늑대"문제의 답안을 봤을 때도 멍했다.
굉장히 어려운 길로 돌아갔음을 크게 느꼈다. 스터디 교재의 저자의 "단순하게 완전탐색을 활용하여 문제를 푸는 방법을 가장 먼저 생각해보고 이후에 시간복잡도와 공간복잡도를 고려하여 문제를 푸는 방향을 잡는 것이 중요하다"는 말을 또 한번 생각하였다. 그러나 이렇게 문제를 간단하게 푸는 방법(아이디어!!!)을 생각하는 것이 제일 어렵다..


# 67259 : 경주로 건설
### code
```python
## BFS만 이용했을 때
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    global now_cost
    queue = deque()
    answer = 1e9
    costs = [[1e9] * len(board) for i in range(len(board))]
    queue.append((0,0,0,-1))
    costs[0][0] = 0
    while queue:
        x,y,cost,dir = queue.popleft()
        if x == len(board)-1 and y == len(board)-1:
            answer = min(answer, costs[x][y])
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == 1:
                    continue
                if(dir == -1 or dir == i): 
                    now_cost = cost + 100
                else: 
                    now_cost = cost + 600

                if costs[nx][ny] >= now_cost:
                    costs[nx][ny] = now_cost
                    queue.append([nx,ny,now_cost,i])
    return answer

    #BFS + DP
    from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    global now_cost
    queue = deque()
    answer = 1e9
    costs = [[[1e9] * len(board) for i in range(len(board))] for _ in range(4)]

    for i in range(4):
      costs[i][0][0] = 0

    if board[0][1] == 0:
      queue.append([0,1,100,0])
      costs[0][0][1] = 100

    if board[1][0] == 0:
      queue.append([1,0,100,1])
      costs[1][1][0] = 100

    while queue:
        x,y,cost,dir = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == 1:
                    continue
                if(dir == -1 or dir == i): 
                    now_cost = cost + 100
                else: 
                    now_cost = cost + 600

                if costs[i][nx][ny] > now_cost:
                    costs[i][nx][ny] = now_cost
                    queue.append([nx,ny,now_cost,i])
    return min([costs[i][-1][-1] for i in range(4)])
  ```
## 결과
실패 후 구글링
## 접근
BFS를 이용하여 (N-1,N-1)까지 갈 수 있는 경주로 중 최소비용을 정답으로 출력.
1. 현재의 좌표에서 2차원 배열 범위 안에서 다음 좌표가 벽이 아닐 때, 이동
2. 이동하면서 경주로 건설에 드는 비용 계산
3. 비용 계산을 위해서 직선도로인지, 코너인지 선별해주기위한 방향을 알아야한다.

## 문제 회고
처음에 BFS를 이용하여 완전탐색을 해야하는 문제라고 생각하였다. 최단경로가 아닌 최소비용을 구해야 한다는 것과, 직선도로와 코너를 구분하는 것이 상당히 어려워 온전히 나의 힘으로 풀지 못하였다. 그런데도 답안을 제출했을 때 마지막 테스트 케이스 통과가 안나와 구글링을 한 결과 처음에 왼쪽으로 출발하는 경우와 아래로 출발하는 경우 중 최솟값을 선택하는 케이스가 있음을 알 수 있었다.

백준 문제가 아닌 프로그래머스와 삼성SW 역량테스트와 같은 실제 코테에 나오는 문제들을 풀어보면서 단순히 알고리즘을 알고있는 것이 아닌, 적절한 적용과 2개 이상의 알고리즘을 한 문제 내에서 같이 사용하는 것에 대한 대비가 필요하다고 생각했다.

