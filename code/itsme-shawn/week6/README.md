# 5주차

## 1. 프로그래머스\_양과 늑대 (92343)

### 💡 Idea

풀지 못해서 블로그 풀이 참고했음

노드를 왔다갔다 해야하므로, 부모노드에서 자식노드로 파고 들어가는 일반적인 dfs, bfs 로는 해결이 안 된다.

edges 에서 [부모 노드, 자식 노드] 를 받아와서

부모노드는 방문했고, 자식노드(본인)는 방문 안 한 노드만 dfs 를 해야한다.

매 방문마다 answer 리슨트에 현재의 sheep 개수를 저장하고, 모든 dfs 가 끝날 시 max(answer) 를 출력한다.

### 🧑🏻‍💻 Code

```python
def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            # 부모는 방문했고, 자식노드(본인)는 방문 안 한 노드만 dfs
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)
```

### 💬 Commentary

풀이 참고
[[프로그래머스 L3] 양과 늑대 (python)](https://velog.io/@thguss/프로그래머스-L3-양과-늑대-python)

## 2. 프로그래머스\_조이스틱 (42860)

# 💻 Code

## 📂 #1. 틀린 풀이

### 💡 Idea

[최초아이디어]

조이스틱의 최소 횟수는 `(커서를 이동하는 횟수) + (알파벳을 "A"에서 원하는 알파벳까지 이동하는 횟수)` 이다.

여기서 `(알파벳을 "A"에서 원하는 알파벳까지 이동하는 횟수)` 는 고정돼있으므로 `(커서를 이동하는 횟수)` 의 최소값을 구해야한다.

`커서를 이동하는 횟수` 구하기

가장 긴 A 그룹을 안 지나가는 것이 가장 효율적일 것이라고 생각했다. (⇒ 실제로는 효율적이지 않았다. )

그래서 가장 긴 A 그룹의 시작인덱스와 끝인덱스를 찾는다.

그리고 가장 긴 A 그룹을 중심으로 왼쪽그룹과 오른쪽그룹을 나눴다.

`BBAABBBAAAAABB` 가 있으면

- 왼쪽그룹 : BBAABBB
- 가장 긴 A 그룹 : AAAAA
- 오른쪽그룹 : BB

- default(기본진행) : 그냥 오른쪽으로 쭉 진행
- left_twice (왼쪽 2번, 오른쪽 1번) : 왼쪽그룹에서 가장 긴 A 그룹 직전까지 진행했다가 다시 왼쪽그룹의 처음으로 돌아온다. 그리고 왼쪽으로 다시 진행하면서 오른쪽 그룹을 탐색한다.
- right_twice (왼쪽 1번, 오른쪽 2번) : 오른쪽그룹 왔다갔다하고 왼쪽 그룹 탐색

`min(default, left_twice, right_twice)` 이 좌우이동의 최소값이 된다.

### 🧑🏻‍💻 Code

```python
def solution(name):
    answer = 0

    # 한 알파벳 바꿀 때 누르는 조이스틱 최소 횟수
    def get_change_char(ch):
        if ord(ch) <= ord('N'):
            return ord(ch) - ord('A')
        else:
            return ord('Z') - ord(ch) + 1

    # 가장 긴 연속된 A 그룹을 찾는다.
    start, end = 0,0
    flag = 0
    longest_A = [False,False]

    for i in range(len(name)):

        # 'A' 를 처음 발견하면 flag 처리하고 start 인덱스 저장
        if not flag and name[i] == 'A':
            flag = 1
            start = i

        # flag 가 설정된 상태에서 'A' 가 아닌 것을 발견하면 end 값에 i-1 저장
        if flag and name[i] != 'A':

            end = i -1
            flag = 0

            # 가장 긴 A 묶음 갱신
            if longest_A[1] - longest_A[0] <= end - start:
                longest_A = [start, end]

        # flag 가 설정된 상태에서 끝까지 도달했다면 마지막 문자도 A 였다는 의미
        if flag and i == len(name)-1:
            end = i # 예외처리
            flag = 0

            if longest_A[1] - longest_A[0] <= end - start:
                longest_A = [start, end]

    # print(longest_A)

    for ch in name:
        if ch != "A":
            answer += get_change_char(ch)

    default = len(name)- 1 # 기본 (그냥 직진)

    # 'A' 가 없는 경우는 default 가 답이 됨
    if longest_A == [False, False]:
        answer += default
    # 모든 문자가 'A' 인 경우는 답이 0 이 됨
    elif longest_A == [0,len(name)-1]:
        answer = 0

    # 그 외 나머지 경우
    else:

        # 가장 긴 A 의 시작인덱스가 0 인 경우는 0 으로 예외처리
        left = longest_A[0] - 1 if longest_A[0] > 0 else 0
        right= (len(name) - 1) - longest_A[1]

        left_twice = left * 2 + right
        right_twice = left + right * 2

        # default(그냥 직진), left_twice(왼쪽 두 번, 오른쪽 한 번), right_twice(d왼쪽 한 번, 오른쪽 두 번)
        left_right_move = min(default, left_twice, right_twice)

        answer += left_right_move

    return answer
```

### 💬 Commentary

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/38d8dc78-5e17-4bd1-9ffb-31d31f6711b3/Untitled.png)

