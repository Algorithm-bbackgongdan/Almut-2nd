function solution(fees, records) {
  const cars = new Map();
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  const LAST_CALL = getMinute("23:59");

  // [1] Record의 IN, OUT을 기준으로 최대 체류 시간을 구합니다
  // cars의 구조: [entrance, time accumulator]
  records.forEach((record) => {
    const [time, number, action] = record.split(" ");
    const current = getMinute(time);
    // [1-1] 차가 아직 없는 경우 새로 생성합니다
    if (!cars.has(number)) cars.set(number, [-1, 0]);
    // [1-2] 입출차를 기준으로 차의 총 체류 시간을 구합니다
    const [entrance, totalTime] = cars.get(number);
    if (action === "IN") {
      cars.set(number, [current, totalTime]);
    } else if (action === "OUT") {
      const gap = current - entrance;
      cars.set(number, [-1, totalTime + gap]);
    }
  });

  // [2] 각 차의 체류 시간을 기준으로 요금을 구합니다
  // cars의 구조: [fee]
  cars.forEach((car, number) => {
    let [entrance, totalTime] = car;
    // [2-1] 출차 기록이 없는 경우 마지막 시간을 기준으로 구합니다
    if (entrance !== -1) {
      const gap = LAST_CALL - entrance;
      totalTime += gap;
    }
    // [2-2] 기본시간(baseTime)과 단위시간(unitTime)을 기준으로 계산합니다
    const value = totalTime - baseTime;
    if (value <= 0) {
      cars.set(number, baseFee);
      return;
    } else {
      const quotient = ~~(value / unitTime);
      const remain = value % unitTime ? 1 : 0;
      cars.set(number, baseFee + (quotient + remain) * unitFee);
    }
  });

  // [3] 차 배열을 번호 순으로 정렬한 뒤, 비용을 추출합니다
  const answer = [...cars]
    .sort((carA, carB) => {
      return parseInt(carA[0], 10) - parseInt(carB[0], 10);
    })
    .map(([_, cost]) => cost);

  return answer;
}

function getMinute(time) {
  const [hh, mm] = time.match(/\d{2}/g).map((v) => parseInt(v, 10));
  return hh * 60 + mm;
}
