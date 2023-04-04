## backjoon-11779

풀이시간: 2h20m
자바스크립트에 heap 구조가 없어서 시간 소모가 높았습니다.

### 어려웠던 부분

- 문제의 예제와 실제 실행 결과가 달라 이해하는데 어려움이 있었습니다. (동일 비용일 경우 경로 선택)
- 지나온 경로 추적을 적용하는데 어려움이 있었습니다.

### 풀이 방법

- 경로를 도시별로 정리한 뒤 시작 지점을 기준으로 모든 경로를 Heap 구조에 삽입합니다.
- Heap에서 가까운 순으로 경로를 pop한 뒤 각 도시로 최적 경로를 업데이트 합니다.
- 최적 경로를 기준으로 cost를 계산하고, 각 도시별 nearest 도시를 만들어 nearest 순으로 시작 지점까지 역추적 합니다.

### 풀이 로직

```javascript
function solution(input) {
  const [[cityCount], [busCount], ...routes] = input;
  const [start, end] = routes.pop();
  const minDist = new Array(cityCount + 1).fill(Number.MAX_VALUE);
  const busRoute = new Array(cityCount + 1).fill(0).map((_) => []);
  const nearest = new Array(cityCount + 1).fill(start);

  // [1] 버스 경로를 출발 도시 별로 정리합니다
  routes.forEach((route) => {
    const [start, end, dist] = route;
    busRoute[start].push([end, dist]);
  });

  // [2] Heap 객체를 생성합니다
  const heap = new MinHeap();
  heap.insert([start, 0]);

  while (heap.getLength() !== 0) {
    const [currentCity, currentDist] = heap.remove();

    // [3] currentCity까지 거리가 최소 거리보다 크면 건너뜁니다
    if (currentDist > minDist[currentCity]) continue;

    // [4] currentCity까지 이어진 각 버스 루트에 대해 새로운 경로를 궇바니다
    busRoute[currentCity].forEach((route) => {
      const [busEnd, busDist] = route;
      const newDistance = currentDist + busDist;

      // [5] 새로운 경로가 더 짧은 경우, 경로를 업데이트 합니다
      if (minDist[busEnd] > newDistance) {
        minDist[busEnd] = newDistance;
        nearest[busEnd] = currentCity;
        heap.insert([busEnd, newDistance]);
      }
    });
  }

  // [6] Nearest 배열에 대해 지나온 경로를 역추적 합니다
  let currentCity = end;
  let path = [];
  while (currentCity !== start) {
    path.push(currentCity);
    currentCity = nearest[currentCity];
  }
  path.push(start);
  path.reverse();

  const ans = `${minDist[end]}\n${path.length}\n${path.join(" ")}`;
  return ans;
}
```

## backjoon-1956

풀이시간: 1h
플로이드 알고리즘을 이해하는 데 다소 시간이 소모되었습니다.
이상한 지점이 있는데 중간 경로(m)의 nested loop 상 위치가 최상단 / 최하단에 있어도 둘다 통과가 된다는 점 입니다.
```javascript
/// 최상단인 경우
 for (let m = 1; m < v + 1; m++) {
    for (let y = 1; y < v + 1; y++) {
      for (let x = 1; x < v + 1; x++) {
        mat[y][x] = Math.min(mat[y][x], mat[y][m] + mat[m][x]);
      }
    }
  }

/// 최하단인 경우
  for (let y = 1; y < v + 1; y++) {
    for (let x = 1; x < v + 1; x++) {
      for (let m = 1; m < v + 1; m++) {
        mat[y][x] = Math.min(mat[y][x], mat[y][m] + mat[m][x]);
      }
    }
  }
```
논리적으로는 결과가 달라야 할 것 같은데 (x, y = 1 인 경우와 x, y = v + 1 인 경우 각 최소 경로가 다르므로) 
혹시 아이디어가 있다면 공유 주시면 감사하겠습니다.

### 어려웠던 부분

- 플로이드 알고리즘을 이해하는데 어려움이 있었습니다.
  
### 풀이 방법

