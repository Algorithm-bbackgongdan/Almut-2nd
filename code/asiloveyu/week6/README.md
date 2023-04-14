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
  A에 도달할 때 필요 스텝: 현재 포인터 (2) = 2
  기본 총 스텝: 배열 길이 (6) - 1 = 5
  A를 만나기 전에 돌아가는 경우 필요 스텝: 5 - 4 + 2 = 3
- 이를 후진하다가 A를 만나는 경우도 반복합니다
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