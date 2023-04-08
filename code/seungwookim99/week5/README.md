# Week 5

# 3665 : 최종 순위
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
import sys
from collections import deque

input = sys.stdin.readline

def make_order(indegree, team, n, graph):
    for i in range(n):
        for j in range(i + 1, n):
            indegree[team[j]] += 1
            graph[team[i]].append(team[j])

def topology_sort(indegree, graph, n):
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 0
    while q:
        cnt += 1
        curr = q.popleft()
        result.append(curr)
        zero_indegree_exist = False
        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                if zero_indegree_exist:
                    return "?"
                q.append(i)
                zero_indegree_exist = True

    if cnt != n:
        return "IMPOSSIBLE"
    return " ".join(str(i) for i in result)

T = int(input())
answers = []
for _ in range(T):
    n = int(input())
    indegree = [0] * (n + 1)
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    make_order(indegree, team, n, graph)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        else:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1

    answers.append(topology_sort(indegree, graph, n))

for ans in answers:
    print(ans)
```

### ❗️ 결과

성공 (일부 구글링)

### 💡 접근

위상정렬을 이용하는 문제였다. 유지되어야 하는 순서 조건이 존재하기 때문이다.

초기 상태를 살펴보자.

```
5→4→3→2→1

# indegress
[4,3,2,1,0] # 각각 1,2,3,4,5
```

위상 정렬 알고리즘에서 indegree(진입 차수)를 구하기 때문에, 계산해보면 위와 같다.

문제에서 순위 변동이 일어난 두 팀의 정보가 주어진다. 그럼 두 팀 사이의 화살표 방향을 바꿔주면 된다. 즉 기존의 진입차수를 제거하고, 역으로 더해주면 된다.

위상정렬 알고리즘을 통해 답을 구하다 예외 상황이 생길 수 있는데, 이는 각각 다음에 해당된다.

- 모든 노드를 queue에 넣기 전에 queue가 비어 while 빠져나옴
    - → 일관성이 없는 데이터이므로 답은 IMPOSSIBLE
- 진입 차수가 0인 노드가 둘 이상 queue에 들어감
    - → 순서를 확정할 수 없으므로 답은 ?
- 나머지 경우는 정상적으로 위상정렬이 수행되므로 그 결과가 답이다

## 🥳 문제 회고

위상 정렬을 처음 공부해서 바로 떠올리기 어려웠다. 게다가 문제를 잘 못 읽어서 구글링을 한 뒤에 실수를 인지했다. 문제를 잘 읽자!

# 17472 : 다리 만들기 2
- 출처 : 백준 (삼성)
## 😎 Solved Code

### 💻 Code

```python
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = int(1e9)

# input
n, m = map(int, input().split())
islands = [set() for _ in range(8)]  # 해안가 좌표 저장
B = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
bridges = [[INF] * 8 for _ in range(8)]
num = 2

def inside_boundary(y, x):
    return (0 <= y < n) and (0 <= x < m)

def bfs(y, x):
    q = deque([])
    q.append((y, x))
    visited[y][x] = True
    B[y][x] = num
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inside_boundary(ny, nx) and B[ny][nx] == 1 and not visited[ny][nx]:
                q.append((ny, nx))
                B[ny][nx] = num
                visited[ny][nx] = True
            elif inside_boundary(ny, nx) and B[ny][nx] == 0:  # 인접한 곳이 바다라면 해안가
                islands[num].add((y, x))
    return

def bridge_from_a_to_b(a, b, colwise):
    (ay, ax), (by, bx) = a, b
    cnt = 0
    if colwise:  # 세로 다리
        for i in range(1, (by - ay)):
            ay += 1
            if not inside_boundary(ay, ax) or B[ay][ax] != 0:
                return INF
            cnt += 1
    else:  # 가로 다리
        for i in range(1, (bx - ax)):
            ax += 1
            if not inside_boundary(ay, ax) or B[ay][ax] != 0:
                return INF
            cnt += 1
    return cnt

