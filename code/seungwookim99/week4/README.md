# Week4
최단거리 알고리즘 까먹지 말자!!
## 다익스트라(Dijkstra)
- 특정 노드 -> 다른 모든 노드 까지의 최소 비용
- 시작 노드가 주어지는 경우 사용됨
- O(ElogV)
```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

"""
INPUT
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
"""
```
## 플로이드-워셜(Floyd-Warshall)
- 모든 노드 간 최소 비용
- O(V^3)
```python
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd-Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("X", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

"""
INPUT
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
```

# 1956: 운동
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(v + 1):
    graph[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(v + 1):
    for i in range(v + 1):
        for j in range(v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_value = INF
for i in range(1, v):
    for j in range(i + 1, v + 1):
        min_value = min(min_value, graph[i][j] + graph[j][i])
if min_value == INF:
    min_value = -1
print(min_value)
```

### ❗️ 결과

성공

### 💡 접근

플로이드-워셜 알고리즘으로 해결했다.

해당 알고리즘을 수행해 graph[i][j]에 i → j 로 가는 최소비용을 저장한다.

만약 사이클이 존재한다면 graph[i][j] 와 graph[j][i] 는 둘 다 INF가 아닐 것이다.

따라서 graph[i][j] + graph[j][i]의 최솟값을 구해주면 된다.

다만 시간초과가 발생해 불필요한 순회는 최소한으로 해야 했다.

```java
for i in range(1, v):
    for j in range(i + 1, v + 1):
```

이렇게 되면 모든 경우의 수를 중복 없이 최소한의 순회로 탐색하게 된다.

## 🥳 문제 회고

사이클이 생기는 의미를 고민하게 만드는 문제였다. 플로이드-워셜은 시간복잡도가 O(N^3)로 크기 때문에 시간초과가 발생하지 않게 주의해야 한다.

# 11779 : 최소비용 구하기 2
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
paths = [""] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, str(start)))
    distance[start] = 0
    paths[start] = str(start)
    while q:
        dist, now, path = heapq.heappop(q)
        if dist > distance[now]:  # 이미 방문함
            continue
        for i in graph[now]:  # 인접 간선 체크
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                paths[i[0]] = path + " " + str(i[0])
                heapq.heappush(q, (cost, i[0], paths[i[0]]))
    return

dijkstra(start)

print(distance[end])
print(len(paths[end].split(" ")))
print(paths[end])
```

### ❗️ 결과

성공

### 💡 접근

다익스트라로 문제를 해결했다. 

최소 비용을 구하는 것은 다익스트라 구현시 기본적으로 알 수 있는 내용이다.

방문하는 도시의 정보를 저장하기 위해 paths 라는 스트링 리스트를 만들었다.

start 도시 정보를 heap에 push 할 때 `paths[start] = str(start)` 도 넣어준다.

다익스트라 알고리즘을 수행하며 pop하면 해당 노드와 그 노드까지의 최단경로 (path)가 나온다. 인접 노드를 탐색하고 push를 할 때 `paths[i[0]] = path + “ “ + str(i[0])` 로 인접 노드까지의 최단거리를 갱신하고, 함께 튜플로 묶어 push해주면 된다.

가운데에 공백을 추가한 이유는 나중에 공백 기준으로 split 처리를 하기 위함이다.

## 🥳 문제 회고

기본적인 다익스트라 알고리즘이 학습되어 있다면 큰 무리없이 풀 수 있던 문제였다.

# 92341 : 주차 요금 계산
- 출처 : 2022 KAKAO BLIND RECRUITMENT
## 😎 Solved Code

### 💻 Code

```python
def parse_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def get_times_sum(times):
    res = 0
    for i in range(0, len(times), 2):
        res += times[i+1] - times[i]
    return res

def calc_fee(times, fees):
    times_sum = get_times_sum(times)
    res = fees[1]
    if times_sum <= fees[0]:
        return res
    res += ((times_sum - fees[0]) // fees[2])*fees[3]
    # 나머지 0이 아니면 올림처리 (단위 요금 추가)
    if (times_sum - fees[0]) % fees[2] != 0:
        res += fees[3]
    return res
    

def solution(fees, records):
    answer = []
    cars = dict()
    # dictionary에 차량 번호를 key로 시간 value들 저장
    for record in records:
        data = record.split(' ')
        time = parse_to_minutes(data[0])
        num = data[1]
        if num in cars.keys():
            cars[num].append(time)
        else:
            cars[num] = [time]
    
    # 출차 내역 없는 차량 23:59 추가
    out_time = parse_to_minutes('23:59')
    for num in cars.keys():
        if len(cars[num]) % 2 == 1:
            cars[num].append(out_time)
    
    # 차량 번호 오름차순대로 요금 추가
    for num in sorted(cars.keys()):
        answer.append(calc_fee(cars[num], fees))
    return answer
```

### ❗️ 결과

성공

### 💡 접근

딕셔너리를 사용해 records를 가공해 저장했다.

차량번호를 key로, 차량의 입/출차 시간들의 리스트를 value로 저장했다.

입/출차 시간은 분으로 parsing해서 저장했다.

저장 이후 리스트의 길이가 홀수라면 출차를 하지 않은 것이므로 ‘23:59’에 해당하는 시간을 뒤에 append 해주었다.

마지막으로 `sorted(cars.keys())` 을 순회하며 요금을 계산하여 answer에 저장했다.

## 🥳 문제 회고

자료의 저장에 신경을 써야했던 구현 문제였다. 어떻게 데이터를 저장할 지 전략을 잘 세우고 접근해야 헤매지 않을 것 같다.

# 92342 : 양궁대회
- 출처 : 2022 KAKAO BLIND RECRUITMENT
## 😎 Solved Code

### 💻 Code

```python
from itertools import product

def calc_can_win(ap, lion):
    # 두 과녁이 주어졌을 때 우승 여부와 점수차 계산
    score_ap, score_lion = 0, 0
    for i in range(11):
        if ap[i] == 0 and lion[i] == 0:
            continue
        if ap[i] >= lion[i]:
            score_ap += 10 - i
        else:
            score_lion += 10 - i
    return (True, score_lion - score_ap) if score_lion > score_ap else (False, 0)

def calc(case, info, min_shots, n):
    lion = [0]*11
    for i in range(11):
        if case[i] == False:
            continue
        if min_shots[i] <= n:
            lion[i] = min_shots[i]
            n -= min_shots[i]
    if n > 0:
        lion[-1] += n
    can_win, score = calc_can_win(info, lion)
    return (can_win, score, lion)

def sort_filtered(L):
    return sorted(L, key=lambda x: (-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1],-x[0]))

def solution(n, info):
    answer = []
    candidate = []
    min_shots = [0]*11
    for i in range(11):
        min_shots[i] = info[i] + 1 # 10-i 점을 얻을 수 있는 최소 화살 수
    
    for case in product([True, False], repeat=11):
        # 해당 case에 대해 이길 수 있는 방법, 점수 계산
        win, score, lion = calc(case, info, min_shots, n)
        if not win:
            continue
        candidate.append((score,lion))

    if len(candidate) == 0:
        return [-1]
    candidate = sorted(candidate, key=lambda x : -x[0]) # 점수로 내림차순 정렬
    max_score = candidate[0][0]
    
    # 최대점수차로 이길 수 있는 방법들 filter
    filtered = []
    for elem in candidate:
        if elem[0] != max_score:
            break
        filtered.append(elem[1])
    return sort_filtered(filtered)[0]
```

### ❗️ 결과

성공 (마음에 안듬)

### 💡 접근

처음에는 완전 탐색으로 접근했다. 그런데 마냥 완전 탐색 하기에는 경우의 수가 너무 많아보였다.

예제를 조금 더 분석해보니 방법을 찾았다.

어피치가 K점 과녁에 A발을 맞췄다면, 라이언이 K점을 따기 위해서는 최소 A+1 발을 맞춰야 한다.

또는 K점을 따지 않는다면 0발을 맞추는게 좋다. 굳이 1 ~ A-1발을 맞춰서 화살 수를 낭비할 필요가 없기 때문이다.

이렇게 되면 총 11개의 점수에 대해 라이언이 각 점수를 따거나 말거나에 대한 모든 경우의 수를 탐색하면 된다. 즉, 최대 4^11의 경우의 수가 나온다. 이를 product를 사용해서 순회했다.

각 경우마다 라이언이 이길 수 있다면 candidate 리스트에 (점수차, 맞추는 방법)을 append 한다.

그리고 candidate를 점수차에 대해 내림차순 정렬하고, 가장 최대 점수차를 가진 방법들만 필터링 한다. 이 중에서 **가장 낮은 점수를 가장 많이 맞춘** 방법을 선택하기 위해 `sort_filtered(L)` 를 호출하여 0번째 값을 답으로 리턴한다.

## 🥳 문제 회고

구현을 하다보니 너무 지저분하게 코드를 짠 것 같다. 위 코드에서는 4^11 모든 경우의 수에 대해 순회하기 때문에 애초에 불가능한 경우도 점수차를 계산한다. 예를 들어, N = 1 인데 10,9,8의 점수를 가져가는 방법은 절대 없음에도 점수차를 계산한다. 따라서 candidate에 중복값이 생기고 비효율적인 연산이 발생한다.

뭐 실전에서 맞으면 장땡이긴 하지만… 조금 더 간결하게 짤 수 있는 방법이 있을 것 같다. DFS를 쓰면 백트래킹을 사용해서 연산량을 대폭으로 줄일 수 있다.