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