def get_all_bridge(a, b):
    a_beach, b_beach = list(islands[a]), list(islands[b])

    for ay, ax in a_beach:
        for by, bx in b_beach:
            if ay != by and ax != bx:
                continue
            elif ay == by:  # 가로 방향 일치
                if ax < bx:
                    bridge = bridge_from_a_to_b((ay, ax), (by, bx), False)
                else:
                    bridge = bridge_from_a_to_b((by, bx), (ay, ax), False)
            elif ax == bx:  # 세로 방향 일치
                if ay < by:
                    bridge = bridge_from_a_to_b((ay, ax), (by, bx), True)
                else:
                    bridge = bridge_from_a_to_b((by, bx), (ay, ax), True)

            # bridge 길이 갱신
            if bridge > 1:
                bridges[a][b] = min(bridges[a][b], bridge)
                bridges[b][a] = min(bridges[b][a], bridge)
    return

# start
for i in range(n):
    for j in range(m):
        if B[i][j] == 0:
            continue
        if B[i][j] == 1:
            bfs(i, j)
            num += 1

# 임의의 두 섬을 잇는 최소비용의 다리 구하기
for a, b in combinations([x for x in range(2, num)], 2):
    get_all_bridge(a, b)

# kruskal 알고리즘 으로 최소 신장 트리 찾기
parents = [0] * 8
for i in range(8):
    parents[i] = i

edges = []
for i in range(2, num):
    for j in range(2, num):
        if i < j and bridges[i][j] != INF:
            edges.append((bridges[i][j], i, j))

edges.sort()

def find_parent(i):
    if parents[i] != i:
        parents[i] = find_parent(parents[i])
    return parents[i]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return

result = 0
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

parent_node = find_parent(2)
for i in range(3, num):
    if find_parent(i) != parent_node:
        result = -1

print(result)
```

### ❗️ 결과

성공

### 💡 접근

bfs로 각 섬마다 넘버링을 해준다. 주어진 Input이 육지는 1로 표시되어있기 때문에 넘버링을 2부터 해준다.

그럼 지도(B)에 각 육지마다 2,3,4,…로 구분이 된다. bfs 과정에서 `해안가` 좌표를 set으로 따로 저장한다.

해안가는 바다와 인접한 육지라고 정의했다. 이는 나중에 임의의 두 섬을 잇는 최소 길이의 다리를 구할 때 쓰인다.

이제 임의의 두 육지를 combinations로 선택한다. 그리고 각 육지의 해안가 정보들을 가져온다. 하나하나 좌표를 비교해보며 가로 또는 세로 다리를 놓을 수 있는지 전부 순회한다. 매 순회마다 `min()` 함수를 이용해 최소 길이의 다리를 저장한다.

이제 임의의 두 육지(노드) 사이의 최소 거리 다리(간선) 정보가 준비되었다. 남은 작업은 크루스칼 알고리즘으로 최소 신장 트리를 구하면 된다.

## 🥳 문제 회고

어떻게 접근할지 방향을 잡는 과정은 어렵지 않았지만, 구현 내용이 많아서 상당히 버거웠다.

# 19237 : 어른 상어
- 출처 : 백준 (삼성)
## 😎 Solved Code

### 💻 Code

```python
import sys

input = sys.stdin.readline

# static variables
NULL = -1
DIRECTION, COORDINATE = 0, 1
NUMBER, TIME = 0, 1
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
dy = [NULL] + [-1, 1, 0, 0]
dx = [NULL] + [0, 0, -1, 1]

# variables
time = 0

# inputs
n, m, k = map(int, input().split())
sharks = [NULL] * (m + 1)
outs = [False] * (m + 1)

B = []
for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 0:
            tmp[x] = [tmp[x], -k]
            continue
        sharks[tmp[x]] = [NULL, (y, x)]  # (현재 방향, 현재 좌표)
        tmp[x] = [tmp[x], 0]  # (상어 번호, 냄새 뿌린 시각)
    B.append(tmp)

dirs = [NULL] + list(map(int, input().split()))
for i in range(1, m + 1):
    sharks[i][DIRECTION] = dirs[i]

priorities = [[NULL] * 5 for _ in range(m + 1)]

for i in range(1, m + 1):
    for dir in [UP, DOWN, LEFT, RIGHT]:
        priorities[i][dir] = list(map(int, input().split()))

