function solution(today, terms, privacies) {
  // [1] 조건을 숫자(day)값 기준의 오브젝트로 변환합니다
  const baseYear = 2020;
  const condition = terms.reduce((obj, item) => {
    const [key, value] = item.split(/\s/);
    obj[key] = parseInt(value) * 28;
    return obj;
  }, {});
  // [2] 오늘 날짜를 숫자(day)값 기준으로 변환합니다
  const todayAsNumber = getDateAsNumber(today, baseYear);
  // [3] 숫자(day)값을 기준으로 차이를 구해 결과를 반환합니다.
  const answer = privacies.reduce((answer, item, i) => {
    const [date, type] = item.split(/\s/);
    const dateAsNumber = getDateAsNumber(date, baseYear);
    const gap = todayAsNumber - dateAsNumber;
    if (condition[type] <= gap) {
      return [...answer, i + 1];
    }
    return answer;
  }, []);

  return answer;
}

// f: 날짜 문자열을 숫자(day)값으로 변환합니다
function getDateAsNumber(date, baseYear) {
  const [year, month, day] = date.split(/\./).map((v) => parseInt(v));
  const res = (year - baseYear) * 12 * 28 + (month - 1) * 28 + day;
  return res;
}
