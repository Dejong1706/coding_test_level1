def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arrList = []
        hap = 0
        for j in range(len(arr1[0])):
            hap = arr1[i][j] + arr2[i][j]
            arrList.append(hap)
        answer.append(arrList)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))


