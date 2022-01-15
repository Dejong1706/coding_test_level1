import math

def solution(n):
    cnt = 4
    if n < 11:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n <= 5:
            return 3
        elif n <= 10:
            return 4
    else:
        for i in range(11, n+1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % math.sqrt(n) != 0:
                cnt += 1
        return cnt

n = 13
print(solution(n))