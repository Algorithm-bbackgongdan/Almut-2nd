# 2주차

## [1. 백준\_2343 (기타레슨)](https://www.acmicpc.net/problem/2343)

### 아이디어

최적의 블루레이 크기를 찾기 위해서 이분탐색을 이용한다.

1. `주어진 크기일 때의 블루레이 수 <= 주어진 블루레이 개수(M)`:
   이미 가능하지만 블루레이 하나의 크기를 최대한 줄여야 함
2. `주어진 크기일 때의 블루레이 수 > 주어진 블루레이 개수(M)`:
   불가능하므로 블루레이 하나의 크기를 더 늘려야 함

### 코드

```python
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
lectures = list(map(int, read().split()))

start = max(lectures)
end = sum(lectures)
ans = 0


def get_amount(size):  # 주어진 크기(size)일 때의 블루레이 수를 구함
    total = 0
    cnt = 1
    for lecture in lectures:
        total += lecture
        if total > size:
            cnt += 1
            total = lecture
    return cnt


while start <= end:
    mid = (start + end) // 2
    amount = get_amount(mid)

    if amount <= M:  # 이미 가능. but 블루레이 하나의 크기를 최대한 줄여야 함
        ans = mid
        end = mid - 1
    else:  # 안 되는 경우(주어진 블루레이 개수보다 블루레이가 더 많이 필요한 상황)=> 블루레이 하나의 크기를 더 늘려야 함
        start = mid + 1

print(ans)
```

## [2. 백준\_2240 (자두나무)](https://www.acmicpc.net/problem/2240)

### 아이디어

`dp[시간][이동횟수][위치]`의 `1001*31*3` 사이즈 3차원 배열을 사용한다.

1. 1번 위치에 자두가 떨어질 때

```python
dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2]) + 1
dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2])
res = max(dp[time][cnt][1], dp[time][cnt][2])
```

2. 2번 위치에 자두가 떨어질 때

```python
dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2])
dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2]) + 1
res = max(dp[time][cnt][1], dp[time][cnt][2])
```

### 코드

```python
import sys

read = sys.stdin.readline

T, W = map(int, read().split())
trees = [int(read()) for _ in range(T)]

dp = [[[0 for i in range(3)] for j in range(31)] for k in range(1001)]  # dp[시간][이동횟수][위치] => 1001 * 31 * 3

dp[0][0][1] = 0
dp[0][0][2] = 0

res = 0

for time in range(T):
    for cnt in range(W + 1):  # 0 : 이동X
        if trees[time] == 1:  # 1번 위치에 자두가 떨어질 때
            if cnt == 0:
                dp[time][cnt][1] = dp[time - 1][cnt][1] + 1  # 제자리(1번위치)에서 이동 안 하는 경우
            else:
                dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2]) + 1
                dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2])
                res = max(dp[time][cnt][1], dp[time][cnt][2])
        else:  # 2번 위치에 자두가 떨어질 때
            if cnt == 0:
                dp[time][cnt][1] = dp[time - 1][cnt][1]  # 제자리(1번위치)에서 이동 안 하는 경우
            else:
                dp[time][cnt][1] = max(dp[time - 1][cnt][1], dp[time - 1][cnt - 1][2])
                dp[time][cnt][2] = max(dp[time - 1][cnt - 1][1], dp[time - 1][cnt][2]) + 1
                res = max(dp[time][cnt][1], dp[time][cnt][2])

print(res)
```

### 회고 및 코멘트

못 풀어서 솔루션을 찾아봤다.
2차원배열 dp 풀이도 있는것 같았는데 3차원배열 풀이가 이해가 더 잘 가서 해당 풀이를 참고했다.

## [3. 프로그래머스\_미로 탈출 명령어](https://school.programmers.co.kr/learn/courses/30/lessons/150365)

### 아이디어

dfs + 백트래킹으로 풀었다.

그냥 dfs 를 하면 시간초과가 뜨므로
탈출조건을 잘 설정해서 pruning(가지치기) 을 잘 해주는게 핵심포인트이다.

d -> l -> r -> u 순으로 탐색을 한다.

### 코드

```python
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
```

### 회고 및 코멘트

가지치기 방법을 생각하는 게 꽤 까다로웠다.

## [4. 프로그래머스\_두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

### 아이디어

각 큐의 합을 보고 `합이 큰 큐` 에서 `합이 작은 큐` 방향으로 숫자를 추가한다.

### 코드

```python
from collections import deque


def solution(queue1, queue2):
    answer = -1
    cnt = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    limit_cnt = (len(q1) + len(q2)) * 2

    tot1 = sum(q1)
    tot2 = sum(q2)
    total = tot1 + tot2

    if total % 2 == 1:
        return -1
    else:
        target = total // 2
        while cnt <= limit_cnt:
            if tot1 < target:
                tmp = q2.popleft()
                q1.append(tmp)
                tot1 += tmp
                tot2 -= tmp
                cnt += 1
            elif tot1 > target:
                tmp = q1.popleft()
                q2.append(tmp)
                tot1 -= tmp
                tot2 += tmp
                cnt += 1
            elif tot1 == target:
                answer = cnt
                break

    return answer
```

### 회고 및 코멘트

시간초과가 떠서 블로그를 참고했다.
매 번 sum 을 해서 시간초과가 떴는데 total 변수를 활용해서 시간초과를 줄일 수 있었다.