- 주어진 도로들을 기반으로 경로 매트릭스를 생성합니다.
- 경로 매트릭스에 대해 플로이드 W. 알고리즘을 토대로 최단 경로를 구합니다.
- 자기 자신으로 향하는 최단 거리를 구합니다.

### 풀이 로직

```javascript

function solution(input) {
  const [[v, e], ...routes] = input;
  const MAX = Number.MAX_VALUE;
  const mat = new Array(v + 1).fill(0).map((_) => new Array(v + 1).fill(MAX));

  // [1] 각 도로를 기반으로 경로 매트릭스를 생성합니다
  routes.forEach((route) => {
    const [start, end, cost] = route;
    mat[start][end] = cost;
  });

  // [2] 경로 매트릭스에 대해 최단거리를 구합니다
  for (let m = 1; m < v + 1; m++) {
    for (let y = 1; y < v + 1; y++) {
      for (let x = 1; x < v + 1; x++) {
        mat[y][x] = Math.min(mat[y][x], mat[y][m] + mat[m][x]);
      }
    }
  }

  // [3] 자기 자신으로 향하는 최단거리 중 가장 작은 값을 고릅니다
  let min = MAX;
  for (let e = 1; e < v + 1; e++) {
    if (mat[e][e] !== MAX && mat[e][e] < min) {
      min = mat[e][e];
    }
  }
  if (min === MAX) {
    return -1;
  }
  return min;
}
```

## programmers-92341

풀이시간: 1h
문제의 지문을 읽고 이해하는데 시간이 다소 소모되었습니다.
코드를 더 보기좋게 작성할 방법이 있을 것 같은데, 다른 분들은 어떻게 하셨는지 궁금하네요!

### 어려웠던 부분

- NA

### 풀이 방법

- Record를 하나씩 순회하며 차 별로 최대 체류 시간을 구합니다
- 출차 기록이 없는 차에 대해 마지막 시간을 기준으로 체류 시간을 구합니다
- 체류 시간을 기준으로 요금을 구합니다
- 차 배열을 번호 순으로 정렬한 뒤, 비용을 추출합니다

### 풀이 로직

```javascript

function solution(fees, records) {
  const cars = new Map();
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  const LAST_CALL = getMinute("23:59");

  // [1] Record의 IN, OUT을 기준으로 최대 체류 시간을 구합니다
  // cars의 구조: [entrance, time accumulator]
  records.forEach((record) => {
    const [time, number, action] = record.split(" ");
    const current = getMinute(time);
    // [1-1] 차가 아직 없는 경우 새로 생성합니다
    if (!cars.has(number)) cars.set(number, [-1, 0]);
    // [1-2] 입출차를 기준으로 차의 총 체류 시간을 구합니다
    const [entrance, totalTime] = cars.get(number);
    if (action === "IN") {
      cars.set(number, [current, totalTime]);
    } else if (action === "OUT") {
      const gap = current - entrance;
      cars.set(number, [-1, totalTime + gap]);
    }
  });

  // [2] 각 차의 체류 시간을 기준으로 요금을 구합니다
  // cars의 구조: [fee]
  cars.forEach((car, number) => {
    let [entrance, totalTime] = car;
    // [2-1] 출차 기록이 없는 경우 마지막 시간을 기준으로 구합니다
    if (entrance !== -1) {
      const gap = LAST_CALL - entrance;
      totalTime += gap;
    }
    // [2-2] 기본시간(baseTime)과 단위시간(unitTime)을 기준으로 계산합니다
    const value = totalTime - baseTime;
    if (value <= 0) {
      cars.set(number, baseFee);
      return;
    } else {
      const quotient = ~~(value / unitTime);
      const remain = value % unitTime ? 1 : 0;
      cars.set(number, baseFee + (quotient + remain) * unitFee);
    }
  });

  // [3] 차 배열을 번호 순으로 정렬한 뒤, 비용을 추출합니다
  const answer = [...cars]
    .sort((carA, carB) => {
      return parseInt(carA[0], 10) - parseInt(carB[0], 10);
    })
    .map(([_, cost]) => cost);

  return answer;
}

function getMinute(time) {
  const [hh, mm] = time.match(/\d{2}/g).map((v) => parseInt(v, 10));
  return hh * 60 + mm;
}

```