# start
def only_number_one_left():
    for i in range(2, m + 1):
        if not outs[i]:
            return False
    return not outs[1]

def inside_boundary(y, x):
    return (0 <= y < n) and (0 <= x < n)

def is_no_scent(y, x):
    return B[y][x][TIME] + k <= time

def is_my_scent(y, x, num):
    return B[y][x][NUMBER] == num

def get_next_cell(num, coordinate, prior):
    (y, x) = coordinate
    no_scents, my_scents = [], []
    for dir in prior:
        ny, nx = y + dy[dir], x + dx[dir]
        if not inside_boundary(ny, nx):
            continue
        if is_no_scent(ny, nx):
            no_scents.append((ny, nx, dir))
        elif is_my_scent(ny, nx, num):
            my_scents.append((ny, nx, dir))

    if len(no_scents) > 0:
        return no_scents[0]
    else:
        return my_scents[0]

def move(next_cells):
    for num in range(1, m + 1):
        if next_cells[num] == NULL:
            continue
        (ny, nx, ndir) = next_cells[num]
        if is_no_scent(ny, nx) or is_my_scent(ny, nx, num):
            B[ny][nx][NUMBER] = num
            B[ny][nx][TIME] = time + 1
            sharks[num][DIRECTION] = ndir
            sharks[num][COORDINATE] = (ny, nx)
        else:
            outs[num] = True
            sharks[num] = (NULL, (NULL, NULL))
    return

while time <= 1000 and not only_number_one_left():
    next_cells = [NULL] * (m + 1)
    for num in range(1, m + 1):
        if outs[num]:
            continue
        direction, coordinate = sharks[num]
        prior = priorities[num][direction]
        # 다음으로 이동할 위치 구한 뒤 저장
        (ny, nx, ndir) = get_next_cell(num, coordinate, prior)
        next_cells[num] = (ny, nx, ndir)

    # 실제 이동 처리
    move(next_cells)
    time += 1

if time == 1001:
    print(-1)
else:
    print(time)
```

### ❗️ 결과

성공

### 💡 접근

구현은 사실 시키는 대로만 하면 되기 때문에 작업의 순서가 정해져 있다. 다만 해당 작업을 어떻게 **쉽고 빠르게** 구현할지가 관건인 것 같다.

이번 문제를 풀면서 적용한 몇가지 아이디어를 기록해보겠다.

1) [ 인덱스를 1부터 시작하게 설정 ]

간혹 0이 아닌 1부터 인덱스가 시작할 때가 있다.

이번 문제에서 위, 아래, 오른쪽, 왼쪽이 각각 1,2,3,4 였다. 인덱싱을 쉽게 하기 위해 다음과 같이 더미 데이터를 추가할 수 있다.

```python
dy = [NULL] + [-1, 1, 0, 0]
dx = [NULL] + [0, 0, -1, 1]
```

물론 1씩 빼서 0,1,2,3 으로 저장할수도 있다. 그런데 조건이랑 달라진 구현때문에 혼란이 올 때가 있다.

2) [ 변수를 상수처럼 사용 ]

```python
# static variables
NULL = -1
DIRECTION, COORDINATE = 0, 1
NUMBER, TIME = 0, 1
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
```

좋은 방법인지 아닌지는 모르겠지만, 나는 구현을 풀다보면 헷갈려서 이런 상수들을 선언한다.

sharks[i][0]과 sharks[0][1]이 구분이 어렵기 때문에, sharks[i][DIRECTION], sharks[i][COORDINATE] 로 접근하려는 것이다.

3) [ 문제를 내 상황에 맞게 변형하기 ]

이번 문제 조건중에 k초가 흐르면 냄새가 사라진다는 것이 있다. 이를 정직하게 구현하면 조금 어지러워진다.

 2차원 리스트에 각 냄새가 남은 시각을 k초부터 기록하고, 매 시간이 지날 때마다 모두 순회하며 `k -= 1` 을 해야한다. 이는 비효율적이다.

나는 그냥 냄새가 뿌려진 **시각**을 기록했다. 그리고 나중에 상어가 이동하며 현재 시각 대비 k초 이상의 과거의 cell은 냄새가 사라진거라 생각할 수 있다.

그리고 초기값이 0인 경우는 시간을 `-k` 로 설정해야 문제가 발생하지 않는다.

## 🥳 문제 회고

이번에 상어 시리즈 풀면서 가장 어려웠던 문제중 하나다. 구현은 잘 풀다가도 까딱하면 나락가는 것 같다…

# 17822 : 원판 돌리기
- 출처 : 백준 (삼성)
## 😎 Solved Code

### 💻 Code

```python
import sys
from collections import deque

