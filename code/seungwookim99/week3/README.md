# Week 3

# 2343: 기타 레슨
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
import sys

def calc_bluerays_number(length):
  count = 1
  curr_blueray_length = 0
  for video in videos:
    if curr_blueray_length + video > length:
      curr_blueray_length = 0
      count += 1
    curr_blueray_length += video
  return count

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
videos = list(map(int, sys.stdin.readline().rstrip().split(' ')))

left = max(videos)
right = sum(videos)

while left <= right:
  mid = (left + right) // 2
  bluerays_number = calc_bluerays_number(mid)
  if bluerays_number <= M:
    right = mid - 1
  else:
    left = mid + 1

print(left)
```

### ❗️ 결과

성공

### 💡 접근

M개로 나눠담되 블루레이 길이를 최소로 해야한다. 비디오들을 M개로 나눠 담는 경우의 수를 떠올리기란 너무 많다. 따라서 이분탐색으로 접근한다. 그럼 블루레이 길이를 이분탐색 해야 할 것이다.

가능한 블루레이 길이 범위는 `비디오 중 최대길이` ~ `모든 비디오의 길이 합` 일 것이다. 즉, M개의 블루레이로 담는 경우부터 1개의 블루레이로 만드는 경우가 범위이다.

각각을 left, right로 두고 `mid = (left + right) // 2` 를 계산해 이분탐색을 진행한다.

어떤 기준에 따라 left = mid + 1 또는 right = mid -1 로 범위를 좁혀나갈 것이다.

그 기준이 무엇일까?

비디오 리스트를 순회하며 mid 길이의 블루레이를 만들어본다. 그럼 블루레이 개수가 나올 것이다. 

만약 블루레이 개수가 M보다 많다면? 개수를 줄여야 할 것이다. 즉, 블루레이 길이가 너무 짧은 듯 하니 길이를 늘려야 한다. 따라서 left = mid + 1 로 업데이트 한다.

만약 블루레이 개수가 M보다 작거나 같다면? 개수를 늘려야 할 것이다. 즉, 블루레이 길이를 줄여야 한다. 개수가 M과 같다고 하더라도 우린 최소길이를 구해야 하므로 가능한 길이를 줄여야 한다. 따라서 right = mid - 1 로 업데이트 한다.

루프를 탈출하는 순간은 left == right + 1이 되는 순간이다. 이 말은 최소길이를 발견했다는 뜻이며, left값이 바로 답이 된다는 것을 알 수 있다.

## 🥳 문제 회고

접근은 맞게 했으나 정답을 mid라고 출력해 틀렸었다. left, right의 의미를 생각해보면 left가 정답이 될수밖에 없었다. 좋은 이분탐색 문제인 것 같다.


# 2240: 자두나무
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
import sys

T, W = map(int, sys.stdin.readline().rstrip().split(' '))
Jadu = [[0, 0] for _ in range(T + 1)]
for i in range(T):
    tree = int(sys.stdin.readline().rstrip())
    Jadu[i + 1][tree - 1] = 1

# (T + 1) * (W + 1) 2차원 리스트
DP = [[0] * (W + 1) for _ in range(T + 1)]

# 초기화
for w in range(W + 1):
    DP[T][w] = Jadu[T][w % 2]

for t in range(T - 1, -1, -1):
    for w in range(W, -1, -1):
        DP[t][w] = Jadu[t][w % 2] + max(DP[t + 1][w:])

print(DP[0][0])
```

### ❗️ 결과

성공

### 💡 접근

우선 1,2번 나무에 대해 T초에 떨어지는 자두의 수를 다음과 같이 저장했다.

```java
Jadu = [[0,0],[0,1],[1,0], ... ,[1,0]] // (T+1) x 2 2차원 리스트
```

Jadu[t][0]에는 t초에 1번 나무에 떨어지는 자두 개수, Jadu[t][1]에는 t초에 2번 나무에서 떨어지는 자두 개수룰 저장한 것이다.

t초에 w만큼 이동한 상황에서 받을 수 있는 자두의 최대 개수를 DP[t][w] 라고 하자. 그럼 우리가 구할 답은 DP[0][0]일 것이다. 이를 구하기 위해 Top-down 으로 2차원 리스트 DP를 채워나가면 된다.

가장 Top에 해당하는 값 DP[T][W], DP[T][W-1], … , DP[T][0] 은 어떻게 구할 수 있을까?

나무가 두 개 이므로 현재까지 이동한 횟수 w가 홀수라면 2번 나무에, 짝수라면 1번 나무에 위치할 것이다. 우리는 마지막 초(T초)에 어느 나무에서 자두가 떨어지는지 알고 있기 떄문에 초기값을 정하는 데에 큰 어려움이 없다.

따라서 아래와 같이 초기화 할 수 있다.

```java
for w in range(W + 1):
    DP[T][w] = Jadu[T][w % 2]
