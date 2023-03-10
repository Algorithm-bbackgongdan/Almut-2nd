# Week 1
## 파이썬 Unpacking (*)
리스트의 요소를 나열해주는 연산자로 이를 Unpacking 이라 한다.

예를 들어 product라는 함수는 여러개의 list를 매개변수로 받을 수 있다.
```python
product(list1, list2, list3, list4)
```
위와 같이 말이다. 이 예시는 list4 개를 명시적으로 매개변수로 넘겨준 경우다.
그런데 만약 넘겨줘야 하는 매개변수 개수가 가변적일 경우 어떻게 할까?
아래와 같이 Unpacking으로 처리할 수 있다.
```python
from itertools import product

a = [['1', '2', '3'], ['a', 'b']]

for i in product(*a):
    print(i)
'''
출력 결과
('1', 'a')
('1', 'b')
('2', 'a')
('2', 'b')
('3', 'a')
('3', 'b')
'''

```

# 2212: 센서 
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensors = set(map(int, sys.stdin.readline().rstrip().split()))  # 중복 제거
sensors = sorted(list(sensors))
totalRange = sensors[-1] - sensors[0]
distances = []
for i in range(1, len(sensors)):
    distances.append(sensors[i] - sensors[i - 1])
distances = sorted(distances, reverse=True)
kRange = min(K - 1, len(distances))
for k in range(kRange):
    totalRange -= distances[k]
print(totalRange)
```

### ❗️ 결과

성공

### 💡 접근

예제 입력 케이스를 노트에 쓰고 그려가며 예제 답안이 어떻게 나오는지 먼저 분석했다. 분석을 하며 실제 집중국이 세워지는 경우의 수가 여러개 나오는 것을 발견했다.

답이 될 수 있는 여러 경우의 수를 살펴보고 유추한 정보는 2가지였다.

1. 모든 집중국은 센서 위에 있다(아마도)
2. ***서로 거리가 먼 센서들을 하나의 집중국으로 커버하는 것은 반드시 비효율적이다***

이 중에서 2번 정보에 집중했다.

그럼 센서들을 X축에 오름차순으로 주욱 정렬 한 뒤에, 그 사이의 “간격”들을 계산해보면 뭔가 정보가 나올 것 같았다.

예제 1번의 센서들을 중복 제거한 뒤, 오름차순 정렬하여 간격을 측정한 것이다.

```
1--3---6-7--9 이런 형태로 센서가 배치되어있므로, 순서대로 간격을 리스트에 담으면
[2,3,1,2]
```

가장 큰 간격 `3`이 보인다. 딱 봐도 3번 센서와 6번 센서를 하나의 집중국이 커버하는 것은 비효율적이다. 그럼 {1,3}과 {6,7,9}로 나눠서 집중국이 관리할 수 있겠다. 이 상황은 집중국이 2개 사용된 상황이다.

그 다음으로 큰 간격 `2`가 보인다. 간격 2가 2개나 있기 때문에 두 번 더 쪼갤 수 있겠다. 즉, {1,3}과 {6,7,9}에서 {1},{3},{6,7},{9}로 나눠 4개의 집중국이 관리할 수 있을 것이다. 그런데 만약 K가 3이라서 최대 3개의 집중국을 사용할 수 있다면 어떻게 쪼개야 하는가..? 아래와 같이 두 가지 경우가 있을 것이다

1. {1},{3},{6,7,9}
2. {1,3},{6,7},{9}

두 경우의 수신가능 영역의 길이 합은 동일하게 3 이다. 즉, 어떻게 쪼개든 상관없다는 것이다.

이 쯤 되면 규칙을 발견할 수 있다.

1개의 집중국이 수신하는 범위 에서 간격들을 최대 K-1개만큼 빼면 답이 나온다.

즉, `1개의 집중국이 수신하는 범위` = `끝 센서 좌표` - `시작 센서 좌표` 이고, `간격`들을 내림차순 정렬 해 최대 K-1개만큼 빼면 된다.

## 🥳 문제 회고

 초반에 그리디 알고리즘을 적용하기 위한 “기준”을 잡는 데에 많은 시간을 쏟았다. 그리고 그 기준을 “센서 사이의 간격”으로 잡고 나서도 실제 구현하기 까지도 오랜 시간이 걸렸다.  구현이 흔히 말하는 피지컬의 구현은 아니지만, 아이디어를 적용하기 위한 구현 설계가 어려웠다는 뜻이다. 예를 들어, 내가 계속 헤맸던 부분은 “그리디 기준 잡은건 좋아. 그래서 집중국을 실제로 어느 위치에 세워야 하나?” 였다. 간격을 기준으로 센서들의 영역을 나누고, 그 영역 내부에서 실제로 집중국을 어느 위치에 세워야 하는지 엄청 고민했다. “영역에서 첫 번째로 등장하는 센서 위에 세워야 하나..?” 라는 식으로 말이다.

 도저히 답이 안나오는 것 같아서 다시 머리를 비우고 쉽게 접근해보고자 했다. 이번에는 집중국의 위치를 결정하지 말고 일단 간격에 따라 센서 영역들만 나눠보았다. 그랬더니 해답이 어느정도 보였다. 너무 특정 구현에 매몰되지 않고 문제의 본질에 집중해야겠다.

# 15683: 감시
- 출처 : 백준

 ## 😎 Solved Code

### 💻 Code

```python
import sys
import copy
from itertools import product

