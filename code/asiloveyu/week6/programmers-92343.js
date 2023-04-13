// Stack에 들어가는 구조는 다음과 같습니다 [candidate, sheep, wolf]
// candidate - 현재 선택된 노드 집합과 연결된 노드들
// sheep - 양의 수
// wolf - 늑대의 수
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
        stack.push([candidate.filter((node) => node !== cand), sheep, wolf]);
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
