function solution(n, m, x, y, r, c, k) {
  let [currentX, currentY, maxX, maxY, targetX, targetY, step] = [
    y,
    x,
    m,
    n,
    c,
    r,
    k,
  ];
  let ans = "";
  let dist = getDistance([currentX, currentY], [targetX, targetY]);

  // [1] 도달할 수 없는 경우 "impossible"을 반환합니다
  const distRemain = dist % 2;
  const stepRemain = step % 2;
  if (distRemain !== stepRemain) return "impossible";
  if (dist > step) return "impossible";

  // [2] 가능한 dl 패턴을 모두 시도합니다
  while (dist < step) {
    if (currentY !== maxY) {
      ans += "d";
      currentY++;
    } else if (currentX !== 1) {
      ans += "l";
      currentX--;
    } else {
      break;
    }
    step--;
    dist = getDistance([currentX, currentY], [targetX, targetY]);
  }

  // [3] 가능한 rl 패턴을 모두 시도합니다
  let moveRight = true;
  while (dist < step) {
    if (moveRight) {
      ans += "r";
      moveRight = !moveRight;
      currentX += 1;
    } else {
      ans += "l";
      moveRight = !moveRight;
      currentX -= 1;
    }
    dist = getDistance([currentX, currentY], [targetX, targetY]);
    step--;
  }

  // [4] 목적지로 이동합니다
  if (step) {
    const xDist = targetX - currentX;
    const yDist = targetY - currentY;
    if (yDist > 0) {
      ans += "d".repeat(Math.abs(yDist));
    }
    if (xDist < 0) {
      ans += "l".repeat(Math.abs(xDist));
    }
    if (xDist > 0) {
      ans += "r".repeat(Math.abs(xDist));
    }
    if (yDist < 0) {
      ans += "u".repeat(Math.abs(yDist));
    }
  }
  return ans;
}

function getDistance(current, target) {
  const [cx, cy] = current;
  const [tx, ty] = target;
  return Math.abs(cx - tx) + Math.abs(cy - ty);
}