DIR = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)} # 동서남북
CCTV = [ # CCTV별 탐색 방향 정의
  [], 
  [('E'), ('S'), ('W'), ('N')], # 1번 cctv 
  [('E', 'W'), ('S', 'N')], # 2번 cctv
  [('E', 'S'), ('S', 'W'), ('W', 'N'), ('N', 'E')], # 3번 cctv
  [('E', 'S', 'W'), ('S', 'W', 'N'), ('W', 'N', 'E'), ('N', 'E', 'S')], # 4번 cctv
  [('E', 'S', 'W', 'N')] # 5번 cctv
]

def pickCCTVsDirections(cctvs):
    # CCTV들이 감시할 수 있는 방향들의 모든 경우의 수 (최대 4^8)
    res = []
    for (y, x, num) in cctvs:
        res.append(CCTV[num])
    return list(product(*res))

def out_of_range(y, x):
    # office 범위 벗어나는지 test
    return y < 0 or y >= n or x < 0 or x >= m

def calcMarkedPoints(office_):
    # '#'개수 계산 (cctv의 감시 구역 수)
    res = 0
    for i in range(n):
        for j in range(m):
            if office_[i][j] == '#':
                res += 1
    return res

def mark(y, x, dirs, office_):
    # dirs 정보에 맞게 cctv 감시 처리 ('#' 표시)
    for char in dirs:
        ny, nx = y, x
        dy, dx = DIR[char]
        while not out_of_range(ny + dy, nx + dx):
            ny += dy
            nx += dx
            if office_[ny][nx] == 0:
                office_[ny][nx] = '#'
            elif office_[ny][nx] == 6: # 벽을 만나면 너머로 감시 불가
                break

    return office_

def calcCoverSpots(cctvDir):
    # cctvDir 정보에 담긴 cctv들이 감시할 수 있는 영역 계산
    # (cctvDir는 각 cctv들이 탐색할 방향들에 대한 정보가 정의되어 있음)
    office_ = copy.deepcopy(office) # 원본 복사
    for idx, (y, x, num) in enumerate(cctvs):
        # idx 번째로 담긴 cctv의 방향 가져오기 (from cctvDir)
        dirs = cctvDir[idx]

        # office_ 에 # 마킹
        office_ = mark(y, x, dirs, office_)

    return calcMarkedPoints(office_)

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
office = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]

