# 2212 - 센서
import sys

N = int(input())
K = int(input())
sensors = list(map(int, sys.stdin.readline().split()))

# 정렬
sensors.sort()

# K가 개수보다 같거나 많은 경우 결과 0
if K >= len(sensors):
    print(0)
    sys.exit()

# 각 센서 사이 거리 계산
distance = []
for idx, sensor in enumerate(sensors):
    if idx != 0:
        x = sensor - sensors[idx-1]
        distance.append(x)

# 오름차순 정렬
distance.sort(reverse=True)
# 연결하지 않을 거리에 
ans = distance[K-1:]
print(sum(ans))
