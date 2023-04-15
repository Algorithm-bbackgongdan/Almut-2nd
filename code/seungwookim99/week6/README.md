# Week 6

# 92343 : 양과 늑대
- 출처 : 프로그래머스
## 😎 Solved Code

### 💻 Code

```python
def solution(info, edges):
    global answer
    answer = 0
    visited = [False]*len(info)
    visited[0] = True
    def dfs(sheep, wolf):
        global answer
        answer = max(sheep, answer)
        for a,b in edges:
            if visited[a] and not visited[b]:
                visited[b] = True
                if info[b] == 1 and sheep > wolf + 1:
                    dfs(sheep, wolf + 1)
                elif info[b] == 0:
                    dfs(sheep + 1, wolf)
                visited[b] = False
        return
    dfs(1,0)
    return answer
```

### ❗️ 결과

실패(정답 확인)

### 💡 접근

dfs를 이용한 트리 완전 탐색을 이용한다.

모든 간선들에 대해 확인하며, 현재 상태에 대한 양의 개수를 리스트에 계속해서 저장한다.

탐색이 모두 끝난 후 양의 개수 리스트에서 최댓값을 답으로 제출한다.

## 🥳 문제 회고

1년 전에 굉장히 끙끙대며 풀었던 문제다. 다시 풀어봤는데 실패했다…

처음 접근은 다음과 같다.

- 현 상태에서 인접한 노드에 양이 없을 때 까지 모든 양을 모은다 (그리디 + bfs)
- 그 이후에는 bfs로 가장 가까운 양이 있는 노드를 탐색한다.
- 찾은 노드까지 이동한 뒤 위 과정을 반복한다.

하지만 반례를 발견했고, 단순히 bfs로만 풀 수 없다는 걸 알고 좌절했다…

위 코드는 구글링하면서 찾은 코드인데, 너무 간결하고 논리가 단순해서 놀랐다.

dfs를 인접 노드들이 아닌, 모든 간선을 탐색해서 가능한 풀이였다.

시간복잡도는 조금 크지만, 참신한 풀이였다.

# 42860 : 조이스틱
- 출처 : 프로그래머스
## 🥺 Unsolved Code

### 💻 Code

```python
from collections import defaultdict
alphabets_str = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabets = defaultdict(int)

def min_up_down(target):
    idx = alphabets[target]
    return min(idx, 26 - idx)

def solution(name):
    global answer
    answer = int(1e9)
    diff_num = 0
    name_list = list(name)
    # init
    for i, c in enumerate(alphabets_str):
        alphabets[c] = i
    for c in name_list:
        if c != 'A':
            diff_num += 1
    # 첫 문자가 'A'가 아니라면
    cnt = 0
    if name_list[0] != 'A':
        cnt = min_up_down(name_list[0])
        diff_num -= 1
        name_list[0] = 'A'
    
    def shortest_steps(curr, dir):
        cnt = 0
        while True:
            curr += dir
            cnt += 1
            if curr == len(name):
                curr = 0
            elif curr == -1:
                curr = len(name) - 1
            if name[curr] != 'A':
                break
        return (curr, cnt)
    
    def dfs(curr,cnt,d_num):
        global answer
        if d_num == 0:
            answer = min(answer, cnt)
            return

        # left
        next, lr_step = shortest_steps(curr, -1)
        ud_step = min_up_down(name_list[next])
        tmp = name_list[next]
        name_list[next] = 'A'
        dfs(next, cnt + lr_step + ud_step, d_num - 1)
        name_list[next] = tmp
        
        # right
        next, lr_step = shortest_steps(curr, 1)
        ud_step = min_up_down(name_list[next])
        tmp = name_list[next]
        name_list[next] = 'A'
        dfs(next, cnt + lr_step + ud_step, d_num - 1)
        name_list[next] = tmp
        
        return
    
    dfs(0,cnt,diff_num)
    return answer + cnt
```

### ❗️ 결과

실패

### 💡 접근

바꿔야 하는 문자 개수를 센다(n)

현재 위치에서 다음 문자를 바꾸기 위해 좌 또는 우로 이동할 수 있다.

이 모든 경우의 수를 완전탐색한다. 즉, O(2^n)이 소요된다.

### 🧐 접근에 대한 회고

처음 접근은 그리디였다.

현 위치를 기준으로 바꿀수 있는 문자 중 가장 가까운 것을 찾아가게끔 했다.

그러나 이 풀이는 반례가 존재했다.

```
...BBAAOAAB...
```

O가 나의 위치라고 할 때 바꿀수 있는 문자(B)의 최소 거리는 좌, 우가 같다. 어느것을 택해도 상관없어 보이지만 그렇지않다.

왼쪽을 먼저 방문하면 : 4 + 4 + 3 = 11

오른쪽을 먼저 방문하면 : 3 + 3 + 4 = 10

이 나오기 때문이다.

따라서 단순히 완전탐색을 시도했는데… 실패했다. 왜 틀렸는지 잘 모르겠다ㅠ

# 67259 : 경주로 건설
- 출처 : 프로그래머스
## 😎 Solved Code

### 💻 Code

```python
from collections import deque
INF = int(1e10)
def bfs(board,cost,N):
    global answer
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    cost[0][0][0] = cost[1][0][0] = 0
    q = deque([(0,0,0)])
    q = deque([(0,0,1)])
    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nd = i
            if 0<=ny<N and 0<=nx<N and board[ny][nx] == 0:
                c = cost[d][y][x] + 100
                if (x,y) != (0,0) and nd != d:
                    c += 500
                if c < cost[nd][ny][nx]:
                    cost[nd][ny][nx] = c
                    if ny == N-1 and nx == N-1:
                        answer = min(answer, c)
                    else:
                        q.append((ny,nx,nd))

def solution(board):
    global answer
    answer = INF
    N = len(board)
    cost = [[[INF]*N for _ in range(N)] for _ in range(4)]
    bfs(board,cost,N)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

dy,dx 순서에 따라 0 : 우 / 1 : 하 / 2 : 좌 / 3 : 상 의 방향 정보를 갖는다.

3차원 리스트 cost의 1번째 인덱스는 위의 4방향 정보, 2,3번째는 (y,x)를 나타낸다.

bfs시에 시작 지점에서 우(0) / 하(1) 방향 두 군데로 시작할 수 있다.

따라서 queue에 (0,0,0), (0,0,1)을 넣어 시작한다.(y,x,방향)

나머지는 비용을 계산하고 해당 방향과 좌표의 노드의 비용보다 적을 경우 queue에 push 한다.

나름 queue push, pop 연산을 줄이고자 (y,x)가 (N-1,N-1)에 도달했을 때는 강제로 append하지 않고 answer값을 갱신하기만 한다.

## 🥳 문제 회고

평소 풀던 bfs / dfs 문제보다 생각이 많아졌던 문제였다. 방향이라는 조건 하나만 추가됐는데 체감 난이도가 급상승한 것 같다. 어렵게 해결했지만 좋은 문제라고 생각한다.