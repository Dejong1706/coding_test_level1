# arr1, arr2는 각 줄에 이진법으로 값을 받음
# 이진법으로만 푼다음 각 줄마다 벽을검사하여 출력하면 될듯
# 2진법 변환방법 print(bin(숫자))

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        string = ""
        a = int(format(arr1[i], 'b'))
        b = int(format(arr2[i], 'b'))
        hap = str(a+b)
        while(len(hap) < n):
            hap = "0" + hap[0:]
        print(hap)
        for j in hap:
            if int(j) == 0:
                string += " "
            else:
                string += "#"
        answer.append(string)
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))