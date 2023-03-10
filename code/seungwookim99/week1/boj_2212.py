import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensors = set(map(int, sys.stdin.readline().rstrip().split()))  # 중복 제거
sensors = sorted(list(sensors))
totalRange = sensors[-1] - sensors[0]
distances = []
for i in range(1, len(sensors)):
    distances.append(sensors[i] - sensors[i - 1])
distances = sorted(distances, reverse=True)
kRange = min(K - 1, len(distances))
for k in range(kRange):
    totalRange -= distances[k]
print(totalRange)