## backjoon-3665

풀이시간: 3h
간단한 문제이나, 경험 부족으로 시간이 오래 걸렸던 것 같습니다. 
또한, recursive DFS보다 iterative DFS가 성능상 더 유리다하고 하여
while loop로 구현해보도록 노력하였습니다.

### 어려웠던 부분

- 문제의 요구사항을 따르려다가 이상한 방향으로 구현을 잡아, 코드를 모두 뒤엎어야 했습니다.
- 가능하다면, 문제의도를 파악하고 단순한 방향으로 코드를 작성해야 할 것 같습니다.

### 풀이 방법

- iterative DFS를 실행하여 stack이 빌 때까지 순환합니다.
- stack을 초기화합니다.
  - stack에 들어가는 구조는 다음과 같습니다 [candidate, sheep, wolf]
  - candidate - 현재 선택된 노드 집합과 연결된 노드들 (예비노드)
  - sheep - 양의 수
  - wolf - 늑대의 수
- stack을 pop하고 candidate의 길이가 0이면 정답 집합에 포함합니다. (더이상 탐색이 불가)
- candidate의 모든 값(cand)을 하나씩 확인하며 (...)
  - cand == 0 (양 노드) 인 경우, sheep + 1 후 stack에 추가
  - cand == 1 (늑대 노드) 인 경우, wolf + 1 후 stack에 추가
  - 늑대 노드이면서 늑대가 양보다 같거나 많은 경우, 정답 집합에 포함 (더이상 탐색이 불가) 
- 정답 배열을 반환합니다.

### 풀이 로직

```javascript
function solution(info, edges) {
  const answers = [];
  const stack = [[getChildNode(0, info, edges), 1, 0]];
  // [1] Iterative DFS를 실행합니다
  while (stack.length !== 0) {
    const [candidate, sheep, wolf] = stack.pop();
    // [2] candidate의 길이가 0인 경우 정답 리스트에 포함합니다
    if (candidate.length === 0) answers.push(sheep);
    // [3] candidate의 모든 값(cand)에 대해서 Search를 수행합니다
    for (cand of candidate) {
      // [3-1] 현재 cand를 연결 노드 집합에서 지우고 그 자식을 연결 노드 집합에 추가합니다
      const newCandidate = candidate.filter((node) => node !== cand);
      const children = getChildNode(cand, info, edges);
      children.length !== 0 && newCandidate.push(...children);
      // [3-2] cand가 양 노드일 경우
      if (info[cand] === 0) {
        stack.push([newCandidate, sheep + 1, wolf]);
        // [3-3] cand가 늑대 노드일 경우
      } else if (info[cand] === 1 && wolf + 1 < sheep) {
        stack.push([newCandidate, sheep, wolf + 1]);
        // [3-4] cand가 늑대 노드이고 늑대를 초과시킬 경우
      } else {
        answers.push(sheep)
      }
    }
  }
  return Math.max(...answers);
}

// 자식 노드를 탐색하는 함수입니다
function getChildNode(parent, info, edges) {
  const res = [];
  edges.forEach((edge) => {
    if (edge[0] === parent && info[edge[1]] !== -1) {
      res.push(edge[1]);
    }
  });
  return res;
}

```

## backjoon-42860

풀이시간: 3h
마찬가지로 어려운 문제가 아니지만, 인덱스를 잡아주는데 오랜 시간이 소요되었습니다.
(1) 스텝, (2) 갯수, (3) 인덱스 간의 관계에 대해서 조금 더 주의깊게 고민해야할 것 같습니다.

### 어려웠던 부분

- 인덱스를 하나씩 점검하며 노트에 시뮬레이션 하는데 오랜 시간이 소요되었습니다.

### 풀이 방법

- 전진하다가 A를 만날 경우 뒤로가서 나머지 알파벳을 변경하는 개별 경우의 수를 구합니다
  (예) BBAAAB 의 경우 totalStep은
  A를 지나갈 때 필요 스텝: A 길이 (3) - 1 + A와 연결하는 스텝 (2) = 4
  A를 만나기 전에 돌아가는 경우 필요 스텝: 5 - 4 + 2 = 3 <- 더 우월합니다
  - A에 도달할 때 필요 스텝 (뒤로가는 수): 현재 포인터 (2) = 2
  - 기본 총 스텝: 배열 길이 (6) - 1 = 5
- 이를 후진하다가 A를 만나는 경우에도 반복합니다
- 각 경우의 수 중 최소값을 고르고 알파벳 변경 횟수를 더합니다

### 풀이 로직

