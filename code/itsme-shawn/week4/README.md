# 2주차

## 1. 백준\_최소비용 구하기2 (11779)

### 아이디어

#### 다익스트라 알고리즘

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드들 중, 최단 거리가 가장 짧은 노드를 선택한다. (그리디)
4. 선택한 노드를 거쳐서 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다. (dp)
5. 3-4번을 반복한다.

다익스트라에서 방문하지 않은 노드들 중, 최단거리가 가장 짧은 노드를 선택해야 한다.

방법1. 최단거리가 가장 짧은 노드를 최단 거리 테이블(리스트)에서 매번 찾아냄 : $O(V)$

방법2. 최단거리가 가장 짧은 노드를 최소 힙(우선순위 큐)에서 찾아냄 : $O(logV)$

방법1 로 최종 구현 시 ⇒ $O(V^2)$

방법2 로 최종 구현 시 ⇒ $O(E *logV)$

따라서 일반적으로 우선순위 큐를 사용하는 것을 추천합니다

#### 경로 계산

다익스트라 로직 안에서 path_node 라는 변수에 자신노드(이전 정보) 를 저장함으로써 경로를 역추적 가능하게 함

### 코드

```python
import heapq as hq
import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = dict()

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b, w = map(int, read().split())
    graph[a].append((b, w))

start, end = map(int, read().split())

MAX = int(1e9)
distance = [MAX] * (n + 1)
path_node = [0] * (n + 1)


def dijkstra(start):
    q = []  # (시작정점으로부터의 거리, 노드번호) 를 저장할 최소 힙
    # pop 시 거리가 작은 순으로 pop 됨

    # 시작점 세팅
    distance[start] = 0  # 시작점의 거리는 0
    hq.heappush(q, (0, start))  # 힙에 시작점 push

    while q:
        dist, cur = hq.heappop(q)  # 최소 힙에서 (거리,노드번호) pop

        # 현재 노드가 처리되지 않은 노드여야함
        if dist <= distance[cur]:  # pop한 노드의 거리 <= 최단거리 테이블 상에 기록된 거리
            for i in graph[cur]:  # i[0] : 인접노드번호, i[1] : 거리
                cost = dist + i[1]  # 현재노드를 거쳐갈 경우의 거리 계산
                if cost < distance[i[0]]:  # 새롭게 계산한 거리가 작을때만 갱신
                    distance[i[0]] = cost  # 거리테이블 갱신
                    path_node[i[0]] = cur  # 이전노드 정보 저장
                    hq.heappush(q, (cost, i[0]))  # 갱신 노드의 거리와 노드번호를 heap 에 push


dijkstra(start)


print(distance[end])


path = [end]
now = end
while now != start:  # path_node를 역추적해나가면서 경로 얻음
    now = path_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(" ".join(map(str, path)))

```

## 2. 백준\_운동 (1956)

### 아이디어

플로이드-와샬 알고리즘 예제

### 코드

```python
import sys

read = sys.stdin.readline

V, E = map(int, read().split())
MAX = 1e9
dis = [[MAX] * (V + 1) for _ in range(V + 1)]  # 2차원배열 초기화

# 그래프 생성
for i in range(E):
    a, b, c = map(int, read().split())  # a : 시작노드, b : 도착노드, c : 가중치
    dis[a][b] = c

# 플로이드-와샬
for k in range(1, V + 1):  # k : 중간노드
    for i in range(1, V + 1):  # i : 시작노드(행)
        for j in range(1, V + 1):  # j : 도착노드(열)
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

# 출력
ans = MAX
for i in range(V + 1):
    ans = min(ans, dis[i][i])  # dis[i][i] : 사이클 (시작점 ~ 시작점)


if ans == 1e9:  # 최소값이 없으면 -1 출력
    print(-1)
else:
    print(ans)

```

### 회고 및 코멘트

python3는 시간초과가 떠서 pypy3 로 통과했다.
다익스트라로 풀면 python3 로도 통과할 수 있다고 한다.
플로이드 와샬은 구현이 쉽긴하지만 시간복잡도가 $O(V^3)$ 이기 때문에 V 가 조금만 커져도 시간초과가 뜰 수 있다.

