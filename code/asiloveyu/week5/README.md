## backjoon-3665

풀이시간: 3h
문제를 자세히 읽지 않고 진행하다가 중요한 사실을 놓쳐서 한참 헤맸습니다.
이러한 사실은 "새로운 순위로 주어진 (a, b) 배열 중 a가 승자이거나 b가 승자이다" 라는 점입니다.
반드시 "a -> b"라고 이해하여 오류 케이스를 발견하지 못했습니다.

### 어려웠던 부분

- 위상 정렬을 제대로 이해하고 적용하는데 어려움이 있었습니다.
- 문제의 입력이 set 형태로 주어져 코드의 잘못된 부분을 디버깅하는데 어려움이 있습니다.

### 풀이 방법

- 주어진 순위를 기준으로 방향 그래프와 inDegree 배열을 생성합니다.
- 새로운 방향을 기준으로 그래프를 업데이트 합니다. (승자를 기준으로)
- zeroInDegreeSet을 초기화하고 배열의 값을 꺼냅니다.
- 해당 값을 기준으로 정답 배열에 하나씩 inDegree가 0인 vertex를 추가합니다.
- 정답 배열을 반환합니다.

### 풀이 로직

```javascript
function solution(input) {
  let ans = "";
  let line = 1;

  while (line < input.length) {
    
    // [1] 입력 값을 초기화 합니다
    const [teamCount] = input[line++];
    const previousOrder = input[line++];
    const [changeCount] = input[line++];
    const changedDirectionArray = [];
    for (let i = 0; i < changeCount; i++) {
      changedDirectionArray.push(input[line++]);
    }

    // [2] 상수 값을 초기화 합니다
    const directionArray = new Array(teamCount + 1)
      .fill(0)
      .map((_) => new Array());
    const inDegreeArray = new Array(teamCount + 1).fill(0);
    const zeroInDegreeSet = [];
    const newOrder = [];

    // [2] 방향 그래프와 inDegree 배열을 생성합니다
    for (let i = 0; i <= teamCount; i++) {
      for (let j = i + 1; j <= teamCount; j++) {
        directionArray[previousOrder[i]].push(previousOrder[j]);
        inDegreeArray[previousOrder[j]] += 1;
      }
    }

    // [3] 새로운 방향을 참조해 방향 그래프를 업데이트합니다
    for (let i = 0; i < changedDirectionArray.length; i++) {
      const [one, two] = changedDirectionArray[i];

      const oneIsWinnerIndex = directionArray[two].indexOf(one);
      const twoIsWinnerIndex = directionArray[one].indexOf(two);

    // [3-1] oneIsWinner = one이 새로운 승자인 경우 (vice versa)
      if (oneIsWinnerIndex !== -1) {
        directionArray[two].splice(oneIsWinnerIndex, 1);
        inDegreeArray[one] -= 1;
        directionArray[one].push(two);
        inDegreeArray[two] += 1;
      } else if (twoIsWinnerIndex !== -1) {
        directionArray[one].splice(twoIsWinnerIndex, 1);
        inDegreeArray[two] -= 1;
        directionArray[two].push(one);
        inDegreeArray[one] += 1;
      }
    }

    // [4] inDegree가 0인 경우 zeroInDegreeSet 초기화
    for (let i = 1; i <= teamCount; i++) {
      if (inDegreeArray[i] === 0) {
        zeroInDegreeSet.push(i);
      }
    }

    // [5] zeroInDegreeSet에서 winner를 pop한 뒤 연결된 loser를 찾아서 indegree 감소
    // winner를 결과에 추가
    // zeroInDegreeSet의 길이가 0인 경우 (Cycle 생성), 길이가 2인 경우 (순위 결정 불가) -> 오류
    while (zeroInDegreeSet.length === 1) {
      const winner = zeroInDegreeSet.pop();
      directionArray[winner].forEach((loser) => {
        inDegreeArray[loser] -= 1;
        if (inDegreeArray[loser] === 0) {
          zeroInDegreeSet.push(loser);
        }
      });
      newOrder.push(winner);
    }

    // [6] 결과 반환
    // 새로운 순서 배열의 길이가 다른 경우 -> 불가능
    if (newOrder.length !== previousOrder.length) {
      ans = ans.concat("IMPOSSIBLE", "\n");
    } else {
      ans = ans.concat(newOrder.join(" "), "\n");
    }
  }
  return ans.trimEnd();
}

```

## backjoon-17472

