function solution(board) {
  const N = board.length;
  const costBoard = new Array(N)
    .fill(0)
    .map((_) => new Array(N).fill(0).map((_) => new Array(4).fill(-1)));
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  const stack = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
  ];
  costBoard[0][0] = [0, 0, -1, -1];

  // [1] Iterative stack을 이용해 DFS를 실행합니다
  while (stack.length !== 0) {
    const [x, y, cost, rotation] = stack.pop();
    // [2] 각 방향에 대해서
    for (let i = 0; i < 4; i++) {
      // [2-1] 새로운 좌표를 구합니다
      const [dx, dy] = directions[i];
      const [nx, ny] = [x + dx, y + dy];
      // [2-2] 해당 좌표가 유효한지 검증합니다 (테이블 내, 장애물이 아님)
      if (!isValid([nx, ny], board, N)) continue;
      // [2-3] 과거 진행방향(rotation)과 일치할 경우 100, 아니면 600을 더합니다
      const dcost = rotation === i ? 100 : 600;
      const ncost = dcost + cost;
      // [2-4] 새로운 진행방향(i)에 해당하는 최소값을 꺼냅니다
      const pcost = costBoard[ny][nx][i];
      // [2-5] 최소값을 초기화 하거나, 최소값보다 작을 경우 이를 최소값으로 할당하고 stack에 넣습니다
      if (pcost === -1 || ncost < pcost) {
        costBoard[ny][nx][i] = ncost;
        stack.push([nx, ny, ncost, i]);
      }
    }
  }
  return Math.min(...costBoard[N - 1][N - 1].filter((v) => v !== -1));
}

function isValid([x, y], board, N) {
  if (x < 0 || x >= N) return false;
  if (y < 0 || y >= N) return false;
  if (board[y][x] === 1) return false;
  return true;
}
