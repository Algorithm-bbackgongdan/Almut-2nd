/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week2/backjoon-1744.txt", "utf-8", (_, data) => {
//   data
//     .toString()
//     .split("\n")
//     .forEach((line) => {
//       input.push(line.split(" ").map((v) => parseInt(v)));
//     });
//   console.log(solution(input));
// });

////////////////////////////////////
// Reading file from backjoon env //
////////////////////////////////////

let input = [];
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline
  .on("line", function (data) {
    input.push(
      data
        .trim()
        .split(" ")
        .map((v) => parseInt(v))
    );
  })
  .on("close", function () {
    const ret = solution(input);
    console.log(ret);
    process.exit();
  });

//////////////
// Solution //
//////////////

function solution(input) {
  // [1] 내림차순으로 배열 정렬
  const [N, ...unsorted] = input.flatMap((v) => v);
  let res = 0;
  let pPtr = 0;
  let nPtr = N - 1;
  // arr.sort((a, b) => b - a);
  const arr = countSort(unsorted, -1000, 1000);

  // [2] 길이가 1인 에지케이스
  if (N === 1) return arr[0];

  // [3] 2중 좌우 포인터 이동
  // [3-1] 양수 포인터
  while (pPtr < N - 1 && arr[pPtr] > 0 && arr[pPtr + 1] > 0) {
    if (arr[pPtr] === 1 || arr[pPtr + 1] === 1) {
      res += arr[pPtr] + arr[pPtr + 1];
    } else {
      res += arr[pPtr] * arr[pPtr + 1];
    }
    pPtr += 2;
  }
  // [3-2] 음수 포인터
  while (nPtr > 0 && arr[nPtr] < 0 && arr[nPtr - 1] < 0) {
    res += arr[nPtr] * arr[nPtr - 1];
    nPtr -= 2;
  }

  // [4] 좌측 양수 포인터 이동
  if (arr[pPtr] > 0) {
    res += arr[pPtr];
    pPtr += 1;
  }

  // [5] 남은 중간영역 계산
  const gap = nPtr - pPtr;
  if (gap === 0) {
    res += arr[nPtr];
  }

  return res;
}

// Count Sort 구현 함수 (내림차순)
function countSort(arr, min, max) {
  // [1] 최대, 최소 값의 차이 만큼 크기를 가진 배열 생성
  const length = max - min + 1;
  const auxiliary = new Array(length).fill(0);
  const res = [];

  // [2] 배열의 인덱스에 대해 갯수만큼 값 증가
  arr.forEach((item) => {
    auxiliary[-item - min] += 1;
  });

  // [3] 큰 순서대로 정렬 배열로 삽입
  auxiliary.forEach((v, i) => {
    while (v > 0) {
      v--;
      res.push(-i - min);
    }
  });
  return res;
}