```

이제 Top-down으로 DP를 적용할 수 있다. 아래와 같다.

```java
for t in range(T - 1, -1, -1):
    for w in range(W, -1, -1):
        DP[t][w] = Jadu[t][w % 2] + max(DP[t + 1][w:])
```

DP[t][w]는 다음 두 값의 합이다.

- t초에 w만큼 이동한 상황에서 떨어지는 자두 개수 (Jadu[t][w % 2])
- t+1초에 w, w+1, w+2,…W만큼 움직인 경우 받을 수 있는 자두 개수 중 최댓값 (max(DP[t + 1][w: ])

## 🥳 문제 회고

DP유형의 문제라는 것을 알고 풀어서 그런지 해답을 금방 찾을 수 있었다. 아마 DP 문제라는 정보가 없었다면 최대로 받을 수 있는 경우를 그림으로 계속 그려봤을 것 같다. 그러다가 W와 T의 값에 따라 경우의 수가 너무 많다보니 2차원 리스트로 표현해야 할 것이라 생각하고 DP로 접근할 것 같다.


# 118667: 두 큐 합 같게 만들기
- 출처 : 2022 KAKAO TECH INTERSHIP
## 😎 Solved Code

### 💻 Code

```python
from collections import deque

def solution(queue1, queue2):
    MAX_ITERATION = 2*(len(queue1) + len(queue2))
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = q1_sum_orig, q2_sum_orig = sum(q1), sum(q2)
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    while q1 and q2 and (answer < MAX_ITERATION):
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            elem = q1.popleft()
            q2.append(elem)
            q1_sum -= elem
            q2_sum += elem
        elif q1_sum < q2_sum:
            elem = q2.popleft()
            q1.append(elem)
            q2_sum -= elem
            q1_sum += elem
        answer += 1
        
    if len(q1) == 0 or len(q2) == 0 or answer == MAX_ITERATION:
        answer = -1
    return answer
```

### ❗️ 결과

성공

### 💡 접근

우선 불가능한 경우를 생각해봤다. 두 큐의 합이 홀수면 불가능하므로 이를 구현했다.

두 큐 중 합이 큰 쪽에서 pop을 해서 작은쪽에 append를 한다. 그리고 각 큐의 합이 같아질 때 까지 반복하면 될 것이라 생각했다.

이 과정에서 while 루프를 사용했는데, 한 iteration마다 pop / push 가 발생한다. 그리고 매 iteration마다 `sum(queue)`로 큐의 합을 계산하지 않고 `q1_sum`, `q2_sum` 을 관리하며 큐의 합을 계산했다. 그리고 주어진 queue1, queue2를 deque로 만들어 pop / push 연산을 진행했다. 이유는 아래와 같다

- deque는 list와 달리 double linked list로 구현되어있어 popleft()가 O(1)이기 때문
- sum(queue)는 O(n)의 시간복잡도가 걸릴 것으로 예상되므로 이를 줄이기 위함

만약 q1, q2중 어느 하나가 비었다면 while문을 탈출하고 -1을 반환한다.

그럼에도 일부 케이스가 시간초과가 떴다. 아마 무한루프에 빠지는 예외가 존재할 것이라 생각했다. 좀 더 예시를 생각해보고 아래 케이스를 발견했다.

```python
queue1 = [5]
queue2 = [5,2]
```

이 예제는 루프를 빠져나오지 못한다. print를 좀 찍어보니 push / pop을 하다 원 상태로 돌아오는 사이클을 발견했다. 원상태로 돌아오면 더이상 볼 필요가 없으므로 루프를 탈출할 수 있다.

따라서 모든 원소가 pop됐다가 push되는 개수를 세면 `2*(len(queue1) + len(queue2))` 가 된다. 이를 MAX_ITERATION으로 두고 탈출 조건을 추가하니 문제가 해결됐다.

## 🥳 문제 회고

작년 카카오 테크 인턴십에 지원해서 실전으로 풀어본 문제다. 이번에 문제를 풀고 그 당시를 회고해보니, 같은 지점에서 막혔다. 바로 무한 루프를 도는 케이스를 어떻게 해결할 지에 대한 것이다. 그 때는 대략 `3*queue1` 으로 MAX_ITERATION을 설정했다. 사실 이번에 풀 때는 나름 근거는 있지만 확신이 안 섰다.


# 150365: 미로 탈출 명령어
- 출처 : 2023 KAKAO BLIND
## 😎 Solved Code

### 💻 Code

```python
import sys
sys.setrecursionlimit(10000)

dx = {
    'd': 1,
    'l': 0,
    'r': 0,
    'u': -1
}

