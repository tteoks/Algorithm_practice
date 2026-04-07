"""
================================================================================
                    최단 경로 (Shortest Path) - 다익스트라 & 플로이드-워셜
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
그래프에서 두 노드 사이의 "가장 짧은 경로"를 찾는 알고리즘입니다.

종류:
- 다익스트라 (Dijkstra): 하나의 출발점 → 모든 노드까지 최단 거리
- 플로이드-워셜 (Floyd-Warshall): 모든 노드 쌍 사이의 최단 거리
- 벨만-포드 (Bellman-Ford): 음수 가중치 허용

핵심 차이:
- 다익스트라: 양수 가중치만, O(E log V), 출발점 1개
- 플로이드-워셜: 음수 가중치 가능, O(V³), 모든 쌍
- BFS: 가중치 없는 그래프 (가중치 모두 1)

언제 사용하나?
- 다익스트라: "A에서 B까지 최단 거리" (가중치 양수)
- 플로이드-워셜: "모든 쌍 최단 거리", 노드 수 적을 때 (V ≤ 500)
- BFS: 가중치 없는 그래프의 최단 거리


2. 동작 원리
--------------------------------------------------------------------------------

[다익스트라 알고리즘]

    그래프 (가중치 있는 방향 그래프):

    1 --2-- 2 --3-- 4
    |       |       |
    5       1       6
    |       |       |
    3 --1-- 5 ------+

    출발: 1번 노드

    1. 초기 거리: [0, ∞, ∞, ∞, ∞]
                   1  2  3  4  5

    2. 현재 노드: 1 (거리 0)
       → 2: 0+2=2 (갱신)
       → 3: 0+5=5 (갱신)
       거리: [0, 2, 5, ∞, ∞]

    3. 현재 노드: 2 (거리 2, 가장 가까운 미방문)
       → 4: 2+3=5 (갱신)
       → 5: 2+1=3 (갱신)
       거리: [0, 2, 5, 5, 3]

    4. 현재 노드: 5 (거리 3)
       → 3: 3+1=4 < 5 (갱신!)
       → 4: 3+6=9 > 5 (유지)
       거리: [0, 2, 4, 5, 3]

    5. 현재 노드: 3 (거리 4) → 갱신 없음
    6. 현재 노드: 4 (거리 5) → 갱신 없음

    최종: [0, 2, 4, 5, 3]

    핵심: "현재까지 가장 가까운 노드부터 확정" (그리디 + 힙)


[플로이드-워셜 알고리즘]

    핵심 아이디어:
    "i에서 j로 갈 때, k를 거쳐가는 게 더 빠르면 갱신"

    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    3중 반복: k(경유지) → i(출발) → j(도착)

    예시 (3개 노드):

    초기:        k=1 거쳐:    k=2 거쳐:    k=3 거쳐:
    0  2  ∞      0  2  ∞      0  2  5      0  2  5
    ∞  0  3   →  ∞  0  3   →  ∞  0  3   →  ∞  0  3
    7  ∞  0      7  9  0      7  9  0      7  9  0

    dist[1][3] = min(∞, dist[1][2]+dist[2][3]) = min(∞, 2+3) = 5
    dist[3][2] = min(∞, dist[3][1]+dist[1][2]) = min(∞, 7+2) = 9


3. 시간복잡도
--------------------------------------------------------------------------------
| 알고리즘       | 시간복잡도     | 공간복잡도   | 특징              |
|---------------|---------------|-------------|------------------|
| 다익스트라     | O(E log V)    | O(V + E)    | 힙 사용           |
| 플로이드-워셜  | O(V³)         | O(V²)       | 모든 쌍           |
| 벨만-포드      | O(V × E)      | O(V)        | 음수 가중치 가능   |

* V: 정점 수, E: 간선 수


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

import heapq
from math import inf


# ================================
# 다익스트라 (Dijkstra)
# ================================

def dijkstra(graph: dict, start: int) -> dict:
    """
    다익스트라 - 한 점에서 모든 점까지 최단 거리

    Args:
        graph: {노드: [(비용, 이웃노드), ...]}
        start: 출발 노드

    Returns:
        {노드: 최단 거리}
    """
    dist = {node: inf for node in graph}
    dist[start] = 0
    heap = [(0, start)]  # (거리, 노드)

    while heap:
        cost, u = heapq.heappop(heap)

        # 이미 처리된 거리보다 크면 스킵 (중요!)
        if cost > dist[u]:
            continue

        for weight, v in graph[u]:
            new_cost = cost + weight
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))

    return dist


# 다익스트라 - 인접 리스트 (백준 스타일 입력)
def dijkstra_array(n: int, graph: list, start: int) -> list:
    """
    배열 기반 다익스트라

    Args:
        n: 노드 수
        graph: graph[u] = [(비용, v), ...]
        start: 출발 노드 (1-indexed)

    Returns:
        dist[i] = start에서 i까지 최단 거리
    """
    dist = [inf] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost > dist[u]:
            continue

        for weight, v in graph[u]:
            new_cost = cost + weight
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))

    return dist


# 다익스트라 - 경로 추적
def dijkstra_with_path(graph: dict, start: int, end: int) -> tuple:
    """
    최단 거리 + 경로 반환

    Returns:
        (최단 거리, 경로 리스트)
    """
    dist = {node: inf for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost > dist[u]:
            continue

        if u == end:
            break

        for weight, v in graph[u]:
            new_cost = cost + weight
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(heap, (new_cost, v))

    # 경로 복원
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[end], path


# ================================
# 플로이드-워셜 (Floyd-Warshall)
# ================================

def floyd_warshall(n: int, edges: list) -> list:
    """
    모든 쌍 최단 거리

    Args:
        n: 노드 수
        edges: [(u, v, weight), ...]

    Returns:
        dist[i][j] = i에서 j까지 최단 거리
    """
    # 초기화
    dist = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0

    # 간선 정보 입력
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # 중복 간선 처리
        # dist[v][u] = min(dist[v][u], w)  # 무방향이면 추가

    # 3중 반복: k(경유) → i(출발) → j(도착)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


"""
================================================================================
5. 대표 문제: 최단경로 (백준 1753)
================================================================================

