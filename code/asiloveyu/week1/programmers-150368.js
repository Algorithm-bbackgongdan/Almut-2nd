/**
 * 주어진 인자를 이용해 서비스 구독자 수와 매출을 반환합니다.
 * @param {*} users - 사용자(할인율, 서비스 전환 지점) 배열
 * @param {*} emoticons - 이모티콘 별 가격
 * @param {*} discounts - 이모티콘 별 할인율
 * @returns
 */
function calculateResult(users, emoticons, discounts) {
  let subscription = 0;
  let sales = 0;
  // [1] 총 매출과 구독자수를 구합니다.
  for (const user of users) {
    let eachSale = 0;
    for (let j = 0; j < emoticons.length; j++) {
      if (discounts[j] >= user[0]) {
        eachSale += ((100 - discounts[j]) / 100) * emoticons[j];
      }
    }
    // [1-2] 제약조건을 토대로 구독자수와 매출을 더합니다.
    if (eachSale >= user[1]) {
      subscription += 1;
    } else {
      sales += eachSale;
    }
  }
  return [subscription, sales];
}

/**
 * 가능한 할인율 중복 순열을 재귀적으로 in-place 반환합니다.
 * @param {*} source - 서로 다른 n개의 배열
 * @param {*} current - 완성 중인 배열
 * @param {*} candidate - 모든 배열의 집합 (순열)
 * @param {*} k - 배열의 길이
 */
function getCombination(source, current, candidate, k) {
  if (current.length === k) {
    candidate.push(current);
  } else {
    for (value of source) {
      const next = current.concat(value);
      getCombination(source, next, candidate, k);
    }
  }
}

function solution(users, emoticons) {
  // [1] 할인율의 중복 순열을 구합니다.

  const discountSet = [];
  const emoticonCount = emoticons.length;
  const discountRate = [10, 20, 30, 40];
  let maxSubscription = 0;
  let maxSales = 0;

  getCombination(discountRate, [], discountSet, emoticonCount);

  // [2] 중복 순열에 대해 최대 구독자 수 + 매출을 구합니다.

  for (const discounts of discountSet) {
    const [subscription, sales] = calculateResult(users, emoticons, discounts);
    if (maxSubscription < subscription) {
      maxSubscription = subscription;
      maxSales = sales;
    } else if (maxSubscription === subscription && maxSales <= sales) {
      maxSales = sales;
    }
  }
  return [maxSubscription, maxSales];
}
