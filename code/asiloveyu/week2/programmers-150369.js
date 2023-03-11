function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let deliveryOnHold = 0;
  let pickupOnHold = 0;

  // 가장 먼 거리의 집부터 방문해 짐을 나릅니다.
  for (let i = n - 1; i >= 0; i--) {
    deliveryOnHold += deliveries[i];
    pickupOnHold += pickups[i];

    // 공간이 남는 경우 다음 가까운 집의 분량을 미리 나릅니다.
    while (deliveryOnHold > 0 || pickupOnHold > 0) {
      deliveryOnHold -= cap;
      pickupOnHold -= cap;
      answer += (i + 1) * 2;
    }
  }
  return answer;
}
