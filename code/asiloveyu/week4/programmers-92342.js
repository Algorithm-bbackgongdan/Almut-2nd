function solution(n, info) {
  const lion = new Array(11).fill(0);
  const [lionScore, peachScore, lionArray] = dfs(lion, info, n, 0, 0, 0);

  if (lionScore <= peachScore) {
    return [-1];
  } else {
    return lionArray;
  }
}

function dfs(lion, peach, arrow, index, lionScore, peachScore) {
  // [1] 마지막인 경우
  if (index === 10) {
    const newLion = [...lion];
    newLion[index] = arrow;
    return [lionScore, peachScore, newLion];
  }
  if (arrow === 0) {
    for (let i = index; i < 11; i++) {
      if (peach[i] > 0) peachScore += 10 - i;
    }
    return [lionScore, peachScore, lion];
  }

  let winCase, loseCase;

  // [2] 라이언이 해당 점수에서 이기는 경우
  const remainArrow = arrow - (peach[index] + 1);
  // [2-1] 사용가능한 화살이 피치보다 많아야 함
  if (remainArrow >= 0) {
    const newLion = [...lion];
    newLion[index] = peach[index] + 1;
    winCase = dfs(
      newLion,
      peach,
      remainArrow,
      index + 1,
      lionScore + (10 - index),
      peachScore
    );
  }

  // [2] 라이언이 해당 점수에서 지는 경우
  if (peach[index] !== 0) {
    loseCase = dfs(
      lion,
      peach,
      arrow,
      index + 1,
      lionScore,
      peachScore + (10 - index)
    );
  } else {
    loseCase = dfs(lion, peach, arrow, index + 1, lionScore, peachScore);
  }

  // [3] 최적값 반환
  // [3-1] 라이언이 해당 점수에서 이길 수 없는 경우
  if (!winCase) return loseCase;
  // [3-2] 라이언이 더 큰 점수차로 이기는 경우를 반환
  const [winLionScore, winPeachScore] = winCase;
  const [loseLionScore, losePeachScore] = loseCase;
  const winScoreGap = winLionScore - winPeachScore;
  const loseScoreGap = loseLionScore - losePeachScore;

  if (winScoreGap !== loseScoreGap) {
    return winScoreGap > loseScoreGap ? winCase : loseCase;
    // [3-3] 점수차가 같은 경우 낮은 값이 더 많은 경우를 반환
  } else if (winScoreGap === loseScoreGap) {
    return getSkewedArray(winCase, loseCase);
  }
}

// 두 배열 중 낮은 값이 더 많은 배열을 반환
function getSkewedArray(inputOne, inputTwo) {
  const arrOne = inputOne[2];
  const arrTwo = inputTwo[2];

  for (let i = 10; i >= 0; i--) {
    if (arrOne[i] > arrTwo[i]) {
      return inputOne;
    } else if (arrTwo[i] > arrOne[i]) {
      return inputTwo;
    }
  }
  return arrOne;
}
