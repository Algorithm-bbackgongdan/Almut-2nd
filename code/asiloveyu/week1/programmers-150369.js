function solution(cap, n, deliveries, pickups) {
  let dMoved = 0;
  let pMoved = 0;
  let dist = n - 1;
  let ans = 0;

  // 가장 먼 집부터 가장 가까운 집까지 순환합니다.
  while (dist >= 0) {
    // 만약 옮긴 짐의 총합이 목표 집의 짐보다 크면 다음 집으로 이동합니다.
    if (dMoved >= deliveries[dist] && pMoved >= pickups[dist]) {
      // 옮긴 짐에서 현재 집의 짐을 빼 추가로 옮긴 짐을 저장합니다.
      dMoved -= deliveries[dist];
      pMoved -= pickups[dist];
      dist -= 1;
      continue;
    }
    // 매 순환마다 옮긴 짐을 더합니다.
    dMoved += cap;
    pMoved += cap;
    ans += (dist + 1) * 2;
  }

  return ans;
}
