/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week5/backjoon-19237.txt", "utf-8", (_, data) => {
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

// [*] 상어 클래스 입니다
class Shark {
  id;
  alive;
  position;
  rotation;
  directionSet;

  constructor(id) {
    this.id = id;
    this.alive = true;
  }

  kill() {
    this.alive = false;
  }

  set rotation(value) {
    this.rotation = value;
  }
  set position(value) {
    this.position = value;
  }
  set directionSet(value) {
    this.directionSet = value;
  }
}

// [*] 지도의 개별 셀 클래스 입니다
class mapCell {
  constructor(occupient, time) {
    this.occupient = occupient;
    this.time = time;
  }
}

function solution(input) {
  const map = [];
  let sharks = [];
  let rows = 0;
  const [N, M, K] = input[rows++];

  // [1] 지도의 개별 셀 객체(냄새, 타이머)와 상어를 초기화합니다
  let y = 0;
  while (rows <= N) {
    const row = input[rows++];
    const mapRow = [];

    row.forEach((value, x) => {
      if (value !== 0) {
        const shark = new Shark(value);
        shark.position = [x, y];
        sharks.push(shark);
        mapRow.push(new mapCell(value, K));
      } else {
        mapRow.push(new mapCell(value, 0));
      }
    });
    map.push(mapRow);
    y++;
  }

  // [2] 상어를 id 순으로 오름차순 정렬합니다 (1, 2, 3, 4)
  sharks = sharks.sort((sharkA, sharkB) => {
    return sharkA.id - sharkB.id;
  });

  // [3] 상어의 최초 회전 방향을 초기화합니다
  const initialRotation = input[rows++];
  sharks.forEach((shark, id) => {
    shark.rotation = initialRotation[id];
  });

  // [4] 상어의 회전 우선순위를 초기화합니다
  let index = 0;
  while (rows !== N + 2 + M * 4) {
    const up = input[rows++];
    const down = input[rows++];
    const left = input[rows++];
    const right = input[rows++];

    // [4-1] 회전방향 인덱스 (1, 2, 3, 4)와 배열 인덱스를 맞추어줍니다
    sharks[index].directionSet = [null, up, down, left, right];
    index++;
  }

  // [5] 시간에 맞추어 하나씩 증가시키며 상어의 위치를 업데이트합니다
  let t = 0;
  while (t <= 999) {
    // [5-1] 상어의 회전 방향을 결정하고 이동 후 위치를 업데이트 합니다
    for (const shark of sharks) {
      makeMovement(shark, map, N);
    }

    // [5-2] 지도의 모든 타이머를 1씩 감소시킵니다
    for (let x = 0; x < N; x++) {
      for (let y = 0; y < N; y++) {
        map[y][x].time > 0 && map[y][x].time--;
        if (map[y][x].time === 0) {
          map[y][x].occupient = 0;
        }
      }
    }

    // [5-3] 중복된 상어를 제거합니다
    for (const shark of sharks) {
      const [x, y] = shark.position;
      // [5-3-1] 새로운 셀에 중복된 상어가 있는 경우, 상어를 죽입니다 (불쌍하네요)
      if (map[y][x].occupient !== 0 && map[y][x].occupient !== shark.id) {
        shark.kill();
      } else {
        // [5-3-2] 새로운 셀에 중복된 상어가 없는 경우 위치를 업데이트 합니다
        map[y][x].occupient = shark.id;
        map[y][x].time = K;
      }
    }

    // [5-4] 죽인 상어를 배열에서 제거합니다
    sharks = sharks.filter((shark) => {
      return shark.alive === true;
    });

    // [5-5] 시간을 증가시키고, 상어의 길이가 1인 경우 결과를 반환합니다
    t++;
    if (sharks.length === 1) {
      return t;
    }
  }
  return -1;
}

// [*] 현재 회전상태(rotation)에 따라 방향 집합(directionSet)에서
//     방향 순서(directionOrder)를 추출한 뒤 이를 기준으로 움직입니다
function makeMovement(shark, map, N) {
  const dpos = [null, [0, -1], [0, 1], [-1, 0], [1, 0]];
  const currentRotation = shark.rotation;
  const currentDirectionOrder = shark.directionSet[currentRotation];
  const [x, y] = shark.position;

  // [1] 빈 공간 찾기
  for (const i of currentDirectionOrder) {
    const [dx, dy] = dpos[i];
    const [nx, ny] = [x + dx, y + dy];
    if (nx >= N || nx < 0) continue;
    if (ny >= N || ny < 0) continue;

    // [1-1] 상어 객체 업데이트
    if (map[ny][nx].occupient === 0) {
      shark.position = [nx, ny];
      shark.rotation = i;
      return;
    }
  }

  // [2] 지나온 공간 찾기
  for (const i of currentDirectionOrder) {
    const [dx, dy] = dpos[i];
    const [nx, ny] = [x + dx, y + dy];
    if (nx >= N || nx < 0) continue;
    if (ny >= N || ny < 0) continue;

    // [2-1] 상어 객체 업데이트
    if (map[ny][nx].occupient === shark.id) {
      shark.position = [nx, ny];
      shark.rotation = i;
      return;
    }
  }
}
