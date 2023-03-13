"""메인아이디어
집중국의 수신가능 길이의 합을 최소로 하려면
센서~센서 사이가 긴 곳에는 배치하면 안 된다.

1. 센서 사이의 길이 조사
2. 센서 사이의 길이를 큰 순서로 정렬
3. (센서 개수 - 1) 개 를 제외시킴
"""


import sys

read = sys.stdin.readline

n = int(read())
k = int(read())

# 집중국개수 >= 센서개수 이면 집중국의 길이의 합은 0
if k >= n:
    print(0)
else:
    sensor = sorted(list(map(int, read().split())))

    distance = []

    for i in range(1, n):
        distance.append(sensor[i] - sensor[i - 1])

    distance.sort(reverse=True)
    print(sum(distance[k - 1 :]))
