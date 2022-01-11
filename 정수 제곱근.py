import math

def solution(n):
    answer = 0
    answer = math.sqrt(n)
    if answer % 1 == 0:
        answer += 1
        return int(answer**2)
    else:
        answer = -1
        return answer

n = 3
print(solution(n))