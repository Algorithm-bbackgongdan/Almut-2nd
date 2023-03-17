function solution(numbers) {
  const answer = [];
  const res = numbers.map((number) =>
    Array.from(number.toString(2), (v) => parseInt(v))
  );

  // [1] 각 값에 대해서 순환한 뒤 결과를 반환합니다
  for (let i = 0; i < res.length; i++) {
    const binArray = completeBinaryTree(res[i]);
    const value = checkPattern(binArray, 0, binArray.length - 1);
    if (value !== -1) {
      answer.push(1);
    } else {
      answer.push(0);
    }
  }
  return answer;
}

//f: 이진 트리를 포화 이진 트리로 만듭니다
function completeBinaryTree(binArray) {
  let completeTreeLength = 1;
  let exp = 1;
  while (completeTreeLength < binArray.length) {
    completeTreeLength = Math.pow(2, exp) - 1;
    exp++;
  }
  const gap = completeTreeLength - binArray.length;
  return [...Array(gap).fill(0), ...binArray];
}

//f: 이진 트리를 탐색하며 패턴 일치여부를 반환합니다
function checkPattern(binArray, start, end) {
  // [1] 길이가 1이면(리프노드이면) 값을 반환합니다
  if (start === end) {
    return binArray[start];
  }

  // [2] 좌우 자식 노드의 값(0 or 1 or -1)을 구합니다
  const mid = Math.floor((start + end) / 2);
  const leftNode = checkPattern(binArray, start, mid - 1);
  const rightNode = checkPattern(binArray, mid + 1, end);

  // [3] 현재 트리의 상태를 구하고 반환합니다 (1: 이진 트리, 0: 더미 트리, -1: 오류)
  if (leftNode === -1 || rightNode === -1) {
    return -1;
  }
  if (leftNode === 1 && binArray[mid] === 0) {
    return -1;
  }
  if (rightNode === 1 && binArray[mid] === 0) {
    return -1;
  }
  if (leftNode === 0 && rightNode === 0 && binArray[mid] === 0) {
    return 0;
  }
  return 1;
}
