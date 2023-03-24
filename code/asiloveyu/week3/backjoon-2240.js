/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week3/backjoon-2240.txt", "utf-8", (_, data) => {
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
  const [T, W, ...schedule] = input.flat();
  const dp = new Array(3)
    .fill(0)
    .map((_) => new Array(T).fill(0).map((_) => new Array(W + 1).fill(0)));
  const LEFT = 1;
  const RIGHT = 2;

  //dp[현재 나무][현재 시간][움직임 횟수]

  // [1] Time = 0일때 조건을 채웁니다
  for (let move = 0; move < W + 1; move++) {
    if (schedule[0] === LEFT) {
      dp[LEFT][0][move] = 1;
      dp[RIGHT][0][move] = 0;
    } else if (schedule[0] === RIGHT) {
      dp[LEFT][0][move] = 0;
      dp[RIGHT][0][move] = 1;
    }
  }
  dp[RIGHT][0][0] = 0;

  // [2] Move = 0일때 조건을 채웁니다
  let leftAccum = dp[LEFT][0][0];
  for (let time = 1; time < T; time++) {
    if (schedule[time] === LEFT) {
      leftAccum++;
    }
    dp[LEFT][time][0] = leftAccum;
    dp[RIGHT][time][0] = 0;
  }

  // [3] DP를 통해 배열을 채웁니다
  for (let time = 1; time < T; time++) {
    for (let move = 1; move < W + 1; move++) {
      if (schedule[time] === LEFT) {
        dp[LEFT][time][move] = Math.max(
          dp[LEFT][time - 1][move] + 1,
          dp[RIGHT][time - 1][move - 1] + 1
        );
        dp[RIGHT][time][move] = Math.max(
          dp[LEFT][time - 1][move - 1],
          dp[RIGHT][time - 1][move]
        );
      } else if (schedule[time] === RIGHT) {
        dp[LEFT][time][move] = Math.max(
          dp[LEFT][time - 1][move],
          dp[RIGHT][time - 1][move - 1]
        );
        dp[RIGHT][time][move] = Math.max(
          dp[LEFT][time - 1][move - 1] + 1,
          dp[RIGHT][time - 1][move] + 1
        );
      }
    }
  }

  // [4] 시간 내 (T-1) 배열의 최대값을 구합니다
  let ans = 0;
  for (let i = 0; i < W + 1; i++) {
    const currentMax = Math.max(dp[LEFT][T - 1][i], dp[RIGHT][T - 1][i]);
    ans = Math.max(ans, currentMax);
  }
  return ans;
}
