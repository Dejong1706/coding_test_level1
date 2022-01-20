def solution(id_list, report, k):
    answer = []
    dict = {} # 경고 받은 횟수 누적 딕셔너리
    dict2 = {} # 신고에 성공한 횟수 누적 딕셔너리
    for j in id_list:
        dict[j] = 0
        dict2[j] = 0
    for i in report:
        answer.append(i.split())
    for i in range(len(answer)):
        answer[i] = tuple(answer[i])
    answer = tuple(answer)
    answer = list(set(answer))
    for i in range(len(answer)):
        dict[answer[i][1]] += 1
    id_stop = []
    for i in dict:
        if dict.get(i) >= k:
            id_stop.append(i)
    for i in id_stop:
        for j in range(len(answer)):
            if i == answer[j][1]:
                dict2[answer[j][0]] += 1
    result = list(dict2.values())

    return result

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
