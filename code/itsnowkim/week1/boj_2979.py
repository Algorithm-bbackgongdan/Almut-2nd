# 2979 트럭 주차
import sys

a, b, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
maximum = max(arr[0][1], arr[1][1], arr[2][1])
parking = [0 for _ in range(maximum+1)]

# 순서대로 parking 자료구조에 체크
for i in range(3):
    for idx in range(arr[i][0],arr[i][1]):
        parking[idx] += 1

res = 0

for i in parking:
    if i == 1:
        res += a
    elif i == 2:
        res += b*2
    elif i == 3:
        res += c*3

print(res)