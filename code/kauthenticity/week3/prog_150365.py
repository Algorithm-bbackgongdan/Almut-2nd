DIRECTIONS = {"d": (1, 0), "r": (0, 1), "l": (0, -1), "u": (-1, 0)}


def canMove(curX, curY, n, m):
    if curX < 0 or curX >= n or curY < 0 or curY >= m:
        return False

    return True


def getDirection(cur, dest):
    curX, curY = cur
    destX, destY = dest

    diffX = destX - curX
    diffY = destY - curY

    if diffX <= 0 and diffY > 0:
        return "r"
    elif diffX < 0 and diffY == 0:
        return "u"
    elif (diffX < 0 and diffY < 0) or (diffX == 0 and diffY < 0):
        return "l"
    else:
        return "d"


def solution(n, m, x, y, r, c, k):
    answer = ""

    x -= 1
    y -= 1
    r -= 1
    c -= 1

    dist = abs(r - x) + abs(c - y)

    # 애초에 이동할 수 없는 경우
    if abs(dist - k) % 2 != 0 or dist > k:
        return "impossible"

    curX, curY = x, y
    toMove = k

    while True:
        if len(answer) == k:
            break

        dist = abs(r - curX) + abs(c - curY)

        # 맨해튼 거리보다 움직여야 할 거리가 큰 경우 (최적으로 움직이지 않아도 되는 경우)
        if dist < toMove:
            # 그리디하게 d, r, l, u 순으로 움직일 수 있는 곳 확인
            for direction in sorted(DIRECTIONS.keys()):
                tempX, tempY = curX, curY
                dirX, dirY = DIRECTIONS[direction]

                tempX += dirX
                tempY += dirY

                if canMove(tempX, tempY, n, m):
                    curX, curY = tempX, tempY
                    answer += direction
                    break
        # 최적으로 움직여야 하는 경우
        else:
            direction = getDirection(cur=(curX, curY), dest=(r, c))
            dirX, dirY = DIRECTIONS[direction]

            curX += dirX
            curY += dirY

            answer += direction

        toMove -= 1

    return answer
