def solution(answers):
    first_pattern = [1, 2, 3, 4, 5]
    second_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    res_1, res_2, res_3 = 0, 0, 0

    for i in range(len(answers)):
        if (first_pattern[i % len(first_pattern)] == answers[i]):
            res_1 += 1

        if (second_pattern[i % len(second_pattern)] == answers[i]):
            res_2 += 1

        if (third_pattern[i % len(third_pattern)] == answers[i]):
            res_3 += 1

    high_score = max(res_1, res_2, res_3)

    if (res_1 == high_score):
        answer.append(1)

    if (res_2 == high_score):
        answer.append(2)

    if (res_3 == high_score):
        answer.append(3)

    return answer

print(solution([1,3,2,4,2]))
