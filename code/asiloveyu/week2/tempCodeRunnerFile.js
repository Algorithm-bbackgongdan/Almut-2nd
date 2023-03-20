let input = [];
const fs = require("fs");

fs.readFile("code/asiloveyu/week2/backjoon-1744.txt", "utf-8", (_, data) => {
  data
    .toString()
    .split("\n")
    .forEach((line) => {
      input.push(line.split(" ").map((v) => parseInt(v)));
    });
  console.log(solution(input));
});