# cctv 위치 / 사각지대 개수 저장
blindSpotsNum = 0
cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            cctvs.append((i, j, office[i][j]))  # (y, x, cctv번호)
        elif office[i][j] == 0:
            blindSpotsNum += 1

candidate = []
for cctvDirs in pickCCTVsDirections(cctvs):
    candidate.append(blindSpotsNum - calcCoverSpots(cctvDirs))

print(min(candidate))
```

### ❗️ 결과

성공

### 💡 접근

전형적인 구현 문제이기 때문에 어떤 흐름으로 코드가 실행되어야 하는지 대략적으로 생각할 수 있었다.

1. 사무실 내 CCTV가 감시할 수 있는 모든 경우의 수를 구한다 (CCTV 종류별로 회전에 따른 감시 영역이 다르므로)
2. 경우의 수를 전부 순회하며 실제로 감시하는 영역을 ‘#’ 표시로 마킹한다
3. 남은 사각지대의 개수를 세고, 이것이 최솟값이라면 정답으로 업데이트 한다
4. 2로 돌아가 반복한다

다음으로 `CCTV마다 서로 다른 감시 방향` 을 어떻게 정의할지 고민했다. 아래와 같이 정리했다.

```python
DIR = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)} # 동서남북
CCTV = [ # CCTV별 탐색 방향 정의
  [], # 편리한 인덱스 접근을 위해 0번은 빈 리스트로 추가
  [('E'), ('S'), ('W'), ('N')], # 1번 cctv 
  [('E', 'W'), ('S', 'N')], # 2번 cctv
  [('E', 'S'), ('S', 'W'), ('W', 'N'), ('N', 'E')], # 3번 cctv
  [('E', 'S', 'W'), ('S', 'W', 'N'), ('W', 'N', 'E'), ('N', 'E', 'S')], # 4번 cctv
  [('E', 'S', 'W', 'N')] # 5번 cctv
]
```

- 동서남북에 대한 방향을 딕셔너리 형태로 DIR이라 정의했다. ‘E’, ‘S’, ‘W’, ‘N’을 key 값으로 갖고있다.
- CCTV마다 회전시 감시할 수 있는 방향에 대해 튜플의 리스트로 정의했다.
    - 예를 들어 2번의 경우 `동서` 또는 `남북` 으로 감시할 수 있다. 따라서 `[('E', 'W'), ('S', 'N')]` 와 같이 정의했다.

이제 cctv들이 감시할 수 있는 모든 경우의 수를 구해야 한다. 예를 들어 1,2,3 번 CCTV가 있다면 감시 방향/회전 을 고려한 모든 경우의 수는 4*2*4 일 것이다.

이 경우의 수는 `중복조합`으로 해결할 수 있기 때문에 itertools의 product를 사용했다.

남은 로직들은 최대한 함수로 분리해 구현했는데, 각 함수를 설명한 것이다.

1. pickCCTVsDirections(cctvs)
- 주어진 cctv들이 감시할 수 있는 모든 경우의 수를 2차원 리스트로 리턴한다.
    - ex. [  … , [(’E’), (’E’, ‘W’), (’E’, ‘S’) ], … ] 에서 [(’E’), (’E’, ‘W’), (’E’, ‘S’) ] 는 cctv 리스트에 저장된 cctv 순서대로 탐색 방향을 나타낸다.
1. calcCoverSpots(cctvDirs)
- cctv들이 감시할 수 있는 한 경우의 수에 대해 실제로 감시하는 영역의 개수를 리턴한다.
- cctvDirs는 pickCCTVsDirections(cctvs)의 반환값의 원소 중 하나다
1. mark(y,x,dirs,office_)
- (y,x)로부터 dirs 정보에 맞게 감시 영역을 ‘#’으로 마킹한다
    - ex. dirs == (’E’, ‘W’)
1. calcMarkedPoints(office_)
- 오피스 전체를 순회하며 ‘#’(감시되는 구역)의 개수를 센다

## 🥳 문제 회고

구현은 대부분 문제를 처음 보면 어떻게 풀 지 큰 흐름은 보인다. 그러나 실제로 코드로 어떻게 짜야 할 지 막막해진다.

그럴 때 바로 코드부터 작성하기 보다 최대한 자세히 논리를 정리하고, 자료를 저장하는 방식에 대해 고민 한 후에 `한 번에 잘 짜는것`이 중요한 것 같다.

왜냐하면 특히 구현은 요구사항대로 정직하게 짤수록 코드가 길어지기 마련인데, 실수가 나와 디버깅을 할 때 cost가 상당하기 때문이다.

이번 문제도 가장 많이 고민한 지점 중 하나가 `CCTV 정보를 저장하는 방법`과 `모든 경우의 수를 구하는 것` 이었다.

상당히 오랜 시간이 걸렸는데 너무 조급해하지 않고 빠르게 논리를 정리하는 훈련을 해야겠다.

# 150369 : 택배 배달과 수거하기
- 출처 : 프로그래머스
## 😎 Solved Code

### 💻 Code

```python
def findFarthestIndex(L):
    for i in range(len(L)-1, -1, -1):
        if L[i] > 0:
            break
    return i