## programmers-92342

풀이시간: 1h30m
마찬가지로 문제를 읽고 이해하는데 오랜 시간이 소모되었습니다.
문제의 틀은 금방 완성했는데, 예상보다 오류 케이스가 많아 이를 고민하는데도 시간 소모가 많았습니다.

### 어려웠던 부분

- 답안을 구성하며 고려하지 못한 예외 케이스 찾기 (무지와 라이언이 비기는 케이스 등)

### 풀이 방법

- dfs로 매 시행에서 (1) 이기거나 (2) 지는(비기는) 두가지 케이스로 재귀 탐색합니다 (O(2^10))
- 끝에 도달하는 경우 결과륿 반환합니다
  - 인덱스가 10에 도달할 경우 결과(라이언 점수, 어피치 점수, 라이언 기록)를 반환합니다
  - 화살이 모두 떨어질 경우 어피치의 점수를 업데이트 한 뒤 결과를 반환합니다
- 재귀 결과를 역순으로 비교하며 반환합니다
  - 두 케이스 중 점수차가 높은 경우를 반환합니다
  - 두 케이스의 점수차가 같은 경우 '가장' 작은 값이 더 많은 경우를 반환합니다

### 풀이 로직

```javascript
function solution(n, info) {
  const lion = new Array(11).fill(0);
  const [lionScore, peachScore, lionArray] = dfs(lion, info, n, 0, 0, 0);

  if (lionScore <= peachScore) {
    return [-1];
  } else {
    return lionArray;
  }
}

// dfs 수행 함수
function dfs(lion, peach, arrow, index, lionScore, peachScore) {
  // [1] 마지막인 경우
  if (index === 10) {
    const newLion = [...lion];
    newLion[index] = arrow;
    return [lionScore, peachScore, newLion];
  }
  if (arrow === 0) {
    for (let i = index; i < 11; i++) {
      if (peach[i] > 0) peachScore += 10 - i;
    }
    return [lionScore, peachScore, lion];
  }

  let winCase, loseCase;

  // [2] 라이언이 해당 점수에서 이기는 경우
  const remainArrow = arrow - (peach[index] + 1);
  // [2-1] 사용가능한 화살이 피치보다 많은 경우에 수행
  if (remainArrow >= 0) {
    const newLion = [...lion];
    newLion[index] = peach[index] + 1;
    winCase = dfs(
      newLion,
      peach,
      remainArrow,
      index + 1,
      lionScore + (10 - index),
      peachScore
    );
  }

  // [2] 라이언이 해당 점수에서 지는(비기는) 경우
  if (peach[index] !== 0) {
    loseCase = dfs(
      lion,
      peach,
      arrow,
      index + 1,
      lionScore,
      peachScore + (10 - index)
    );
  } else {
    loseCase = dfs(lion, peach, arrow, index + 1, lionScore, peachScore);
  }

  // [3] 최적값 반환
  // [3-1] 라이언이 해당 점수에서 이길 수 없는 경우
  if (!winCase) return loseCase;
  // [3-2] 라이언이 더 큰 점수차로 이기는 경우를 반환
  const [winLionScore, winPeachScore] = winCase;
  const [loseLionScore, losePeachScore] = loseCase;
  const winScoreGap = winLionScore - winPeachScore;
  const loseScoreGap = loseLionScore - losePeachScore;

  if (winScoreGap !== loseScoreGap) {
    return winScoreGap > loseScoreGap ? winCase : loseCase;
    // [3-3] 점수차가 같은 경우 낮은 값이 더 많은 경우를 반환
  } else if (winScoreGap === loseScoreGap) {
    return getSkewedArray(winCase, loseCase);
  }
}

// 두 배열 중 낮은 값이 더 많은 배열을 반환
function getSkewedArray(inputOne, inputTwo) {
  const arrOne = inputOne[2];
  const arrTwo = inputTwo[2];

  for (let i = 10; i >= 0; i--) {
    if (arrOne[i] > arrTwo[i]) {
      return inputOne;
    } else if (arrTwo[i] > arrOne[i]) {
      return inputTwo;
    }
  }
  return arrOne;
}

```