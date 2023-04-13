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