def isWorkRemain(remainWorks):
    return remainWorks != 0

def work(workList, workIdx, cap):
    doneWorksNum = 0
    
    # 최대 cap 개수만큼 배달/수거 작업 수행
    while (workIdx >= 0) and (doneWorksNum != cap):
        if workList[workIdx] > 0:
            workList[workIdx] -= 1
            doneWorksNum += 1
        else:
            workIdx -= 1
    
    # 만약 workList[workIdx]가 0이라면, workList[workIdx] > 0 일 때 까지 workIdx 감소
    if (workIdx >= 0) and (workList[workIdx] == 0):
        while workIdx >= 0:
            if workList[workIdx] > 0:
                break
            workIdx -= 1
    
    return (doneWorksNum, workIdx)

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliverIdx = findFarthestIndex(deliveries)
    pickupIdx = findFarthestIndex(pickups)
    
    remainDeliver = sum(deliveries)
    remainPickups = sum(pickups)
    
    while (isWorkRemain(remainDeliver)) and (isWorkRemain(remainPickups)):        
        answer += 2 * (max(deliverIdx, pickupIdx) + 1)
        
        deliverDoneNum, deliverIdx = work(deliveries, deliverIdx, cap)
        pickupDoneNum, pickupIdx = work(pickups, pickupIdx, cap)
        
        remainDeliver -= deliverDoneNum
        remainPickups -= pickupDoneNum
    
    while isWorkRemain(remainDeliver):
        answer += 2 * (deliverIdx + 1)
        deliverDoneNum, deliverIdx = work(deliveries, deliverIdx, cap)
        remainDeliver -= deliverDoneNum
    
    while isWorkRemain(remainPickups):
        answer += 2 * (pickupIdx + 1)
        pickupDoneNum, pickupIdx = work(pickups, pickupIdx, cap)
        remainPickups -= pickupDoneNum
    
    return answer
```

### ❗️ 결과

성공

### 💡 접근

코드의 작동 흐름을 대략적으로 다음과 같이 정리했다.

1. 최대한 먼 곳부터 역순으로 최대한 많이 배달 처리 한다.
2. 최대한 먼 곳부터 역순으로 최대한 많이 수거 처리 한다.
3. `1,2 번 둘 중 더 먼 거리 * 2` 만큼 거리를 더해준다. (먼 곳을 가는 빈도를 줄여야 하므로. 그렇지 않으면 한 번 더 먼 곳을 가야해서 비효율적)
4. 1번부터 반복한다
5. 배달 / 수거 중 남은 업무가 있으면 마무리 한다.

배달과 수거 처리는 사실 같은 논리로 처리하므로 `work` 라는 함수로 정의했다. 아래는 work 함수의 대략적인 작동 방식이다.

```python
# <Case 1>
deliveries == [1,0,3,1,2], cap == 4
# 위와 같은 상황이라면 배달 업무를 하는 최초 인덱스는 4이고, 배달 처리를 하면 아래와 같아진다.
deliveries == [1,0,2,0,0]
# 뒤에서부터 최대 4개를 제거한 것이다. 그리고 배달 업무를 하는 인덱스는 2로 업데이트 된다.

