def solution(n):
    answer = ''
    while n > 0:
        n, a = divmod(n, 3)
        answer += str(a)
    answer = int(answer, 3)

    return answer