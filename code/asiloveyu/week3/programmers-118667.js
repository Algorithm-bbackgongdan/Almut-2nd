function solution(queue1, queue2) {
  // [1] queue를 하나로 합친 뒤 현재 합을 나타내는 포인터를 start, end로 정합니다
  let start = 0;
  let end = queue1.length - 1;
  let queue = queue1.concat(queue2);
  let step = 0;
  let current = queue1.reduce((acc, v) => acc + v, 0);
  const target = queue.reduce((acc, v) => acc + v, 0) / 2;
  const length = queue.length;

  // [2] start, end가 역전되거나, 끝에 도달하기 전까지 반복합니다
  while (start <= end && start < length && end < length) {
    // [3] current(현재 합)이 목표보다 큰 경우 start 포인터를 증가시킵니다
    if (current > target) {
      current -= queue[start];
      start++;
      step++;
      // [4] current(현재 합)이 목표보다 작은 경우 end 포인터를 증가시킵니다
    } else if (current < target) {
      end++;
      current += queue[end];
      step++;
      // [5] current(현재 합)이 목표와 같은 경우 step을 반환합니다
    } else if (current === target) {
      return step;
    }
  }

  // [6] current(현재 합)이 목표에 도달하지 못한 경우 -1을 반환합니다
  return -1;
}
