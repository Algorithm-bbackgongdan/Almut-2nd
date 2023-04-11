/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week5/backjoon-17822.txt", "utf-8", (_, data) => {
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

class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
    this.tail = 0;
  }
  enqueue(value) {
    this.queue.push(value);
    this.head++;
  }
  dequeue() {
    if (this.tail > this.head) return;
    const value = this.queue[this.tail];
    this.tail++;
    return value;
  }
  length() {
    return this.head - this.tail;
  }
}

function solution(input) {
  let cursor = 0;
  const [N, M, T] = input[cursor++];
  const board = [[]];
  const info = [];
  while (cursor < N + 1) {
    board.push(input[cursor++]);
  }
  while (cursor < N + T + 1) {
    info.push(input[cursor++]);
  }
  let time = 0;
  while (time < T) {
    rotate(info[time], board, N, M);
    let adjacentCount = 0;
    let numberCount = 0;
    let sum = 0;

    for (let b = 1; b <= N; b++) {
      for (let i = 0; i < M; i++) {
        if (board[b][i] > 0) {
          adjacentCount += bfs([b, i], board, N, M);
          sum += board[b][i];
          numberCount += 1;
        }
      }
    }
    if (adjacentCount === 0 && numberCount !== 0) {
      let boardAvg = sum / numberCount;
      for (let b = 1; b <= N; b++) {
        for (let i = 0; i < M; i++) {
          if (board[b][i] === 0) continue;
          if (board[b][i] > boardAvg) {
            board[b][i]--;
          } else if (board[b][i] < boardAvg) {
            board[b][i]++;
          }
        }
      }
    }
    time++;
  }

  let ans = 0;
  for (let b = 1; b <= N; b++) {
    for (let i = 0; i < M; i++) {
      ans += board[b][i];
    }
  }

  return ans;
}

function bfs(start, board, N, M) {
  const [b, i] = start;
  const value = board[b][i];
  const queue = new Queue();
  let count = 0;
  queue.enqueue([b, i]);

  // queue operation 수행
  while (queue.length() > 0) {
    const [cb, ci] = queue.dequeue();
    if (board[cb][ci] !== value) continue;
    board[cb][ci] = 0;
    count++;
    const ub = cb + 1;
    const db = cb - 1;
    const ri = (ci + 1) % M;
    const li = (ci - 1 + M) % M;

    if (ub <= N) queue.enqueue([ub, ci]);
    if (db >= 1) queue.enqueue([db, ci]);
    queue.enqueue([cb, ri]);
    queue.enqueue([cb, li]);
  }

  // 좌표 리셋
  if (count === 1) {
    board[b][i] = value;
    return 0;
  }
  return count;
}

function rotate([x, d, k], board, N, M) {
  let index = 0;
  while (index < N) {
    index++;
    if (index % x !== 0) continue;
    const newBoard = new Array(M);
    if (d === 0) {
      // 시계방향 회전
      for (let i = 0; i < M; i++) {
        const ni = (i + k) % M;
        newBoard[ni] = board[index][i];
      }
    } else if (d === 1) {
      // 반시계방향 회전
      for (let i = 0; i < M; i++) {
        const ni = (i - k + M) % M;
        newBoard[ni] = board[index][i];
      }
    }
    board[index] = newBoard;
  }
}
