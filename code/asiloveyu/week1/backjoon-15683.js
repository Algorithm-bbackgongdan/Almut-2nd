/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

let input = [];
const fs = require("fs");

fs.readFile("code/asiloveyu/week1/backjoon-15683.txt", "utf-8", (_, data) => {
  data
    .toString()
    .split("\n")
    .forEach((line) => {
      input.push(line.split(" ").map((v) => parseInt(v)));
    });
  console.log(solution(input));
});

////////////////////////////////////
// Reading file from backjoon env //
////////////////////////////////////

// let input = [];
// const readline = require("readline").createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// readline
//   .on("line", function (data) {
//     input.push(
//       data
//         .trim()
//         .split(" ")
//         .map((v) => parseInt(v))
//     );
//   })
//   .on("close", function () {
//     const ret = solution(input);
//     console.log(ret);
//     process.exit();
//   });

//////////////
// Solution //
//////////////

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
const direction = {
  1: [[0], [1], [2], [3]],
  2: [
    [0, 2],
    [1, 3],
  ],
  3: [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
  ],
  4: [
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 0],
    [3, 0, 1],
  ],
  5: [[0, 1, 2, 3]],
};
let ans = Number.MAX_VALUE;

const watch = (x, y, direction, tempMap, n, m) => {
  let [nx, ny] = [x, y];
  for (type of direction) {
    while (true) {
      nx += dx[type];
      ny += dy[type];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m || tempMap[nx][ny] === 6) {
        break;
      } else if (tempMap[nx][ny] === 0) {
        tempMap[nx][ny] = "#";
      }
    }
  }
};

const dfs = (index, map, cctv, n, m) => {
  let temp = JSON.parse(JSON.stringify(map));

  if (index === cctv.length) {
    count = 0;
    for (t of temp) {
      count += t.filter((item) => item === 0).length;
    }
    ans = ans < count ? ans : count;
    return;
  }

  const [x, y, type] = cctv[index];
  for (d of direction[type]) {
    watch(x, y, d, temp, n, m);
    dfs(index + 1, temp, cctv, n, m);
    temp = JSON.parse(JSON.stringify(map));
  }
};

const solution = (input) => {
  const n = input[0][0];
  const m = input[0][1];
  const map = [...input.slice(1)];
  const cctv = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (map[i][j] !== 0 && map[i][j] !== 6) {
        cctv.push([i, j, map[i][j]]);
      }
    }
  }

  dfs(0, map, cctv, n, m);

  return ans;
};
