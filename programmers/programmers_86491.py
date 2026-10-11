def solution(sizes):
    sorted_sizes = list(map(sorted, sizes))
    max_x, max_y = 0, 0
    answer = 0

    for i in sorted_sizes:
        if i[0] > max_x:
            max_x = i[0]

        if i[1] > max_y:
            max_y = i[1]

    answer = max_x * max_y

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
