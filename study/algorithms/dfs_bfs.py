"""
================================================================================
                         DFS (깊이 우선 탐색) & BFS (너비 우선 탐색)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------

[DFS (Depth-First Search) - 깊이 우선 탐색]
- 한 방향으로 끝까지 탐색한 후, 막히면 되돌아와서 다른 방향 탐색
- 스택 또는 재귀로 구현
- "깊이" 있게 파고드는 탐색

[BFS (Breadth-First Search) - 너비 우선 탐색]
- 현재 위치에서 가까운 노드부터 탐색
- 큐로 구현
- "넓게" 퍼져나가는 탐색
- 최단 거리 문제에 적합!

언제 사용하나?
- DFS: 경로 존재 여부, 모든 경로 탐색, 사이클 검출, 백트래킹
- BFS: 최단 거리, 최소 횟수, 레벨별 탐색


2. 동작 원리
--------------------------------------------------------------------------------

그래프 예시:
        1
       / \
      2   3
     / \   \
    4   5   6

[DFS 탐색 순서] - 1 → 2 → 4 → 5 → 3 → 6
    깊이 우선: 한 방향으로 끝까지 간 후 돌아옴

    1에서 시작
    → 2로 이동 (1의 자식)
    → 4로 이동 (2의 자식) - 막다른 길!
    → 2로 돌아옴
    → 5로 이동 (2의 다른 자식) - 막다른 길!
    → 2로 돌아옴 → 1로 돌아옴
    → 3으로 이동 (1의 다른 자식)
    → 6으로 이동 - 끝!

[BFS 탐색 순서] - 1 → 2 → 3 → 4 → 5 → 6
    너비 우선: 가까운 노드부터 탐색

    레벨 0: 1
    레벨 1: 2, 3  (1에서 거리 1)
    레벨 2: 4, 5, 6  (1에서 거리 2)


스택 vs 큐 동작:

[DFS - 스택 사용]
    push(1) → 스택: [1]
    pop() → 1 방문, push(3), push(2) → 스택: [3, 2]
    pop() → 2 방문, push(5), push(4) → 스택: [3, 5, 4]
    pop() → 4 방문 → 스택: [3, 5]
    pop() → 5 방문 → 스택: [3]
    pop() → 3 방문, push(6) → 스택: [6]
    pop() → 6 방문 → 스택: []

[BFS - 큐 사용]
    enqueue(1) → 큐: [1]
    dequeue() → 1 방문, enqueue(2), enqueue(3) → 큐: [2, 3]
    dequeue() → 2 방문, enqueue(4), enqueue(5) → 큐: [3, 4, 5]
    dequeue() → 3 방문, enqueue(6) → 큐: [4, 5, 6]
    dequeue() → 4 방문 → 큐: [5, 6]
    dequeue() → 5 방문 → 큐: [6]
    dequeue() → 6 방문 → 큐: []


3. 시간복잡도
--------------------------------------------------------------------------------
| 알고리즘 | 시간복잡도     | 공간복잡도   |
|---------|---------------|-------------|
| DFS     | O(V + E)      | O(V)        |
| BFS     | O(V + E)      | O(V)        |

* V: 정점(노드) 수, E: 간선 수


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

from collections import deque

# ================================
# 그래프 표현 방법
# ================================

# 방법 1: 인접 리스트 (가장 많이 사용)
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

# 방법 2: 입력 받아서 그래프 만들기
def build_graph(n: int, edges: list) -> dict:
    """
    n: 노드 수
    edges: [[u, v], ...] 간선 리스트
    """
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 무방향 그래프
    return graph


# ================================
# DFS 템플릿
# ================================

# DFS - 재귀 버전 (가장 직관적)
def dfs_recursive(graph: dict, start: int, visited: set = None) -> list:
    """
    재귀를 이용한 DFS
    """
    if visited is None:
        visited = set()

    result = []
    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# DFS - 스택 버전
def dfs_stack(graph: dict, start: int) -> list:
    """
    스택을 이용한 DFS
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # 역순으로 넣어야 작은 번호부터 방문
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# ================================
# BFS 템플릿
# ================================

def bfs(graph: dict, start: int) -> list:
    """
    큐를 이용한 BFS
    """
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# ================================
# 2D 그리드 탐색 템플릿 (중요!)
# ================================

# 4방향 이동 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 8방향 이동 (대각선 포함)
dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs_grid(grid: list, start: tuple) -> int:
    """
    2D 그리드에서 BFS - 최단 거리 찾기
    """
    n, m = len(grid), len(grid[0])
    sx, sy = start

    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    queue = deque([(sx, sy, 0)])  # (x, y, 거리)

    while queue:
        x, y, dist = queue.popleft()

        # 목적지 도착 체크 (필요시)
        # if grid[x][y] == 'E':
        #     return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 체크 & 방문 체크 & 이동 가능 체크
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가