## 3. 프로그래머스\_주차 요금 계산 (92341)

### 아이디어

IN 일 때만 차 번호를 키 값으로 하는 딕셔너리에 (들어온 시간, 누적 주차시간) 아이템을 저장한다.

OUT 일 때는 해당 차 번호의 들어온 시간을 초기화시켜주고, 누적 주차시간을 계산한다.

### 코드

```python
# 주차 요금 계산


def get_parkingtime(in_time, out_time):
    in_time_to_minute = int(in_time[0:2]) * 60 + int(in_time[3:])
    out_time_to_minute = int(out_time[0:2]) * 60 + int(out_time[3:])

    return out_time_to_minute - in_time_to_minute


def get_totalfee(total_minute, fees):
    basic_time, basic_price, new_time, new_price = fees
    if total_minute <= basic_time:
        return basic_price
    else:
        if (total_minute - basic_time) % new_time == 0:
            add_price = int((total_minute - basic_time) / new_time) * new_price
        else:
            add_price = int((total_minute - basic_time) / new_time + 1) * new_price
        return basic_price + add_price


def solution(fees, records):
    answer = []

    dic = dict()  # 누적계산용
    lst = []

    for record in records:
        time, car_num, detail = record.split()

        # IN
        if detail == "IN":
            if car_num in dic:
                dic[car_num][0] = time

            else:
                dic[car_num] = [time, 0]  # (들어온 시간, 누적 주차시간)

        # OUT
        elif detail == "OUT":
            dic[car_num][1] += get_parkingtime(dic[car_num][0], time)
            dic[car_num][0] = False

    # 요금 계산하면서 출차 안 한 차도 같이 처리
    for car_num in dic:
        if dic[car_num][0]:
            dic[car_num][1] += get_parkingtime(dic[car_num][0], "23:59")
            dic[car_num][0] = False

    lst = sorted(dic.items())
    print(lst)

    for l in lst:
        answer.append(get_totalfee(l[1][1], fees))

    print(answer)

    return answer

```

### 회고 및 코멘트

맨 처음에 스택이나 큐 같은 자료구조를 사용하려고 했었는데 구현을 하다보니 일반적인 딕셔너리로 하는 것이 더 수월한 것 같아서 수정하였다.

## 3. 프로그래머스\_양궁대회 (92342)

### 아이디어

### 코드

```python
# 양궁대회
def solution(n, info):
    print()
    print(info)
    possible_answer = []
    result = []
    ryan_possible_info = []  # 10점 ~ 1점
    for i in range(len(info)):
        ryan_possible_info.append([0, info[i] + 1])

    print(ryan_possible_info)

    for i in range(0b11111111111 + 0b1):
        bin_to_str = ("0" * 10 + str(bin(i))[2:])[-11:]
        temp = []
        for j in range(11):
            temp.append(ryan_possible_info[j][int(bin_to_str[j])])

        result.append(temp)

    maxx = 0

    for res in result:
        apeach_score, ryan_score = 0, 0
        if sum(res) > n:
            continue
        else:
            # print("res1", res)
            for i in range(11):
                if info[i] == 0 and res[i] == 0:
                    pass
                elif info[i] < res[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i

            # print("r,a", ryan_score,apeach_score)

            if ryan_score - apeach_score >= maxx:
                maxx = ryan_score - apeach_score
                # print("res2", res)
                possible_answer.append([maxx, res])

    max_results = []

    for ans in possible_answer:
        if ans[0] == maxx:
            max_results.append(ans[1])

    # max_results.sort(key=lambda x : (-x[-1],-x[-2],-x[-3],-x[-4],-x[-5],-x[-6],-x[-7],-x[-8],-x[-9],-x[-10],-x[-11]))
    max_results.sort(key=lambda x: tuple(-x[(-1) * i] for i in range(1, 12)))
    print(max_results)
    # 예시 : [[1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0], [1, 1, 2, 3, 0, 2, 0, 0, 0, 0, 0]]

    if maxx == 0:
        return [-1]
    else:
        ans = max_results[0]
        if sum(ans) < n:
            ans[-1] += n - sum(ans)
        return ans

```

### 회고 및 코멘트
