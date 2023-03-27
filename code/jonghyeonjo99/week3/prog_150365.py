def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''
    dist = abs(x-r) + abs(y-c)
    if(k < dist or (k + dist) % 2 == 1): return 'impossible'
    if (k == dist):
        if(x < r):
            for i in range(r-x):
                answer += 'd'
            if(y < c):
                for i in range(c-y):
                    answer += 'r'
            else:
                for i in range(y-c):
                    answer += 'l'
        else:
            if(y < c):
                for i in range(c-y):
                    answer += 'r'
                for j in range(x-r):
                    answer += 'u'
            else:
                for i in range(y-c):
                    answer += 'l'
                for j in range(x-r):
                    answer += 'u'
    if(k > dist):
        if(x < r):
            m = k - (r-x)
            n = dist - (r-x)
            s = m/n
            for i in range(r-x):
                answer += 'd'
            if(y < c):
                if(m % 2 == 1):
                    for i in range(s):
                        answer += 'rl'
                    for j in range(m - (2*s)):
                        answer += 'r'
                else:
                    for i in range(s-1):
                        answer += 'rl'
                    for j in range(m - 2*(s-1)):
                        answer += 'r'
            else:
                for i in range(n):
                    answer += 'l'
                for j in range((k-dist)//2):
                    answer += 'rl'
        else:
            if (y < c):
                for i in range (c-y):
                    answer += 'r'
                for j in range ((k-(c-y)-(x-r))//2):
                    answer += 'l'
                for i in range ((k-(c-y)-(x-r))//2):
                    answer += 'r'
                for j in range (x-r):
                    answer += 'u'
            else:
                for i in range(y-c):
                    answer += 'l'
                for i in range((k-(y-c)-(x-r))//2):
                    answer += 'rl'
                for i in range(x-r):
                    answer += 'u'       
    return answer