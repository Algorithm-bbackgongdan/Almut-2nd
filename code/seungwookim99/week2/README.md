# Week 2

# 16234: 인구 이동 
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys
from collections import deque

def check_boundary(y, x):
    return 0 <= y < N and 0 <= x < N

def check_moveable(a, b):
    return L <= abs(a - b) <= R

def move():
    # unions에 저장된 정보를 바탕으로 인구이동 처리
    for (contries, population) in unions:
        for (y, x) in contries:
            world[y][x] = population

def union_exist(y, x):
    # (y,x)을 시작으로 연합국가가 존재하는지 bfs로 체크
    # 존재하면 (연합국들 좌표 리스트, 인구수 평균) 을 unions에 append 후 True 반환
    # 존재하지 않으면 False 반환
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    q = deque([(y, x)])
    contries = []
    populationSum = 0
    visited[y][x] = True

    while q:
        cy, cx = q.popleft()
        contries.append((cy, cx))
        populationSum += world[cy][cx]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if check_boundary(ny,nx) and not visited[ny][nx] and check_moveable(world[cy][cx], world[ny][nx]):
                visited[ny][nx] = True
                q.append((ny, nx))

    populationAvg = populationSum // len(contries)
    if len(contries) == 1:
        return False
    else:
        unions.append((contries, populationAvg))
        return True

N, L, R = map(int, sys.stdin.readline().rstrip().split(' '))
world = [ list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

days = 0
moveCanOccur = True

while moveCanOccur:
    moveCanOccur = False
    visited = [[False] * N for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and union_exist(i, j):
                moveCanOccur = True
    if moveCanOccur:
        move()
        days += 1
print(days)
```

### ❗️ 결과

성공

### 💡 접근

인접한 국가들과 연합이 될 수 있는지 여부를 확인해야 하기 때문에 BFS로 접근했다.

우선 NxN 의 국가들을 전부 순회한다.

해당 국가를 방문하지 않았다면 `union_exist`로 그 국가로부터 주변국들과 연합을 만들 수 있는지 확인한다.

`union_exist` 의 반환이 True라면 실제로 인구 이동이 발생할 것이므로 moveCanOccur 플래그를 True 처리한다

모든 순회 이후 moveCanOccur가 True 라면 실제 인구 이동을 수행하고, days를 증가시킨다.

여기에서 union_exist에선 BFS가 사용되었다. 시작 좌표로부터 BFS 탐색을 하며 조건에 맞다면 queue에 새로운 좌표를 추가한다.

queue에 새로운 좌표를 추가한다는 것은 시작 좌표의 국가와 연합이 될 수 있다는 것이다.

queue에 좌표가 추가되기 위한 조건은 다음과 같다.

- NxN boundary 내부에 존재
- 아직 방문 안 함
- L ≤ 인구수 차이 ≤ R

## 🥳 문제 회고

주변국들을 야금야금 탐색한다는 점에서 BFS로 해결할 수 있는 문제였다. 다만 여러 조건들이 붙어 구현의 역량도 요구되는 문제였다.

# 1744: 수 묶기 
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
ones = []
zeroExists = False
negatives = []
positives = []  # 2이상의 양수
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        zeroExists = True  # 0 존재 참
    elif num == 1:
        ones.append(num)
    elif num < 0:
        negatives.append(num)
    else:
        positives.append(num)

positives.sort(reverse=True)
negatives.sort()

answer = 0

for i in range(1, len(negatives), 2): # 절대값이 큰 두 수 순서대로 묶어주기
    answer += negatives[i] * negatives[i - 1]

# 음수 개수가 홀수고 0이 없다면 -> 가장 작은 음수를 더함
if (len(negatives) % 2 == 1) and not zeroExists:
    answer += negatives[-1]

for i in range(1, len(positives), 2): # 절대값이 큰 두 수 순서대로 묶어주기
    answer += positives[i] * positives[i - 1]

if len(positives) % 2 == 1:
    answer += positives[-1]
answer += sum(ones)
print(answer)
```

### ❗️ 결과

성공

### 💡 접근

예제 입력들과 몇몇 예시를 추가해 생각한 결과 수 종류마다 서로 다른 특징이 있음을 발견했다.

1. 음수/양수 각각 절댓값이 큰 두 수를 묶을수록 최대가 된다
2. 1은 묶지 말고 반드시 더해야 최대가 된다
3. 만약 음수가 홀수개수라면 두 가지 경우가 존재한다
    1. 0이 존재한다면, 절대값이 가장 작은 음수와 묶는다 → 0 x 음수 = 0
    2. 0이 없다면, 어쩔수 없이 그대로 더해준다

1번은 거의 자명하다. 음수 x 음수 = 양수로 만들되, 절댓값을 최대한 크게 만들수록 합이 커지기 때문이다.

2번도 거의 자명하다. 1 x N < N + 1 이기 때문이다

3번은 약간 고민이 필요했다. 음수가 짝수개라면 둘 씩 묶어 전부 양수의 합으로 바꿀 수 있다. 

하지만 음수가 홀수개라면 `절대값이 가장 작은 음수 1개`가 남는다. 문제의 목표는 합을 최대한 크게 만드는 것이므로, 음수를 더할수록 불리해진다.

만약 0이 존재한다면, 0과 그 음수를 묶어 음수를 없앨 수 있다.

0이 존재하지 않다면, 어쩔 수 없이 이 음수를 더해준다.

## 🥳 문제 회고

논리를 빈틈없이 정리 한 후 구현하니 실수가 없었다. 앞으로 수도코드를 먼저 짠 후에 코드로 옮겨야겠다.

# 150370 : 개인정보 수집 유효기간
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
def parseDateToDays(date):
    date_split = date.split('.')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])

    return day + 28 * month + 12 * 28 * year

