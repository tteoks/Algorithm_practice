from collections import deque


def solution(n, computers):
    answer = 0

    def bfs(start):
        visited = set([start])
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for idx, neighbor in enumerate(computers[node]):
                if neighbor == 1 and idx not in visited:
                    visited.add(idx)
                    queue.append(idx)
        return result

    def check_num_unique(candidates):
        result = 0
        seen = set()

        for c in candidates:
            tmp = tuple(sorted(c))

            if tmp not in seen:
                result += 1
                seen.add(tmp)

        return result

    tmp_res = []
    for i in range(n):
        tmp_res.append(bfs(i))

    answer = check_num_unique(tmp_res)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
