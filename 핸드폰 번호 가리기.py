def solution(phone_number):
    answer = phone_number[-4:]
    answer2 = ""
    for i in range(len(phone_number[:-4])):
        answer2 += "*"
    result = answer2 + answer
    return result
