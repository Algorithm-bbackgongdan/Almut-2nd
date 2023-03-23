import sys

def calc_bluerays_number(length):
  count = 1
  curr_blueray_length = 0
  for video in videos:
    if curr_blueray_length + video > length:
      curr_blueray_length = 0
      count += 1
    curr_blueray_length += video
  return count

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
videos = list(map(int, sys.stdin.readline().rstrip().split(' ')))

left = max(videos)
right = sum(videos)

while left <= right:
  mid = (left + right) // 2
  bluerays_number = calc_bluerays_number(mid)
  if bluerays_number <= M:
    right = mid - 1
  else:
    left = mid + 1

print(left)