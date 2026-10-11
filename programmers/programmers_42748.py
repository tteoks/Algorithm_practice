def solution(array, commands):
    answer = []

    for command in commands:
        tmp = []
        start, end, num = command

        tmp = array[start - 1:end]
        tmp.sort()
        answer.append(tmp[num - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
