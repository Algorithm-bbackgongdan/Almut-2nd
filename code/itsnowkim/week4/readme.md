# week 4 - 최단경로, 그래프 이론

## 최단경로
최단 거리 알고리즘
- 다익스트라
- 플로이드 워셜
- 벨만 포드
그리디 알고리즘 + 다이나믹 프로그래밍 알고리즘이 최단 경로 알고리즘에 적용됨.

### 다익스트라 최단 경로 알고리즘
그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘.
다익스트라 최단 경로 알고리즘은 '음의 간선'이 없을 때 정상적으로 동작한다. 음의 간선이란 0보다 작은 값을 가지는 간선을 의미.
현실 세계의 길(간선)은 음의 간선으로 표현되지 않으므로 다익스트라 알고리즘은 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.

기본적으로 그리디 알고리즘으로 분류됨.
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 위 과정에서 3과 4 반복

핵심은 다음과 같다. **"각 노드에 대한 현재까지의 최단 거리" 정보를 매 loop마다 업데이트한다.**

책에서 본 웃긴 말
>시험을 준비하는 여러분은 "구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드" 를 정확히 이해하고 구현할 수 있을 때까지 연습해야 한다.
특히 알고리즘 대회를 준비하는 독자라면 다익스트라 최단 경로 알고리즘은 자다가도 일어나서 바로 코드를 작성할 수 있을 정도로 코드에 숙달되어 있어야 한다.

1. 간단한 다익스트라 알고리즘 O(V^2) V=노드의 개수
```python
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

"""
[input]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

[output]
0
2
3
1
2
4
"""
```
전체 노드의 개수가 5000개 이하라면 일반적으로 위 코드 이용, 하지만 10000개를 넘어갈 경우 개선된 다익스트라 이용.

2. 개선된 다익스트라 알고리즘 O(ElogV) V=노드의 개수, E=간선의 개수
힙 자료구조를 사용한다. 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다. 이 과정에서 로그 시간이 걸린다.

```python
import heapq
import sys
imput = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0이며, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

### 플로이드 워셜
다익스트라의 경우 하나의 노드에서 다른 노드까지의 최단거리를 계산하는 알고리즘.
플로이드 워셜의 경우 모든 노드의 최단 거리를 계산한다.
따라서 최종 output 도 2차원 배열.

알고리즘에서도 차이가 있다.
다익스트라의 경우 "해당 노드에서 갈 수 있는 다른 노드까지의 최단 거리" 를 계산한 후, 업데이트하지만, 플로이드 워셜의 경우 "해당 노드를 거쳐갈 수 있는 모든 경로에 대한 최단 거리" 를 업데이트한다.

따라서 기존에는 greedy 방식이었다면, 플로이드 워셜의 경우 dynamic programming 기법으로 문제를 푼다.
시간 복잡도는 O(N^3) 이다.

```python
INF = int(1e9)
# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값들을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C로 설정
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한 출력
        if graph[a][b] == INF:
            print('INFINITY',end=" ")
        else:
            print(graph[a][b],end=" ")
    print()
```

## 그래프 이론
앞에서 배운 여러 알고리즘을 활용하여 기본적인 kruskal 알고리즘과 위상 정렬 알고리즘에 대해 공부한다.

그 전에 기초가 되는 "Union-Find 알고리즘" 에 대해 다룬다.

### Union-Find
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 출력
print('부모 테이블 : ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
```

`find_parent` 의 시간 복잡도가 최악의 경우 O(V) 인 일렬로 길게 늘어진 linked list 형태가 될 수 있어서, 경로 압축 기법을 적용한다. (Path Compression)

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```

- 서로소 집합을 활용하여 "무방향 그래프 내에서의 사이클 판별"을 할 수 있다.
- 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.

### 서로소 집합을 활용한 cycle 판별 - 무방향 그래프에서만 적용 가능
핵심 : 간선들을 순차적으로 탐색하면서 root 노드를 업데이트 해 주고, 같은 root 노드를 가지는 노드들은 cycle이 발생한 것.

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int, input().split())
parent = [i for i in range(v+1)]# 부모 태이블 초기화

cyle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
```

### 신장 트리 (Spanning Tree) - Kruskal Algorithm
최소 비용의 신장 트리를 만드는 목적이다.
다음과 같은 스텝으로 이루어집니다.
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int, input().split())
# 부모 테이블 초기화
parent = [i for i in range(v+1)]

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 
for edge in edges:
    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
```

### 위상 정렬 (Topology Sort)
위상 정렬은 정렬 알고리즘의 일종이다.
순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
**"방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것"**

1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

알고리즘에서도 확인할 수 있듯이 큐가 빌 때까지 큐에서 원소를 계속 꺼내서 처리하는 과정을 반복한다. 이 때 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
사이클이 존재하는 경우 사이클에 포함되어 있는 원소 중에서 어떠한 원소도 큐에 들어가지 못하기 때문이다.(진입차수가 0이 될 수 없으므로)
다만, 기본적으로 위상 정렬 문제에서는 사이클이 발생하지 않는다고 명시하는 경우가 더 많으므로, 여기서는 사이클이 발생하는 경우는 고려하지 않으며 2절의 실전 문제에 사이클이 발생하는 경우를 처리하는 문제를 수록하였다.

```python
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A 에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end= ' ')

topology_sort()
```

# 문제풀이

## 최단거리찾기2 - boj_11779
다익스트라 알고리즘을 활용해서 최단 거리를 찾으면 되는 문제였다.
경로까지 추가로 찾아야 하기 때문에, 최단 거리를 업데이트 해 줄 때 해당 노드를 경로에 추가하는 방식으로 구현하였다.
쉽게 풀 수 있는 문제였다.

## 운동 - boj_1956
사이클이 생기는 경우를 찾고, 해당 경우들에 대해 최단 경로를 출력하는 문제이다.
먼저 방향성이 있는 그래프이므로 사이클이 있는지 체크하기 위해서는 두 가지 방법이 존재한다.
1. 위상 정렬을 통해 사이클이 있는지 체크한다.
2. DFS 를 이용해 사이클이 있는지 체크한다.

2번을 통해 각 노드들에 대해 사이클 여부를 먼저 파악한 후, 사이클이 있다면 같은 그룹으로 묶어서 해당 그룹의 비용을 계산한 후,
각 그룹의 비용 최솟값을 출력하면 문제에서 요구하는 조건을 만족하는 답을 구할 수 있다.


## 주차 요금 계산 - prog_92341
문제 조건에 따라 구현만 하면 되는 문제였다.
상황도 납득 가능하게 잘 주어져서 쉽게 풀 수 있었지만, 하루동안의 금액을 계산할 때 하루 전체의 시간을 누적합으로 하여 요금을 부과하는 부분에서 실수가 있어서 디버깅에 시간이 쓰였다.
이러한 구현 문제가 나올 때는 문제를 천천히 읽더라도 실수 없이 읽는 것이 중요하다는 것을 느꼈다.

## 양궁대회 - prog_92342
어렵다.
단순히 모든 경우의 수에 대해서 이길 수 있는 경우를 찾은 후 최대로 이기면서, 낮은 점수가 많은 것을 찾을 수 있지만, 이렇게 할 경우에 시간복잡도가 너무 커져서 불가능하다. 따라서 다른 방법으로 접근해야 하는데, 해법이 greedy라고 생각했다.

