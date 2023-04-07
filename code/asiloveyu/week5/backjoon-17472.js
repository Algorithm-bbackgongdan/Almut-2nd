/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week5/backjoon-17472.txt", "utf-8", (_, data) => {
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
  const [[height, width], ...map] = input;
  const direction = [
    [0, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
  ];
  const path = [];
  let flag = 2;

  // [1] Map의 섬에 index를 부여
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      if (map[y][x] === 1) {
        fillIsland([x, y], flag, direction, map, width, height);
        flag++;
      }
    }
  }

  // [2] 각 섬에 대해서 edge 탐색
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      if (map[y][x] !== 0) {
        for (const d of direction) {
          const [dest, cost] = checkPath([x, y], d, map, width, height);
          // edge의 구성 (시작, 끝, 비용(길이))
          if (dest !== -1) path.push([map[y][x], dest, cost]);
        }
      }
    }
  }

  // [3] 각 edge에 대해 거리를 기준으로 오름차 정렬
  path.sort((a, b) => {
    return a[2] - b[2];
  });

  // [4] Kruskal 알고리즘 기반 MST 수행
  const parent = new Array(flag).fill(0).map((_, i) => i);
  const SPAN_EDGE = flag - 3; // flag = (0, 1, ...) = island 개수 + 2
  let pathCount = 0;
  let costSum = 0;

  // [4-1] 거리가 낮은 순으로 모든 edge(path)에 대해 union 수행
  for (p of path) {
    const [a, b, cost] = p;
    const ap = findParent(parent, a);
    const bp = findParent(parent, b);

    if (ap !== bp) {
      pathCount++;
      costSum += cost;
      union(parent, ap, bp);
    }
    if (pathCount === SPAN_EDGE) break;
  }

  // [4-2] 결과 반환
  if (pathCount !== SPAN_EDGE) return -1;
  return costSum;
}

// Union-Find에서 Union 함수
function union(parent, a, b) {
  parent[a] = b;
}

// Union-Find에서 Find 함수
function findParent(parent, vertex) {
  // 부모가 자기 자신이 아니면 path optimization을 수행하며 부모 탐색
  if (vertex !== parent[vertex]) {
    parent[vertex] = findParent(parent, parent[vertex]);
  }
  return parent[vertex];
}

// 길의 존재 여부를 확인하는 함수
function checkPath(start, direction, map, w, h) {
  const [dx, dy] = direction;
  let [x, y] = start;
  const startValue = map[y][x];
  let movement = 0;

  // 진행방향으로 한칸씩 전진
  do {
    x += dx;
    y += dy;
    movement++;
    if (x >= w || x < 0) return [-1, 0];
    if (y >= h || y < 0) return [-1, 0];
    if (map[y][x] === startValue) return [-1, 0];
  } while (map[y][x] === 0);

  // 다리의 길이는 움직임 - 1
  const bridgeLen = movement - 1;

  // 다리 길이가 2 이상인 경우만 값 반환 (목표점, 다리 길이)
  if (bridgeLen >= 2) return [map[y][x], bridgeLen];
  else return [-1, 0];
}

// 각 섬에 인덱스를 부여하는 함수
function fillIsland(start, flag, direction, map, w, h) {
  const [x, y] = start;
  map[y][x] = flag;
  // 상하좌우로 확장하며 섬에 인덱스 값 부여
  for (const d of direction) {
    const [dx, dy] = d;
    const [nx, ny] = [x + dx, y + dy];
    if (0 <= nx && nx < w && 0 <= ny && ny < h && map[ny][nx] === 1) {
      fillIsland([nx, ny], flag, direction, map, w, h);
    }
  }
}
