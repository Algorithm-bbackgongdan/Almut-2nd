import sys

read = sys.stdin.readline

N, M = map(int, read().split())
lectures = list(map(int, read().split()))

start = max(lectures)
end = sum(lectures)
ans = 0


def get_amount(size):  # 주어진 크기(size)일 때의 블루레이 수를 구함
    total = 0
    cnt = 1
    for lecture in lectures:
        total += lecture
        if total > size:
            cnt += 1
            total = lecture
    return cnt


while start <= end:
    mid = (start + end) // 2
    amount = get_amount(mid)

    if amount <= M:  # 이미 가능. but 블루레이 하나의 크기를 최대한 줄여야 함
        ans = mid
        end = mid - 1
    else:  # 안 되는 경우(주어진 블루레이 개수보다 블루레이가 더 많이 필요한 상황)=> 블루레이 하나의 크기를 더 늘려야 함
        start = mid + 1

print(ans)