```javascript
function solution(name) {
  const nameArray = name.split("");
  const candidates = [name.length - 1];
  let fPtr = 1;
  // [1] 전진하며 A를 만날 경우, 뒤로가서 나머지 알파벳을 변경하는 개별 경우의 수를 구합니다
  while (fPtr < name.length) {
    // [1-1] A를 만난 경우
    if (name[fPtr] === "A") {
      let aPtr = fPtr;
      // [1-2] 해당 A 집합의 길이를 구합니다
      while (aPtr < name.length && name[aPtr] === "A") aPtr++;
      // [1-3] aLength: A 집합의 길이, pastStep: 돌아가는 거리, totalStep: 총 거리
      const aLength = aPtr - fPtr;
      const pastStep = fPtr;
      const totalStep = name.length - 1 - (aLength + 1) + pastStep;
      candidates.push(totalStep);
    }
    fPtr++;
  }
  // [2] 후진하며 A를 만날 경우, 앞으로 돌아가서 나머지 알파벳을 변경하는 경우의 수를 구합니다
  let rPtr = name.length - 1;
  while (rPtr >= 0) {
    // [2-1] A를 만난 경우
    if (name[rPtr] === "A") {
      let aPtr = rPtr;
      // [2-2] 해당 A 집합의 길이를 구합니다
      while (aPtr >= 1 && name[aPtr] === "A") aPtr--;
      // [1-3] aLength: A 집합의 길이, pastStep: 돌아가는 거리, totalStep: 총 거리
      const aLength = rPtr - aPtr;
      const pastStep = name.length - rPtr;
      const totalStep = name.length - 1 - (aLength + 1) + pastStep;
      candidates.push(totalStep);
    }
    rPtr--;
  }

  // char의 변경 횟수를 구한 뒤 candidates의 최소값과 더합니다
  let sum = getCharChange(nameArray);
  sum += Math.min(...candidates);
  return sum;
}

// 각각 char의 필요 변경 횟수를 구하여 더한 뒤 반환합니다
function getCharChange(arr) {
  let sum = 0;
  const a = "A".charCodeAt(0);
  const z = "Z".charCodeAt(0);
  arr.forEach((s) => {
    const aDist = s.charCodeAt(0) - a;
    const zDist = z - s.charCodeAt(0) + 1;
    sum += aDist < zDist ? aDist : zDist;
  });
  return sum;
}
```


## backjoon-42860

풀이시간: 2h
dfs, dp를 이용해 간단한 코드를 작성할 수 있었지만,
dp 임에도 이전 최소비용이 이후 최소비용을 보장하지 않을 수 있다는 개념을 떠올리는데 어려움이 있었습니다.
풀이가 잘 나오지 않아, 아이디어에 대한 힌트를 보고 풀었습니다.

### 어려웠던 부분

- 회전 시 가중되는 비용으로 인해 dp의 기본 원칙이 성립하지 않을 수 있다는 사실을 이해하기 어려웠습니다.
- 3차원 dp를 구성하는데 다소 어려움이 있었습니다.

### 풀이 방법

- 반복문 스택을 이용해 DFS 길찾기를 시도합니다.
- 이때, 각 DFS의 포인터들은 현재까지 비용을 포함합니다.
- 포인터를 기준으로 상하좌우를 탐색합니다.
  - 상하좌우 방향으로 셀에서 해당 방향과 일치하는 최소비용을 찾습니다.
  - 해당 최소비용이 현재까지 비용보다 큰 경우, 이를 현재의 비용으로 교체합니다.
  - 이후, 해당 방향으로 포인터를 stack에 삽입해 DFS를 수행합니다.
- 마지막 셀에서 상하좌우 방향으로 최소값을 구한뒤 반환합니다.

```javascript
function solution(board) {
  const N = board.length;
  const costBoard = new Array(N)
    .fill(0)
    .map((_) => new Array(N).fill(0).map((_) => new Array(4).fill(-1)));
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  const stack = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
  ];
  costBoard[0][0] = [0, 0, -1, -1];

  // [1] Iterative stack을 이용해 DFS를 실행합니다
  while (stack.length !== 0) {
    const [x, y, cost, rotation] = stack.pop();
    // [2] 각 방향에 대해서
    for (let i = 0; i < 4; i++) {
      // [2-1] 새로운 좌표를 구합니다
      const [dx, dy] = directions[i];
      const [nx, ny] = [x + dx, y + dy];
      // [2-2] 해당 좌표가 유효한지 검증합니다 (테이블 내, 장애물이 아님)
      if (!isValid([nx, ny], board, N)) continue;
      // [2-3] 과거 진행방향(rotation)과 일치할 경우 100, 아니면 600을 더합니다
      const dcost = rotation === i ? 100 : 600;
      const ncost = dcost + cost;
      // [2-4] 새로운 진행방향(i)에 해당하는 최소값을 꺼냅니다
      const pcost = costBoard[ny][nx][i];
      // [2-5] 최소값을 초기화 하거나, 최소값보다 작을 경우 이를 최소값으로 할당하고 stack에 넣습니다
      if (pcost === -1 || ncost < pcost) {
        costBoard[ny][nx][i] = ncost;
        stack.push([nx, ny, ncost, i]);
      }
    }
  }
  return Math.min(...costBoard[N - 1][N - 1].filter((v) => v !== -1));
}

function isValid([x, y], board, N) {
  if (x < 0 || x >= N) return false;
  if (y < 0 || y >= N) return false;
  if (board[y][x] === 1) return false;
  return true;
}

```