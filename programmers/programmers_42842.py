def solution(brown, yellow):
    answer = []
    yellow_candidates = []

    for idx in range(1, yellow + 1):
        if (yellow % idx == 0):
            y_x = int(yellow / idx)
            y_y = int(yellow / y_x)

            if (y_x < y_y):
                break
            yellow_candidates.append((y_x, y_y))

    for y_x, y_y in yellow_candidates:
        edge_required = y_x * 2 + y_y * 2 + 4
        if (edge_required == brown):
            answer.extend([y_x + 2, y_y + 2])
            break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
