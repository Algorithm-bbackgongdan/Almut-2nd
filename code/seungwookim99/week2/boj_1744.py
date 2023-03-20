import sys

N = int(sys.stdin.readline().rstrip())
ones = []
zeroExists = False
negatives = []
positives = []  # 2이상의 양수
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        zeroExists = True  # 0 존재 참
    elif num == 1:
        ones.append(num)
    elif num < 0:
        negatives.append(num)
    else:
        positives.append(num)

positives.sort(reverse=True)
negatives.sort()

answer = 0

for i in range(1, len(negatives), 2): # 절대값이 큰 두 수 순서대로 묶어주기
    answer += negatives[i] * negatives[i - 1]

# 음수 개수가 홀수고 0이 없다면 -> 가장 작은 음수를 더함
if (len(negatives) % 2 == 1) and not zeroExists:
    answer += negatives[-1]

for i in range(1, len(positives), 2): # 절대값이 큰 두 수 순서대로 묶어주기
    answer += positives[i] * positives[i - 1]

if len(positives) % 2 == 1:
    answer += positives[-1]
answer += sum(ones)
print(answer)