# <Case 2>
pickups == [0,3,0,4,0], cap == 4
# 위와 같은 상황이라면 수거 업무를 하는 최초 인덱스는 3이고, 수거 처리를 하면 아래와 같아진다.
pickups == [0,3,0,0,0]
# 뒤에서부터 최대 4개를 제거한 것이다. 그리고 수거 업무를 하는 인덱스는 1로 업데이트 된다.
```

while 문에 남아있는 업무(배달/수거)가 있는지 체크하며 계속해서 work 함수를 수행한다. work를 수행하며 남은 업무 리스트를 업데이트 하며, 업무 시작 인덱스를 업데이트 한다.

## 🥳 문제 회고

생각보다 상당히 오래 걸렸다. 구현은 흐름을 잡는 것 자체는 어렵지 않은데 막상 구현하기 까지 많은 고민이 필요한 것 같다.

특히 work 내부 로직을 짜는 데에 많은 시간이 걸렸다.

- 뒤에서부터 최대 cap 개수만큼 -1 처리
- 해당 인덱스에 업무가 0이 되면 index를 앞으로 계속 이동시킴
- 만약 모든 업무가 끝났다면 반복문 탈출

과 같이 여러 조건을 고려해야 했기 때문에 디버깅에 시간이 걸렸다.

# 150368 : 이모티콘 할인행사
- 출처 : 프로그래머스
## 😎 Solved Code

### 💻 Code

```python
from itertools import product
DISCOUNT_RATE = [10,20,30,40]

def purchaseCost(wishRatio, emoticons, discountRatios):
    cost = 0
    for i in range(len(emoticons)):
        if discountRatios[i] >= wishRatio:
            cost += emoticons[i] * (100 - discountRatios[i]) // 100
    return cost

def solution(users, emoticons):
    candidate = []
    for discountRatios in product(DISCOUNT_RATE, repeat=len(emoticons)):
        plusMember = 0
        salesPriceSum = 0
        for (wishRatio, criteriaPrice) in users:
            costExpected = purchaseCost(wishRatio, emoticons, discountRatios)
            if costExpected >= criteriaPrice:
                plusMember += 1
            else:
                salesPriceSum += costExpected
        candidate.append((plusMember, salesPriceSum))
    candidate.sort(key = lambda x : (-x[0], -x[1]))
    return candidate[0]
```

### ❗️ 결과

성공

### 💡 접근

이모티콘 할인율은 10,20,30,40 중 가능하다. 따라서 각 이모티콘에 적용될 수 있는 할인율의 모든 경우의수를 구하고, 이를 순회하며 문제를 해결할 수 있겠다.

product로 `DISCOUNT_RATE` 라는 리스트에서 이모티콘 개수만큼 중복순열을 구했다.

그리고 각 경우마다 users를 순회하며 예상 구매가를 구했다. 이는 purchaseCost 함수에서 처리했다.

문제 조건대로 예상 구매가와 유저 자신의 기준가격을 비교하며 플러스 서비스 가입자를 늘리거나, 판매액을 더해주었다. 그리고 그 결과를 candidate 리스트에 튜플 형태로 담았다.

순회를 마치고 할인행사 목표의 우선순위에 맞게 candidate를 정렬했다.

1순위로 플러스 가입자에 대해 내림차순 정렬, 그리고 2순위로 판매액을 기준으로 내림차순 정렬했다.

## 🥳 문제 회고

전형적인 구현문제였다. 모든 겅우의 수를 고려해야 했던 문제다. 비교적 쉽게 해결했다.