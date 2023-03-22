## backjoon-2343

풀이시간: 2h
문제 자체는 간단하지만 최소 너비를 이진탐색으로 구한다는 사실을 떠올리기 어려웠습니다.
처음에는 DP를 사용해 가능한 조합의 모든 경우의 수를 구하고자 하였으나, 시간 복잡도를 맞출 수 없었습니다.

### 어려웠던 부분

- 이진 탐색 시 잘못된 인덱스 관리로 무한루프가 자주 발생했습니다. 

### 풀이 방법

- 이진 탐색을 이용해 O(log n) 시간 내에 최소 디스크 너비를 구합니다.
- 개별 디스크 너비에 대해 주어진 디스크 개수 O(n)를 만족하는 지 확인합니다.

### 풀이 로직

```javascript

function solution(input) {
  const [lectureCount, containerCount] = input[0];
  const lectures = input[1];
  let minSize = 0;
  let maxSize = lectures.reduce((ac, v) => ac + v, 0);
  let currentSize = 0;

  // [1] L포인터(minSize)와 R포인터(maxSize)를 기준으로 이진탐색합니다
  while (minSize !== maxSize) {
    currentSize = ~~((minSize + maxSize) / 2);
    // [2] 현재 너비(평균값)을 기준으로 컨테이너(디스크)가 작은지 확인합니다)
    const containerIsSmall = isContainerSmall(
      lectures,
      lectureCount,
      currentSize,
      containerCount
    );
    // [3] 디스크가 작을 경우 L포인터(minSize)를 증가시킵니다
    if (containerIsSmall) {
      minSize = currentSize + 1;
      // [4] 디스크가 클 경우 R포인터(maxSize)를 감소시킵니다
    } else {
      maxSize = currentSize;
    }
  }
  return minSize;
}

// 주어진 너비를 기준으로 컨테이너(디스크) 개수의 초과 여부를 반환합니다
function isContainerSmall(lectures, length, width, containerCount) {
  let totalCount = 0;
  let currentSum = 0;
  for (let i = 0; i < length; i++) {
    // [1] 강의 길이가 디스크 너비보다 작은지 확인합니다
    if (lectures[i] > width) {
      return true;
      // [2] 현재까지 강의 길이의 합이 디스크 너비보다 작은 지 확인합니다
    } else if (currentSum + lectures[i] <= width) {
      currentSum += lectures[i];
      // [3] 강의 길이의 합이 디스크 너비보다 큰 경우 새로운 디스크를 생성합니다
    } else {
      currentSum = lectures[i];
      totalCount += 1;
    }
  }
  // [4] 남은 강의가 존재할 경우 디스크를 추가합니다
  if (currentSum) totalCount += 1;
  return totalCount > containerCount;
}

```