[문제]
방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의
최단 경로를 구하시오.

[입력]
첫째 줄: 정점 수 V, 간선 수 E
둘째 줄: 시작 정점 K
셋째 줄부터: u v w (u→v, 가중치 w)

[예시]
Input:
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

Output:
0
2
3
7
INF


6. 문제 해설
--------------------------------------------------------------------------------
왜 다익스트라를 쓰나?
    - 한 점에서 모든 점까지 최단 거리 → 다익스트라
    - 가중치가 양수 → 다익스트라 사용 가능
    - 정점 수가 많을 수 있음 → 힙 기반 다익스트라

알고리즘:
    1. 출발점 거리 = 0, 나머지 = ∞
    2. 힙에서 가장 가까운 노드 꺼냄
    3. 이웃 노드들의 거리 갱신
    4. 갱신되면 힙에 추가
    5. 반복

동작 과정 (시작: 1):
    초기: dist = [_, 0, ∞, ∞, ∞, ∞]  (1-indexed)
    힙: [(0, 1)]

    [Pop (0, 1)]
    → 노드 2: 0+2=2 < ∞ → 갱신, 힙에 추가
    → 노드 3: 0+3=3 < ∞ → 갱신, 힙에 추가
    dist: [_, 0, 2, 3, ∞, ∞]

    [Pop (2, 2)]
    → 노드 3: 2+4=6 > 3 → 유지
    → 노드 4: 2+5=7 < ∞ → 갱신
    dist: [_, 0, 2, 3, 7, ∞]

    [Pop (3, 3)]
    → 노드 4: 3+6=9 > 7 → 유지
    dist: [_, 0, 2, 3, 7, ∞]

    [Pop (7, 4)] → 갱신 없음
    힙 비어있음 → 종료

    최종: [_, 0, 2, 3, 7, INF]