def makeTermsDictionary(terms):
    res = {}
    for term in terms:
        type_ = term.split(' ')[0]
        month = int(term.split(' ')[1])
        res[type_] = month        
    return res

def solution(today, terms, privacies):
    answer = []
    parsedToday = parseDateToDays(today)
    termsDict = makeTermsDictionary(terms)
    for i, privacy in enumerate(privacies):
        date = privacy.split(' ')[0]
        parsedDate = parseDateToDays(date)
        type_ = privacy.split(' ')[1]
        expiration = termsDict[type_]
        
        if (parsedDate + 28 * expiration) <= parsedToday:
            answer.append(i+1)
    
    return answer
```

### ❗️ 결과

성공

### 💡 접근

오늘 날짜를 days 수로 바꾼다.

terms를 약관종류 - 유효기간 을 key - value 형태로 저장한다.

privacies를 순회하며 개인정보 수집 일자와 유효기간을 days 수로 바꾼다.

오늘 날짜와 대소를 비교하여 answer 리스트에 append 한다.

## 🥳 문제 회고

간단한 구현 문제였다

# 150367 : 표현 가능한 이진트리
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
def decimalToBinaryString(number):
    binary = ''
    while number > 0:
        if number % 2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        number //= 2
    treeLevel = 1
    while 2**treeLevel - 1 < len(binary):
        treeLevel += 1
    binary = '0' * ((2**treeLevel - 1) - len(binary)) + binary
    return binary

def isBinaryTree(S):
    if len(S) == 1:
        return True
    left = S[:len(S) // 2]
    mid = S[len(S)//2]
    right = S[len(S)//2 + 1:]
    if mid == '1':
        return isBinaryTree(left) and isBinaryTree(right)
    else:
        if ('1' in left) or ('1' in right):
            return False
        return True

def solution(numbers):
    answer = []
    for number in numbers:
        binary = decimalToBinaryString(number)
        if isBinaryTree(binary):
            answer.append(1)
        else:
            answer.append(0)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

우선 numbers를 순회한다.

주어진 number를 이진수 문자열로 바꾼다. 이 때, 문자열의 길이가 포화 이진트리의 노드 개수가 될 수 있도록 문자열 앞에 0을 추가해준다. 예를 들어 10이라는 십진수는 이진수로 바꾸면 1010이다. 문제의 상황에 따라 이를 포화 이진트리로 만들기 위해 필요한 최소 노드 수는 7개다. 왜냐하면 2^2 - 1 < 4 (1010의 길이) < 2^3 - 1 이기 때문이다.

```python
treeLevel = 1
while 2**treeLevel - 1 < len(binary):
    treeLevel += 1
binary = '0' * ((2**treeLevel - 1) - len(binary)) + binary
```

위와 같은 코드로 최소 개수만큼 0을 앞에 더할 수 있다.

그 결과 반드시 문자열의 길이는 홀수가 된다. 이 문자열은 이진트리를 중위순회한 결과이기 때문에, 문자열의 중앙을 기준으로 왼쪽 서브 트리와 오른쪽 서브 트리로 나눌 수 있다. 예를 들어, 0001010의 경우 000 과 010 으로 나눌 수 있는 것이다. 

여기에서 규칙을 발견할 수 있다. 만약 문자열 중앙의 문자가 ‘0’이고 좌, 우 서브트리 중 어느 하나라도 ‘1’을 포함하면 이는 이진트리가 아니다. 왜냐하면 문자열의 가운데 문자는 루트 노드고 좌 우는 자식 서브트리인데, 루트 노드가 0이면 좌, 우 서브트리의 노드들도 존재할 수 없기 때문이다(즉, 서브트리 노드들이 반드시 0이어야 한다)

따라서 분할정복으로 재귀함수를 구현하여 문제를 해결할 수 있다. 반복적으로 서브트리들의 이진트리 가능 여부를 검사하고, 어느 하나라도 이진 트리가 아닌 경우 전체는 이진 트리가 아니게 된다.

## 🥳 문제 회고

처음에 직접 이진트리를 만들고 이를 바탕으로 순회해야 하나 고민했다. 하지만 주어진 number를 이진수로 바꾸면 이미 포화 이진트리라 가정하고 중위 순회한 결과가 나오기 때문에 뭔가 순서가 어색했다.

예제를 조금 더 들여다보니 결과가 나왔고 분할정복으로 문제를 해결할 수 있음을 발견했다.