dy = {
    'd': 0,
    'l': -1,
    'r': 1,
    'u': 0
}
def manhattan_distance(p1,p2):
    (x1,y1), (x2,y2) = p1, p2
    return abs(x1-x2) + abs(y1-y2)

def is_impossible(p1,p2,k):
    man_d = manhattan_distance(p1,p2)
    if man_d > k: # 최단경로보다 k가 작을 때
        return True
    return man_d % 2 != k % 2 # 홀수 / 짝수 번에 갈 수 있는지 여부

def solution(n, m, x, y, r, c, k):
    global answer
    global end
    global K
    K = k
    answer = ""
    start, end = (x,y), (r,c)
    if is_impossible(start, end, k):
        return "impossible"
    
    def inside_boundary(x,y):
        return (1 <= x <= n) and (1 <= y <= m)
    
    def dfs(x,y,moves):
        global answer
        if len(moves) == K:
            if (x == end[0]) and (y == end[1]):
                answer = moves # 정답 저장 및 dfs 종료
                return True
            else:
                return False
        steps_to_go = K - len(moves) # 남은 step
        shortest_path_len = manhattan_distance((x,y),end) # 현위치 기준 최단거리
        if steps_to_go < shortest_path_len:
            return False
        
        for direction in ['d','l','r','u']:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if inside_boundary(nx,ny):
                solved = dfs(nx,ny,moves+direction)
                if solved:
                    return True
        return False
    dfs(x,y,"")
    return answer
```

### ❗️ 결과

어렵게 성공

### 💡 접근

백트래킹을 곁들인 DFS로 접근했다.

먼저 일부 케이스는 impossible 여부를 바로 판단할 수 있다. 이를 `is_impossible` 에서 처리했다.

start → end 까지의 맨하탄 거리(최단거리)가 k 보다 크다면 애초에 불가능하다. 또는 맨하탄 거리와 k가 홀수 / 짝수로 서로 다르다면 도달이 불가능하다. 이는 몇 번 손으로 그리며 시뮬레이션 해보면 알 수 있다.

dfs로 k depth 만큼 재귀탐색을 진행하고, depth k에서 end에 도달했는지 확인한다.

이 때 아주 중요한 것은 동서남북 탐색의 순서를 `[’d’, ‘l’, ‘r’, ‘u’]` 로 해야한다!! 왜냐하면 문제에서 end로 k번만에 갈 수 있는 경로중 사전순으로 가장 빠른 경로를 출력하라고 했기 때문이다. 이렇게 탐색을 진행하다 k번째에 end에 최초로 도달하면, 그 경로가 정답이 될수밖에 없다. 그럼 탐색을 즉시 종료할 수 있으므로 연산량을 크게 줄일 수 있다. 즉시 종료를 위해 caller는 callee 결과의 영향을 받아야 한다. 따라서 dfs 함수는 답을 찾으면 True, 아니면(탐색을 계속 해야 한다면) False를 반환한다. 

```python
if inside_boundary(nx,ny):
		solved = dfs(nx,ny,moves+direction)
    if solved:
		    return True
```

그리고 dfs 내부에서 재귀호출 결과에 따라 즉시 탈출할 수 있게 처리해두었다.

연산량을 더 줄이기 위해 백트래킹을 얹어준다. 현 위치에서 남은 이동횟수로 end까지 도달할 수 없는게 자명하면 더 탐색을 할 이유가 없다.

```python
steps_to_go = K - len(moves) # 남은 step
shortest_path_len = manhattan_distance((x,y),end) # 현위치 기준 최단거리
if steps_to_go < shortest_path_len:
    return False
```

`moves` 에는 현재까지 온 경로(ex. ‘drrld’)를 string으로 저장하고 있다. K번 이동하기 위해 남은 step 수와, 현 위치에서 최단거리까지의 길이를 비교하며 dfs 중간에서 pruning을 진행할 수 있다.

## 🥳 문제 회고

처음에는 변수의 범위 조건을 보고 막연하게 DFS/BFS로 접근하면 시간 초과가 뜰 것이라 생각했다. 따라서 접근을 바꿔 그리디 방식으로 생각했다. 그런데 1시간 넘게 고민해도 도저히 방법이 안떠올라 포기했다. 당시에 현수형이랑 문제를 같이 풀고있었고, 나와 다르게 DFS로 접근했다. 일부 백트래킹 조건을 추가하면 문제를 해결할 수 있을 것 같아서 백지 상태에서 다시 시작했고 어렵게 풀었다.

아마 실전이었다면 고민하다 스킵했을 것 같은 문제다. “impossible”을 출력하는 여러 예외 케이스를 각각 처리해야 하며, 적당히 pruning까지 해야했던 까다로운 문제였다.