7. 코드 구현
--------------------------------------------------------------------------------
"""


def solve_shortest_path():
    """백준 1753 - 최단경로"""
    import sys
    input = sys.stdin.readline

    V, E = map(int, input().split())
    K = int(input())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    dist = dijkstra_array(V, graph, K)

    for i in range(1, V + 1):
        print(dist[i] if dist[i] != inf else "INF")


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def dijkstra_with_trace(graph: dict, start: int) -> dict:
    """동작 과정을 출력하면서 실행"""
    dist = {node: inf for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    print(f"출발점: {start}")
    print(f"초기 거리: {dist}")
    print("=" * 60)

    step = 0
    while heap:
        cost, u = heapq.heappop(heap)

        if cost > dist[u]:
            print(f"\n  (스킵) 노드 {u}: 현재 비용 {cost} > 확정 거리 {dist[u]}")
            continue

        step += 1
        print(f"\n[Step {step}] 노드 {u} 확정 (거리: {cost})")
        print(f"  힙 상태: {heap}")

        for weight, v in graph[u]:
            new_cost = cost + weight
            if new_cost < dist[v]:
                old = dist[v]
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
                print(f"  → 노드 {v}: {old} → {new_cost} (갱신!)")
            else:
                print(f"  → 노드 {v}: {dist[v]} ≤ {new_cost} (유지)")

    print(f"\n최종 거리: {dist}")
    return dist


def floyd_warshall_with_trace(n: int, edges: list) -> list:
    """동작 과정을 출력하면서 실행"""
    dist = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    def print_matrix(dist, n):
        for i in range(1, n + 1):
            row = []
            for j in range(1, n + 1):
                row.append(f"{dist[i][j]:3}" if dist[i][j] != inf else "  ∞")
            print(f"  {row}")

    print("초기 거리 행렬:")
    print_matrix(dist, n)

    for k in range(1, n + 1):
        updated = False
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    old = dist[i][j]
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if not updated:
                        print(f"\n경유지 k={k}:")
                        updated = True
                    print(f"  dist[{i}][{j}]: {old if old != inf else '∞'} → {dist[i][j]}")

        if updated:
            print_matrix(dist, n)
        else:
            print(f"\n경유지 k={k}: 갱신 없음")

    return dist


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("최단 경로 예제 실행")
    print("=" * 60)

    # 다익스트라 테스트
    print("\n[다익스트라]")
    graph = {
        1: [(2, 2), (5, 3)],
        2: [(2, 1), (3, 4), (1, 5)],
        3: [(5, 1), (1, 5)],
        4: [(3, 2), (6, 3)],
        5: [(1, 2), (1, 3), (6, 4)]
    }

    dist = dijkstra(graph, 1)
    print(f"1번에서 각 노드까지: {dist}")

    # 경로 추적
    cost, path = dijkstra_with_path(graph, 1, 4)
    print(f"1 → 4 최단 거리: {cost}, 경로: {' → '.join(map(str, path))}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("다익스트라 동작 과정 추적")
    print("=" * 60)
    dijkstra_with_trace(graph, 1)

    # 플로이드-워셜 테스트
    print("\n" + "=" * 60)
    print("플로이드-워셜")
    print("=" * 60)

    edges = [
        (1, 2, 2),
        (2, 3, 3),
        (3, 1, 7),
    ]

    print("\n[동작 과정]")
    floyd_warshall_with_trace(3, edges)


"""
================================================================================
9. 최단 경로 선택 가이드
================================================================================

[다익스트라 사용]
- "A에서 B까지 최단 거리" (출발점 1개)
- 가중치가 모두 양수
- 노드/간선이 많을 때 (V ≤ 100,000)
- 예: 네비게이션, 네트워크 라우팅

[플로이드-워셜 사용]
- "모든 쌍의 최단 거리"
- 노드 수가 적을 때 (V ≤ 500)
- 음수 가중치 가능 (음수 사이클은 불가)
- 예: 모든 도시 간 최단 거리

[BFS 사용]
- 가중치가 없거나 모두 동일
- 예: 미로 최단 거리, 최소 이동 횟수

[벨만-포드 사용]
- 음수 가중치가 있을 때
- 음수 사이클 판별


================================================================================
10. 연습 문제 추천
================================================================================

다익스트라:
- 백준 1753번: 최단경로 (기본)
- 백준 1916번: 최소비용 구하기
- 백준 1238번: 파티 (왕복 최단 거리)
- 백준 4485번: 녹색 옷 입은 애가 젤다지?

플로이드-워셜:
- 백준 11404번: 플로이드 (기본)
- 백준 11403번: 경로 찾기
- 백준 1389번: 케빈 베이컨의 6단계 법칙

응용:
- 백준 1504번: 특정한 최단 경로 (경유지 다익스트라)
- 백준 9370번: 미확인 도착지
- 백준 5719번: 거의 최단 경로
================================================================================
"""