풀이시간: 3h
풀이 알고리즘이 주어졌으므로 문제에 대한 개념적인 구현은 금방 끝났지만,
디버깅하는데 오랜 시간이 걸렸습니다. 해당 문제 요인은 Union-Find의 과정 중
parent 배열의 재할당을 각 집합의 최상단 parent가 아니라 자식의 parent 값을 재할당하여
문제가 발생했습니다. 단순한 실수로도 오랜 시간이 소모될 수 있음을 배웠습니다.

### 어려웠던 부분

- 다량의 코드를 오류 없이 작성하는데 어려움이 있었습니다.
- Union-Find와 Kruskal의 개념을 확실히 이해하는데 시간이 소모되었습니다.

### 풀이 방법

- map의 개별 섬에 대해서 개별 숫자(2, 3, 4, ...)를 부여합니다.
- DFS (recursion)을 이용해 모든 가능한 edge를 탐색합니다.
- edge를 오름차순으로 정렬합니다.
- 정렬한 edge를 기준으로 Kruskal MST를 수행합니다.
- MST가 완성되면 (edge의 개수가 vertex - 1)인 경우 반환하고, 아니면 -1 을 반환합니다.

### 풀이 로직

```javascript
function solution(input) {
  const [[height, width], ...map] = input;
  const direction = [
    [0, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
  ];
  const path = [];
  let flag = 2;

  // [1] Map의 섬에 index를 부여
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      if (map[y][x] === 1) {
        fillIsland([x, y], flag, direction, map, width, height);
        flag++;
      }
    }
  }

  // [2] 각 섬에 대해서 edge 탐색
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      if (map[y][x] !== 0) {
        for (const d of direction) {
          const [dest, cost] = checkPath([x, y], d, map, width, height);
          // edge의 구성 (시작, 끝, 비용(길이))
          if (dest !== -1) path.push([map[y][x], dest, cost]);
        }
      }
    }
  }

  // [3] 각 edge에 대해 거리를 기준으로 오름차 정렬
  path.sort((a, b) => {
    return a[2] - b[2];
  });

  // [4] Kruskal 알고리즘 기반 MST 수행
  const parent = new Array(flag).fill(0).map((_, i) => i);
  const SPAN_EDGE = flag - 3; // flag = (0, 1, ...) = island 개수 + 2
  let pathCount = 0;
  let costSum = 0;

  // [4-1] 거리가 낮은 순으로 모든 edge(path)에 대해 union 수행
  for (p of path) {
    const [a, b, cost] = p;
    const ap = findParent(parent, a);
    const bp = findParent(parent, b);

    if (ap !== bp) {
      pathCount++;
      costSum += cost;
      union(parent, ap, bp);
    }
    if (pathCount === SPAN_EDGE) break;
  }

  // [4-2] 결과 반환
  if (pathCount !== SPAN_EDGE) return -1;
  return costSum;
}

// Union-Find에서 Union 함수
function union(parent, a, b) {
  parent[a] = b;
}

// Union-Find에서 Find 함수
function findParent(parent, vertex) {
  // 부모가 자기 자신이 아니면 path optimization을 수행하며 부모 탐색
  if (vertex !== parent[vertex]) {
    parent[vertex] = findParent(parent, parent[vertex]);
  }
  return parent[vertex];
}

// 길의 존재 여부를 확인하는 함수
function checkPath(start, direction, map, w, h) {
  const [dx, dy] = direction;
  let [x, y] = start;
  const startValue = map[y][x];
  let movement = 0;

  // 진행방향으로 한칸씩 전진
  do {
    x += dx;
    y += dy;
    movement++;
    if (x >= w || x < 0) return [-1, 0];
    if (y >= h || y < 0) return [-1, 0];
    if (map[y][x] === startValue) return [-1, 0];
  } while (map[y][x] === 0);

  // 다리의 길이는 움직임 - 1
  const bridgeLen = movement - 1;

  // 다리 길이가 2 이상인 경우만 값 반환 (목표점, 다리 길이)
  if (bridgeLen >= 2) return [map[y][x], bridgeLen];
  else return [-1, 0];
}

// 각 섬에 인덱스를 부여하는 함수
function fillIsland(start, flag, direction, map, w, h) {
  const [x, y] = start;
  map[y][x] = flag;
  // 상하좌우로 확장하며 섬에 인덱스 값 부여
  for (const d of direction) {
    const [dx, dy] = d;
    const [nx, ny] = [x + dx, y + dy];
    if (0 <= nx && nx < w && 0 <= ny && ny < h && map[ny][nx] === 1) {
      fillIsland([nx, ny], flag, direction, map, w, h);
    }
  }
}

```