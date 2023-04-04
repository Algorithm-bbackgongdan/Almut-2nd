/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week4/backjoon-1956.txt", "utf-8", (_, data) => {
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
  const [[v, e], ...routes] = input;
  const MAX = Number.MAX_VALUE;
  const mat = new Array(v + 1).fill(0).map((_) => new Array(v + 1).fill(MAX));

  // [1] 각 도로를 기반으로 경로 매트릭스를 생성합니다
  routes.forEach((route) => {
    const [start, end, cost] = route;
    mat[start][end] = cost;
  });

  // [2] 경로 매트릭스에 대해 최단거리를 구합니다
  for (let m = 1; m < v + 1; m++) {
    for (let y = 1; y < v + 1; y++) {
      for (let x = 1; x < v + 1; x++) {
        mat[y][x] = Math.min(mat[y][x], mat[y][m] + mat[m][x]);
      }
    }
  }

  // [3] 자기 자신으로 향하는 최단거리 중 가장 작은 값을 고릅니다
  let min = MAX;
  for (let e = 1; e < v + 1; e++) {
    if (mat[e][e] !== MAX && mat[e][e] < min) {
      min = mat[e][e];
    }
  }
  if (min === MAX) {
    return -1;
  }
  return min;
}