input = sys.stdin.readline
X = 0
ALL_ZERO = -1

# inputs
n, m, t = map(int, input().split())
B = [deque(list(map(int, input().split()))) for _ in range(n)]
B = [[]] + B  # dummy 추가

tasks = [list(map(int, input().split())) for _ in range(t)]

def rotate(x, d, k):
    shift_num = k % m if k != 1 else 1
    if d == 1:
        shift_num = (m - shift_num) % m
    for i in range(x, n + 1, x):
        for _ in range(shift_num):
            elem = B[i].pop()
            B[i].appendleft(elem)
    return

def average():
    total = 0
    cnt = 0
    for i in range(1, n + 1):
        for j in range(m):
            if B[i][j] == X:
                continue
            total += B[i][j]
            cnt += 1
    if cnt == 0:
        return ALL_ZERO
    return total / cnt

def check_adjacent():
    candidate = set()
    for i in range(1, n + 1):
        curr, next = 0, 1
        for _ in range(m):
            if B[i][curr] == B[i][next] and B[i][curr] != X:
                candidate.add((i, curr))
                candidate.add((i, next))
            curr = next
            next += 1
            if next == m:
                next = 0

    # colwise
    for j in range(m):
        curr, next = 1, 2
        for _ in range(1, n):
            if B[curr][j] == B[next][j] and B[curr][j] != X:
                candidate.add((curr, j))
                candidate.add((next, j))
            curr = next
            next += 1

    candidate = list(candidate)
    for y, x in candidate:
        B[y][x] = X

    return len(candidate) > 0

is_all_zero = False
for x, d, k in tasks:
    rotate(x, d, k)
    is_deleted = check_adjacent()
    if not is_deleted:
        avg = average()
        if avg == ALL_ZERO:
            is_all_zero = True
            break
        for i in range(1, n + 1):
            for j in range(m):
                if B[i][j] == X:
                    continue
                if B[i][j] > avg:
                    B[i][j] -= 1
                elif B[i][j] < avg:
                    B[i][j] += 1

answer = 0
if not is_all_zero:
    for i in range(1, n + 1):
        answer += sum(B[i])
print(answer)
```

### ❗️ 결과

성공

### 💡 접근

핵심 아이디어 몇 개만 기록해보겠다.

1) rotate() 함수 구현 (회전)

회전할 때 모듈러 연산을 하면 최소 회전 횟수를 구할 수 있다. 원순열이기 때문에 사이클이 존재하기 때문이다.

또한 데이터는 `deque` 을 사용해 큐로 저장했다. 리스트와 달리 double linked list로 구현되어 있어서 맨 끝과 맨 처음 원소 push / pop 이 O(1)이기 때문이다.

2) 인접한 수들 X 처리

생각보다 고민을 많이하게 하는 구현이었다. 오리지널 투 포인터를 사용하려 했는데, 익숙하지 않아서 포기했다… 대신 `sliding window`라는 기법을 사용했다. 일종의 투 포인터이긴 한데 길이 L 짜리 윈도우를 가지고 순회하며 체크하는 것이다. 

우린 인접한 수를 체크해야 하므로 window size를 2로 잡는다. 그럼 야금야금 인접한 두 노드들을 계속해서 체크할 수 있다. 그러다가 같은 수가 나오면 두 좌표를 저장한다.

이 때, 리스트에 해당 좌표를 저장하면 데이터의 중복이 생긴다. 따라서 `set()` 자료구조에 담아서 중복을 피했다.

## 🥳 문제 회고

이번 주차 문제중 그나마 쉬워보였지만,,, 역시나 오래 걸렸다