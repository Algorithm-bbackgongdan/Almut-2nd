/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week3/backjoon-2343.txt", "utf-8", (_, data) => {
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
  const [lectureCount, containerCount] = input[0];
  const lectures = input[1];
  let minSize = 0;
  let maxSize = lectures.reduce((ac, v) => ac + v, 0);
  let currentSize = 0;

  // [1] L포인터(minSize)와 R포인터(maxSize)를 기준으로 이진탐색합니다
  while (minSize !== maxSize) {
    currentSize = ~~((minSize + maxSize) / 2);
    // [2] 현재 너비(평균값)을 기준으로 컨테이너(디스크)가 작은지 확인합니다)
    const containerIsSmall = isContainerSmall(
      lectures,
      lectureCount,
      currentSize,
      containerCount
    );
    // [3] 디스크가 작을 경우 L포인터(minSize)를 증가시킵니다
    if (containerIsSmall) {
      minSize = currentSize + 1;
      // [4] 디스크가 클 경우 R포인터(maxSize)를 감소시킵니다
    } else {
      maxSize = currentSize;
    }
  }
  return minSize;
}

// 주어진 너비를 기준으로 컨테이너(디스크) 개수의 초과 여부를 반환합니다
function isContainerSmall(lectures, length, width, containerCount) {
  let totalCount = 0;
  let currentSum = 0;
  for (let i = 0; i < length; i++) {
    // [1] 강의 길이가 디스크 너비보다 작은지 확인합니다
    if (lectures[i] > width) {
      return true;
      // [2] 현재까지 강의 길이의 합이 디스크 너비보다 작은 지 확인합니다
    } else if (currentSum + lectures[i] <= width) {
      currentSum += lectures[i];
      // [3] 강의 길이의 합이 디스크 너비보다 큰 경우 새로운 디스크를 생성합니다
    } else {
      currentSum = lectures[i];
      totalCount += 1;
    }
  }
  // [4] 남은 강의가 존재할 경우 디스크를 추가합니다
  if (currentSum) totalCount += 1;
  return totalCount > containerCount;
}
