/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week2/backjoon-16234.txt", "utf-8", (_, data) => {
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
  const [N, L, R] = input[0];
  const map = input.slice(1);
  const parts = new Array(N).fill(0).map((_, i) => i);
  let populationMoved = true;
  let dayCount = 0;

  while (true) {
    const visit = new Array(N).fill(0).map(() => new Array(N).fill(false));
    populationMoved = false;

    // [1] 지도의 모든 좌표를 순환합니다
    for (let y = 0; y < N; y++) {
      for (let x = 0; x < N; x++) {
        // [2] 각 좌표에 대해 연합을 탐색합니다
        if (visit[y][x] === false) {
          const ally = searchAlly([y, x], visit, map, N, L, R);
          const count = ally.length;
          // [3] 연합 내 인구 평균 값을 구하고 해당 값을 적용합니다
          const value = ally.reduce((accum, [y, x]) => accum + map[y][x], 0);
          const newValue = parseInt(value / count);
          ally.forEach(([y, x]) => {
            map[y][x] = newValue;
          });
          // [4] 인구이동이 있는 경우 이를 플래그로 표기합니다
          if (count > 1) {
            populationMoved = true;
          }
        }
      }
    }
    if (!populationMoved) {
      break;
    }
    dayCount++;
  }

  return dayCount;
};

const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];

function searchAlly(cord, visit, map, N, L, R) {
  // [1] 탐색한 좌표에 대해 표기합니다
  const [y, x] = cord;
  const ally = [[y, x]];
  visit[y][x] = true;

  // [2] 현재 좌표를 기준으로 상하좌우를 탐색합니다.
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (ny >= 0 && ny < N && nx >= 0 && nx < N && visit[ny][nx] === false) {
      const gap = Math.abs(map[ny][nx] - map[y][x]);
      if (L <= gap && gap <= R) {
        ally.push(...searchAlly([ny, nx], visit, map, N, L, R));
      }
    }
  }
  return ally;
}