반례 케이스가 발생한다.

`AAABBAAAABBB` 같은 경우, 답은 14인데 위 코드는 15 가 나온다.

내 코드

좌우이동 : 왼쪽3칸이동(BBB) + 오른쪽3칸이동(BBA) + 오른쪽4칸(AABB) = 10

알파벳바꾸기 : 5

총합: 15

실제

좌우이동 : 왼쪽으로 9칸 (BBBAAAABB) = 9

알파벳바꾸기 : 5

총합 : 14

나는 가장 긴 A 묶음은 무조건 안 지나가는게 효율적이라고 생각하고 코드를 짰는데 애초부터 그 방법이 그리디한 방법이 아니였다.

결국 이 방법으로는 포기

---

## 📂 #2. 정답 풀이

### 💡 Idea

A 묶음을 지나가는 스킵해야하는 것이 맞긴한데, 가장 긴 A 묶음을 스킵해야 하는 것은 아니다.

따라서 `기존방식`, `왼쪽으로 가는 방식`, `오른쪽으로 가는 방식` 중 작은 값을 매번 체크한다.

### 🧑🏻‍💻 Code

```python
def solution(name):

	# 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
				# for문 돌면서 왼쪽으로 갈지 오른쪽으로 갈지 매번 체크를 한다.
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
```

### 💬 Commentary

접근은 비슷하게 했는데 애초에 그리디 판단 자체를 잘못해서 틀렸다.

실전에서 문제의 의도대로 그리디하게 접근을 못 할거라면 bfs, dfs 완전탐색이 나을 것 같다.

참고풀이

[[프로그래머스, 파이썬] 조이스틱, Greedy](https://velog.io/@jqdjhy/프로그래머스-파이썬-조이스틱-Greedy)

## 3. 프로그래머스\_경주로 건설 (67259)

# 💻 Code

## 📂 #1

### 💡 Idea

bfs 로 탐색을 하는데 큐에 (x좌표, y좌표, 누적비용, 방향) 을 저장하며 탐색을 한다.

1. 직선/코너 판단

   큐에 pop 한 방향 값과 같으면 직선이고, 다르면 코너다.

2. 최소비용

   큐에 누적비용을 담음으로써 방문할 노드의 최소비용을 갱신해준다.

### 🧑🏻‍💻 Code

```python
from collections import deque

def solution(board):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(board)
    MAX = int(1e9)

    def bfs(start):
        visited = [[MAX]*n for _ in range(n)]
        visited[0][0] = 0

        q = deque([start]) # x, y, cost, direction
        while q:
            x, y, c, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:

                    # dp

                    if i == d: # 방향 그대로이면 직선 금액 계산
                        nc = c + 100
                    else: # 방향 달라지면 코너 금액 계산
                        nc = c + 600

                    # new cost 가 작을 때만 갱신하고 방문처리, 큐 append
                    if nc < visited[nx][ny]:
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i])

        return visited[n-1][n-1]

    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])
```
