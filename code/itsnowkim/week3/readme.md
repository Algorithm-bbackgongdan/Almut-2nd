# week 3 - 이분탐색, DP
## 이분탐색
### 순차 탐색
Sequentail Search. 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

파이썬에서는 리스트에 특정 값의 원소가 있는지 체크할 때도 순차 탐색으로 원소를 확인하고,
리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드를 이용할 때도 내부에서는 순차 탐색이 수행된다.

```python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

시간 복잡도는 O(N) 이다.

### 이분 탐색 - 반으로 쪼개면서 탐색하기
Binary Search는 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.

위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 [시작점, 끝점, 중간점] 이다.
찾으려는 데이터와, 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.

시간복잡도는 O(logN)이다.
구현하는 방법은 재귀 함수를 이용하는 방법과, 단순 반복문을 이용하는 방법이 있다.

```python
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n, target 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

```python
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None
        

# n, target 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

저자의 말
- 이진 탐색은 단골 문제이므로 외워라! -> 외웠다!
- 탐색 범위가 2000만을 넘어가면 이진 탐색으로 접근해보길 권함.
- 1000만 단위를 넘어가게 되면 이진 탐색과 같이 O(logN)의 알고리즘을 떠올려야 한다.

### 이진 탐색 트리
이진 탐색의 전제 조건은 데이터 정렬이다.
이진 탐색 트리는 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.
이진 탐색 트리는 다음과 같은 특징을 가진다.
- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.
**왼쪽 자식 노드 < 부도 노드 < 오른쪽 자식 노드**

## DP

## 문제풀이
### 기타 레슨 - 2343
