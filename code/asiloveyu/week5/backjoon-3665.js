/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week5/backjoon-3665.txt", "utf-8", (_, data) => {
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

function solution(input) {
  let ans = "";
  let line = 1;

  while (line < input.length) {
    const [teamCount] = input[line++];
    const previousOrder = input[line++];
    const [changeCount] = input[line++];
    const changedDirectionArray = [];

    for (let i = 0; i < changeCount; i++) {
      changedDirectionArray.push(input[line++]);
    }

    const directionArray = new Array(teamCount + 1)
      .fill(0)
      .map((_) => new Array());
    const inDegreeArray = new Array(teamCount + 1).fill(0);
    const zeroInDegreeSet = [];
    const newOrder = [];

    // [1] direction array, in degree array 생성
    for (let i = 0; i <= teamCount; i++) {
      for (let j = i + 1; j <= teamCount; j++) {
        directionArray[previousOrder[i]].push(previousOrder[j]);
        inDegreeArray[previousOrder[j]] += 1;
      }
    }

    // [2] changed direction array을 기준으로 direction array 수정
    for (let i = 0; i < changedDirectionArray.length; i++) {
      const [one, two] = changedDirectionArray[i];

      const oneIsWinnerIndex = directionArray[two].indexOf(one);
      const twoIsWinnerIndex = directionArray[one].indexOf(two);

      if (oneIsWinnerIndex !== -1) {
        directionArray[two].splice(oneIsWinnerIndex, 1);
        inDegreeArray[one] -= 1;
        directionArray[one].push(two);
        inDegreeArray[two] += 1;
      } else if (twoIsWinnerIndex !== -1) {
        directionArray[one].splice(twoIsWinnerIndex, 1);
        inDegreeArray[two] -= 1;
        directionArray[two].push(one);
        inDegreeArray[one] += 1;
      }
    }

    // [3] zeroInDegreeSet 초기화
    for (let i = 1; i <= teamCount; i++) {
      if (inDegreeArray[i] === 0) {
        zeroInDegreeSet.push(i);
      }
    }

    while (zeroInDegreeSet.length === 1) {
      // [4] zeroInDegreeSet에서 winner를 pop한 뒤 연결된 loser를 찾아서 indegree 감소, winner를 결과에 추가
      const winner = zeroInDegreeSet.pop();
      directionArray[winner].forEach((loser) => {
        inDegreeArray[loser] -= 1;
        if (inDegreeArray[loser] === 0) {
          zeroInDegreeSet.push(loser);
        }
      });
      newOrder.push(winner);
    }

    // [6] 결과 반환
    if (newOrder.length !== previousOrder.length) {
      ans = ans.concat("IMPOSSIBLE", "\n");
    } else {
      ans = ans.concat(newOrder.join(" "), "\n");
    }
  }
  return ans.trimEnd();
}
