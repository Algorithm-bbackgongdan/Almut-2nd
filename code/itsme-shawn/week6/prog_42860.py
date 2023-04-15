def solution(name):
    answer = 0

    # 한 알파벳 바꿀 때 누르는 조이스틱 최소 횟수
    def get_change_char(ch):
        if ord(ch) <= ord("N"):
            return ord(ch) - ord("A")
        else:
            return ord("Z") - ord(ch) + 1

    # 가장 긴 연속된 A 그룹을 찾는다.
    start, end = 0, 0
    flag = 0
    longest_A = [False, False]

    for i in range(len(name)):
        # 'A' 를 처음 발견하면 flag 처리하고 start 인덱스 저장
        if not flag and name[i] == "A":
            flag = 1
            start = i

        # flag 가 설정된 상태에서 'A' 가 아닌 것을 발견하면 end 값에 i-1 저장
        if flag and name[i] != "A":
            end = i - 1
            flag = 0

            # 가장 긴 A 묶음 갱신
            if longest_A[1] - longest_A[0] <= end - start:
                longest_A = [start, end]

        # flag 가 설정된 상태에서 끝까지 도달했다면 마지막 문자도 A 였다는 의미
        if flag and i == len(name) - 1:
            end = i  # 예외처리
            flag = 0

            if longest_A[1] - longest_A[0] <= end - start:
                longest_A = [start, end]

    # print(longest_A)

    for ch in name:
        if ch != "A":
            answer += get_change_char(ch)

    default = len(name) - 1  # 기본 (그냥 직진)

    # 'A' 가 없는 경우는 default 가 답이 됨
    if longest_A == [False, False]:
        answer += default
    # 모든 문자가 'A' 인 경우는 답이 0 이 됨
    elif longest_A == [0, len(name) - 1]:
        answer = 0

    # 그 외 나머지 경우
    else:
        # 가장 긴 A 의 시작인덱스가 0 인 경우는 0 으로 예외처리
        left = longest_A[0] - 1 if longest_A[0] > 0 else 0
        right = (len(name) - 1) - longest_A[1]

        left_twice = left * 2 + right
        right_twice = left + right * 2

        # default(그냥 직진), left_twice(왼쪽 두 번, 오른쪽 한 번), right_twice(d왼쪽 한 번, 오른쪽 두 번)
        left_right_move = min(default, left_twice, right_twice)

        answer += left_right_move

    return answer
