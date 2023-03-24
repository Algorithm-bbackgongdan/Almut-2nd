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

## backjoon-2240

풀이시간: 4h
3중 배열 DP를 처음 사용하는 문제였습니다. 3중 배열 DP를 떠올리지 못해
greedy로 풀이할 경우 10^7이 간신히 도달하는 듯 하여 이를 고민하다가 시간을 많이 소모했습니다.

DP문의 구현은 어렵지 않았지만, 기초 케이스 (index = 0)을 마련하는데 실수가 많았습니다.
특히, 현재 위치가 RIGHT이고 이동이 2번인 경우 (LEFT(시작) -> RIGHT -> LEFT) 발생이 불가능한 경우가 존재하는데,
이런 부분의 예외 처리 없이도 문제가 풀려서 좀 당황스럽습니다.

### 어려웠던 부분

- 2중 2차원 배열을 상호 참조하는 점화식을 고안하기가 쉽지 않았습니다.
- 점화식의 가장 마지막 값이 최적 해가 아닐 수 있다는 사실을 이해하기 어려웠습니다. (이동하지 않는 게 유리할 수 있음)

### 풀이 방법

- 3차원 배열을 만든 뒤 index = 0일때 값을 채웁니다 

### 풀이 로직

```javascript

function solution(input) {
  const [T, W, ...schedule] = input.flat();
  const dp = new Array(3)
    .fill(0)
    .map((_) => new Array(T).fill(0).map((_) => new Array(W + 1).fill(0)));
  const LEFT = 1;
  const RIGHT = 2;

  //dp[현재 나무][현재 시간][움직임 횟수]

  // [1] Time = 0일때 조건을 채웁니다
  // 첫번째 값을 기준으로 값을 지정합니다
  for (let move = 0; move < W + 1; move++) {
    if (schedule[0] === LEFT) {
      dp[LEFT][0][move] = 1;
      dp[RIGHT][0][move] = 0;
    } else if (schedule[0] === RIGHT) {
      dp[LEFT][0][move] = 0;
      dp[RIGHT][0][move] = 1;
    }
  }



  // [2] Move = 0일때 조건을 채웁니다
  // 움직임 없이 RIGHT로 바로 이동할 수 없으므로 0으로 지정합니다
  let leftAccum = dp[LEFT][0][0];
  for (let time = 1; time < T; time++) {
    if (schedule[time] === LEFT) {
      leftAccum++;
    }
    dp[LEFT][time][0] = leftAccum;
    dp[RIGHT][time][0] = 0;
  }
    dp[RIGHT][0][0] = 0;

  // [3] DP를 통해 배열을 채웁니다
  for (let time = 1; time < T; time++) {
    for (let move = 1; move < W + 1; move++) {
      if (schedule[time] === LEFT) {
        dp[LEFT][time][move] = Math.max(
          dp[LEFT][time - 1][move] + 1,
          dp[RIGHT][time - 1][move - 1] + 1
        );
        dp[RIGHT][time][move] = Math.max(
          dp[LEFT][time - 1][move - 1],
          dp[RIGHT][time - 1][move]
        );
      } else if (schedule[time] === RIGHT) {
        dp[LEFT][time][move] = Math.max(
          dp[LEFT][time - 1][move],
          dp[RIGHT][time - 1][move - 1]
        );
        dp[RIGHT][time][move] = Math.max(
          dp[LEFT][time - 1][move - 1] + 1,
          dp[RIGHT][time - 1][move] + 1
        );
      }
    }
  }

  // [4] 시간 내 (T-1) 배열의 최대값을 구합니다
  let ans = 0;
  for (let i = 0; i < W + 1; i++) {
    const currentMax = Math.max(dp[LEFT][T - 1][i], dp[RIGHT][T - 1][i]);
    ans = Math.max(ans, currentMax);
  }
  return ans;
}


```