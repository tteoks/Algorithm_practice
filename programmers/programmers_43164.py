from collections import deque


def solution(begin, target, words):
    answer = 0

    if begin not in words:
        words.insert(0, begin)

    if target not in words:
        return answer

    n = len(words)
    maps = [[False] * n for _ in range(n)]

    def check_word(a, b):
        tmp = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                if tmp == 1:
                    return False
                else:
                    tmp += 1
        return True if tmp == 1 else False

    def bfs(start, end):
        result = 0
        queue = deque([(start, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[start][start] = True

        while queue:
            i, d = queue.popleft()
            if i == end:
                return d

            for j, map in enumerate(maps[i]):
                if map:
                    visited[i][j] = True
                    queue.append((j, d + 1))
        return result

    for i in range(n):
        for j in range(i + 1, n):
            if check_word(words[i], words[j]):
                maps[i][j] = True
                maps[j][i] = True

    answer = bfs(words.index(begin), words.index(target))
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
