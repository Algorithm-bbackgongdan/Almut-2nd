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