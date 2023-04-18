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
