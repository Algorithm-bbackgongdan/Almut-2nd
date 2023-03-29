/////////////////////////////////
// Reading file from local env //
/////////////////////////////////

// let input = [];
// const fs = require("fs");

// fs.readFile("code/asiloveyu/week4/backjoon-11779.txt", "utf-8", (_, data) => {
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
  const [[cityCount], [busCount], ...routes] = input;
  const [start, end] = routes.pop();
  const minDist = new Array(cityCount + 1).fill(Number.MAX_VALUE);
  const busRoute = new Array(cityCount + 1).fill(0).map((_) => []);
  const nearest = new Array(cityCount + 1).fill(start);

  // [1] 버스 경로를 출발 도시 별로 정리합니다
  routes.forEach((route) => {
    const [start, end, dist] = route;
    busRoute[start].push([end, dist]);
  });

  // [2] Heap 객체를 생성합니다
  const heap = new MinHeap();
  heap.insert([start, 0]);

  while (heap.getLength() !== 0) {
    const [currentCity, currentDist] = heap.remove();

    // [3] currentCity까지 거리가 최소 거리보다 크면 건너뜁니다
    if (currentDist > minDist[currentCity]) continue;

    // [4] currentCity까지 이어진 각 버스 루트에 대해 새로운 경로를 궇바니다
    busRoute[currentCity].forEach((route) => {
      const [busEnd, busDist] = route;
      const newDistance = currentDist + busDist;

      // [5] 새로운 경로가 더 짧은 경우, 경로를 업데이트 합니다
      if (minDist[busEnd] > newDistance) {
        minDist[busEnd] = newDistance;
        nearest[busEnd] = currentCity;
        heap.insert([busEnd, newDistance]);
      }
    });
  }

  // [6] Nearest 배열에 대해 지나온 경로를 역추적 합니다
  let currentCity = end;
  let path = [];
  while (currentCity !== start) {
    path.push(currentCity);
    currentCity = nearest[currentCity];
  }
  path.push(start);
  path.reverse();

  const ans = `${minDist[end]}\n${path.length}\n${path.join(" ")}`;
  return ans;
}

///////////////////
// Heap Function //
///////////////////

class MinHeap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex(parentIndex) {
    return 2 * parentIndex + 1;
  }

  getRightChildIndex(parentIndex) {
    return 2 * parentIndex + 2;
  }

  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }

  getLength() {
    return this.heap.length;
  }

  hasLeftChild(index) {
    return this.getLeftChildIndex(index) < this.heap.length;
  }

  hasRightChild(index) {
    return this.getRightChildIndex(index) < this.heap.length;
  }

  hasParent(index) {
    return this.getParentIndex(index) >= 0;
  }

  leftChild(index) {
    return this.heap[this.getLeftChildIndex(index)];
  }

  rightChild(index) {
    return this.heap[this.getRightChildIndex(index)];
  }

  parent(index) {
    return this.heap[this.getParentIndex(index)];
  }

  swap(index1, index2) {
    const temp = this.heap[index1];
    this.heap[index1] = this.heap[index2];
    this.heap[index2] = temp;
  }

  peek() {
    if (this.heap.length === 0) {
      throw new Error("empty heap");
    }
    return this.heap[0];
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  remove() {
    if (this.heap.length === 0) {
      throw new Error("empty heap");
    } else if (this.heap.length === 1) {
      return this.heap.pop();
    } else {
      const min = this.heap[0];
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
      return min;
    }
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (
      this.hasParent(index) &&
      this.parent(index)[1] > this.heap[index][1]
    ) {
      this.swap(this.getParentIndex(index), index);
      index = this.getParentIndex(index);
    }
  }

  heapifyDown() {
    let index = 0;
    while (this.hasLeftChild(index)) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      if (
        this.hasRightChild(index) &&
        this.rightChild(index)[1] < this.leftChild(index)[1]
      ) {
        smallerChildIndex = this.getRightChildIndex(index);
      }

      if (this.heap[index][1] < this.heap[smallerChildIndex][1]) {
        break;
      } else {
        this.swap(index, smallerChildIndex);
      }

      index = smallerChildIndex;
    }
  }
}
