/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week1/backjoon-2212.txt", "utf-8", (_, data) => {
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

const solution = (input) => {
  const sensorCount = input[0];
  const relayCount = input[1];
  const distanceMap = [];

  // 센서를 1차원 공간에 좌표 순서대로 배열합니다.
  const sensorMap = input[2].sort((a, b) => a - b);

  // 각 센서 간 거리 배열을 구합니다.
  for (let i = 0; i < sensorMap.length - 1; i++) {
    const v = Math.abs(sensorMap[i] - sensorMap[i + 1]);
    v !== 0 && distanceMap.push(v);
  }

  // 거리 배열을 오름차순으로 정렬합니다.
  distanceMap.sort((a, b) => a - b);

  // 거리 배열의 큰 값을 순서대로 (중계기 갯수 - 1)개를 제거한 뒤 거리 배열을 모두 더합니다.
  return distanceMap
    .slice(0, distanceMap.length - (relayCount - 1))
    .reduce((accum, v) => accum + v, 0);
};