"""
================================================================================
5. 대표 문제: 미로 탈출 (최단 거리)
================================================================================

[문제]
N x M 크기의 미로가 있습니다.
- 1: 이동 가능한 칸
- 0: 벽 (이동 불가)

(1, 1)에서 출발하여 (N, M)까지 가는 최소 칸 수를 구하세요.
시작 칸과 도착 칸도 포함하여 카운트합니다.

[예시]
미로:
    1 0 1 1 1
    1 0 1 0 1
    1 0 1 0 1
    1 1 1 0 1
    0 0 0 0 1

(1,1) → (5,5) 최단 거리: 9


6. 문제 해설
--------------------------------------------------------------------------------
왜 BFS를 쓰나?
    - BFS는 가까운 곳부터 탐색하므로 "최단 거리"를 보장
    - DFS는 최단 거리를 보장하지 않음!

BFS가 최단 거리를 보장하는 이유:
    - 거리 1인 모든 노드를 먼저 방문
    - 그 다음 거리 2인 모든 노드를 방문
    - ...
    - 처음 도착하면 그게 최단 거리!

동작 과정:

    미로 (1: 이동가능, 0: 벽):
    1 0 1 1 1
    1 0 1 0 1
    1 0 1 0 1
    1 1 1 0 1
    0 0 0 0 1

    거리 기록:
    1  .  9  10 11
    2  .  8  .  12
    3  .  7  .  13
    4  5  6  .  14
    .  .  .  .  15  ← 도착! 최단거리 = 9 (시작 포함이므로)

    실제로는... 문제에서 시작점도 포함하라고 했으니:
    답: 9


7. 코드 구현
--------------------------------------------------------------------------------
"""


def solve_maze(maze: list) -> int:
    """
    미로 최단 거리 - BFS

    Args:
        maze: 2D 리스트 (1: 이동가능, 0: 벽)

    Returns:
        최단 거리 (시작, 도착 포함), 불가능하면 -1
    """
    n = len(maze)
    m = len(maze[0])

    # 4방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 거리 저장 배열 (-1: 미방문)
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 1  # 시작점 거리 = 1 (문제 조건)

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능하고 미방문인 경우
                if maze[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance[n-1][m-1]


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def solve_maze_with_trace(maze: list) -> int:
    """동작 과정을 출력하면서 실행"""
    n = len(maze)
    m = len(maze[0])

    print("입력 미로:")
    for row in maze:
        print("  " + " ".join(map(str, row)))
    print()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dir_names = ['상', '하', '좌', '우']

    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 1

    queue = deque([(0, 0)])
    step = 0

    print("=" * 50)
    print("BFS 탐색 시작")
    print("=" * 50)

    while queue:
        step += 1
        x, y = queue.popleft()

        print(f"\n[Step {step}] 현재 위치: ({x}, {y}), 거리: {distance[x][y]}")
        print(f"  큐 상태: {list(queue)}")

        # 도착점 체크
        if x == n - 1 and y == m - 1:
            print(f"\n도착! 최단 거리: {distance[x][y]}")
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                    print(f"  → {dir_names[i]}({nx}, {ny}) 이동 가능, 거리 {distance[nx][ny]} 기록")
                elif maze[nx][ny] == 0:
                    print(f"  → {dir_names[i]}({nx}, {ny}) 벽!")
                elif distance[nx][ny] != -1:
                    print(f"  → {dir_names[i]}({nx}, {ny}) 이미 방문")
            else:
                print(f"  → {dir_names[i]} 범위 밖")

    print("\n거리 배열:")
    for row in distance:
        print("  " + " ".join(f"{d:2}" if d != -1 else " ." for d in row))

    return distance[n-1][m-1]


# ================================
# DFS vs BFS 비교 예시
# ================================

def compare_dfs_bfs():
    """DFS와 BFS 탐색 순서 비교"""
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: []
    }

    print("그래프:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
    print()

    print(f"DFS 탐색 순서: {dfs_recursive(graph, 1)}")
    print(f"BFS 탐색 순서: {bfs(graph, 1)}")


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("DFS/BFS 예제 실행")
    print("=" * 60)

    # DFS vs BFS 비교
    print("\n[DFS vs BFS 비교]")
    compare_dfs_bfs()

    # 미로 탈출 테스트
    print("\n" + "=" * 60)
    print("미로 탈출 (최단 거리)")
    print("=" * 60)

    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]

    # 빠른 테스트
    result = solve_maze(maze)
    print(f"\n최단 거리: {result}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)

    small_maze = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1]
    ]
    solve_maze_with_trace(small_maze)


"""
================================================================================
9. DFS/BFS 선택 가이드
================================================================================

[BFS 사용]
- "최단", "최소" 키워드가 있으면 BFS!
- 예: 최단 거리, 최소 이동 횟수

[DFS 사용]
- 모든 경로 탐색
- 경로 존재 여부만 확인
- 백트래킹 문제
- 사이클 검출

[둘 다 가능]
- 연결 요소 개수 세기
- 섬의 개수 세기


================================================================================
10. 연습 문제 추천
================================================================================

BFS (최단 거리):
- 백준 2178번: 미로 탐색
- 백준 7576번: 토마토
- 백준 1697번: 숨바꼭질
- 프로그래머스: 게임 맵 최단거리

DFS:
- 백준 1260번: DFS와 BFS
- 백준 2667번: 단지번호붙이기
- 백준 1012번: 유기농 배추

응용:
- 백준 2206번: 벽 부수고 이동하기
- 백준 7569번: 토마토 (3차원)
================================================================================
"""
