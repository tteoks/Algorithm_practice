from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def can_change(a, b):
        diff = 0

        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False

        return True

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        word, depth = queue.popleft()

        if word == target:
            return depth

        for next_word in words:
            if next_word not in visited and can_change(word, next_word):
                visited.add(next_word)
                queue.append((next_word, depth + 1))

    return 0


def solution(maps):
    answer = -1

    n, m = len(maps), len(maps[0])
    sx, sy = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    queue = deque([(sx, sy, 1)])

    while queue:
        x, y, d = deque.popleft(queue)
        if x == n - 1 and y == m - 1:
            answer = d
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))

    return answer


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
