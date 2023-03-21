# 기타 레슨
import sys

N, M = map(int, sys.stdin.readline().split(' '))
# 강의 순서대로 arr 구성 - 섞이면 안 된다.
arr = list(map(int, sys.stdin.readline().split(' ')))

start = max(arr)
end = sum(arr)
answer = end
while (start <= end):
    count = 1
    temp = 0
    mid = (start + end) // 2
    
    # arr 순차적으로 돌면서 mid값보다 적도록 담기
    for item in arr:
        # 비디오에 담기
        if temp + item <= mid:
            temp += item
        else: # 못 담을 경우 다음 새 비디오에 담기
            count += 1
            temp = item
            if count > M:
                break

    # print(f'count : {count} mid : {mid}')
    # M보다 비디오의 개수가 많아질 경우 - mid값을 올려줘라
    if count > M:
        start = mid + 1
    # M보다 비디오의 개수가 적을 경우 - mid값을 내려라
    else:
        end = mid - 1
        answer = min(answer, mid)

print(answer)