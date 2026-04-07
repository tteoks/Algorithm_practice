"""
================================================================================
                         유니온 파인드 (Union-Find) / 분리 집합 (Disjoint Set)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
유니온 파인드는 "여러 원소가 같은 그룹에 속하는지"를 빠르게 판별하는 자료구조입니다.
서로소 집합(Disjoint Set)이라고도 합니다.

두 가지 핵심 연산:
- Find: 원소가 속한 그룹(대표 원소)을 찾기
- Union: 두 그룹을 하나로 합치기

최적화 기법:
- 경로 압축 (Path Compression): Find 시 루트까지의 모든 노드를 루트에 직접 연결
- 랭크 기반 합치기 (Union by Rank): 작은 트리를 큰 트리에 붙이기

언제 사용하나?
- "같은 그룹인지?" 판별
- 그래프의 사이클 검출
- 크루스칼 MST (최소 신장 트리)
- 네트워크 연결 판별
- 집합 합치기/분리


2. 동작 원리
--------------------------------------------------------------------------------

[초기 상태] - 각자가 자신의 대표
    parent: [0, 1, 2, 3, 4, 5]
    노드:    0  1  2  3  4  5

    각 노드가 독립적인 집합:
    {0} {1} {2} {3} {4} {5}


[Union(1, 2)] - 1과 2를 합침
    parent: [0, 1, 1, 3, 4, 5]
                  ^
    1이 2의 부모가 됨
    {0} {1, 2} {3} {4} {5}


[Union(3, 4)] - 3과 4를 합침
    parent: [0, 1, 1, 3, 4, 5]
                      ^
    {0} {1, 2} {3, 4} {5}


[Union(1, 3)] - {1,2}와 {3,4}를 합침
    parent: [0, 1, 1, 1, 3, 5]
                      ^
    1
   / \
  2   3
      |
      4

    {0} {1, 2, 3, 4} {5}


[경로 압축 (Path Compression)]
    Find(4) 호출 시:
    4 → 3 → 1 (루트 찾음)
    이후 4를 직접 1에 연결!

    압축 전:     압축 후:
      1            1
     / \         / | \
    2   3       2  3  4
        |
        4


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산          | 최적화 없음  | 경로 압축 + 랭크  |
|--------------|------------|------------------|
| Find         | O(n)       | O(α(n)) ≈ O(1)  |
| Union        | O(n)       | O(α(n)) ≈ O(1)  |

* α(n): 아커만 함수의 역함수, 사실상 상수
* n이 10^80이어도 α(n) ≤ 4


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""


# ================================
# 기본 구현 (배열 기반)
# ================================

class UnionFind:
    def __init__(self, n: int):
        """n개의 원소로 초기화 (0 ~ n-1)"""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # 집합의 개수

    def find(self, x: int) -> int:
        """x의 루트(대표 원소)를 찾기 + 경로 압축"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축!
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """x와 y가 속한 집합을 합치기

        Returns:
            True: 합침 성공 (서로 다른 집합이었음)
            False: 이미 같은 집합
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # 이미 같은 집합

        # 랭크 기반 합치기 (작은 트리를 큰 트리에 붙임)
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """x와 y가 같은 집합인지"""
        return self.find(x) == self.find(y)

    def group_count(self) -> int:
        """현재 집합의 개수"""
        return self.count


# ================================
# 간단한 함수 버전 (코테에서 빠르게 쓸 때)
# ================================

def make_union_find(n: int) -> list:
    """parent 배열 생성"""
    return list(range(n))


def find(parent: list, x: int) -> int:
    """경로 압축 Find"""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list, x: int, y: int) -> bool:
    """Union (간단 버전)"""
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    parent[ry] = rx
    return True


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 사이클 검출
def has_cycle(n: int, edges: list) -> bool:
    """
    무방향 그래프에서 사이클이 있는지 판별

    간선을 추가할 때 이미 같은 집합이면 = 사이클!
    """
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True  # 이미 연결되어 있는데 또 연결 = 사이클
    return False


# 패턴 2: 연결 요소 개수
def count_components(n: int, edges: list) -> int:
    """그래프의 연결 요소(connected component) 수"""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.group_count()


# 패턴 3: 크루스칼 MST (최소 신장 트리)
def kruskal(n: int, edges: list) -> tuple:
    """
    크루스칼 알고리즘으로 MST 구하기

    Args:
        n: 노드 수
        edges: [(weight, u, v), ...]

    Returns:
        (MST 총 비용, MST 간선 리스트)
    """
    edges.sort()  # 가중치 기준 정렬
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):  # 사이클 아닌 경우만 추가
            mst_cost += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break  # MST 완성

    return mst_cost, mst_edges


"""
================================================================================
5. 대표 문제: 집합의 표현 (백준 1717)
================================================================================

[문제]
n+1개의 집합 {0}, {1}, ..., {n}이 있다.
- 0 a b: a가 포함된 집합과 b가 포함된 집합을 합침
- 1 a b: a와 b가 같은 집합에 포함되어 있는지 확인

[예시]
Input:
7 8
0 1 3
1 1 7     → NO
0 7 6
1 7 1     → NO
0 3 7
0 4 2
0 1 1
1 1 1     → YES

Output:
NO
NO
YES


6. 문제 해설
--------------------------------------------------------------------------------
왜 유니온 파인드를 쓰나?
    - "같은 집합인지?" 질의 → Find
    - "집합을 합쳐라" 명령 → Union
    - 연산이 최대 100,000번 → O(α(n)) ≈ O(1)이 필요

동작 과정:
    초기: {0} {1} {2} {3} {4} {5} {6} {7}

    0 1 3 → Union(1, 3)
    {0} {1, 3} {2} {4} {5} {6} {7}

    1 1 7 → Find(1) ≠ Find(7) → NO

    0 7 6 → Union(7, 6)
    {0} {1, 3} {2} {4} {5} {6, 7}

    1 7 1 → Find(7) ≠ Find(1) → NO

    0 3 7 → Union(3, 7) → {1, 3}과 {6, 7} 합침
    {0} {1, 3, 6, 7} {2} {4} {5}

    0 4 2 → Union(4, 2)
    {0} {1, 3, 6, 7} {2, 4} {5}

    0 1 1 → Union(1, 1) → 같은 집합, 변화 없음

    1 1 1 → Find(1) == Find(1) → YES


7. 코드 구현
--------------------------------------------------------------------------------
"""


def solve_disjoint_set():
    """백준 1717 - 집합의 표현"""
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    uf = UnionFind(n + 1)  # 0 ~ n

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            uf.union(a, b)
        else:
            print("YES" if uf.connected(a, b) else "NO")


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


class UnionFindWithTrace:
    """동작 과정을 출력하는 유니온 파인드"""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        path = [x]
        while self.parent[x] != x:
            x = self.parent[x]
            path.append(x)

        root = x
        # 경로 압축
        for node in path[:-1]:
            self.parent[node] = root

        if len(path) > 2:
            print(f"    경로 압축: {' → '.join(map(str, path))} "
                  f"→ 모두 {root}에 직접 연결")
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        print(f"  Find({x}) = {rx}, Find({y}) = {ry}")

        if rx == ry:
            print(f"  → 이미 같은 집합!")
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        print(f"  → {ry}를 {rx} 아래에 연결")
        print(f"  parent: {self.parent}")
        return True


def trace_example():
    """동작 과정 추적 예시"""
    uf = UnionFindWithTrace(8)

    operations = [
        ("union", 1, 3),
        ("find", 1, 7),
        ("union", 7, 6),
        ("find", 7, 1),
        ("union", 3, 7),
        ("union", 4, 2),
        ("find", 1, 1),
    ]

    print(f"초기 parent: {uf.parent}")
    print("=" * 50)

    for op, a, b in operations:
        if op == "union":
            print(f"\nUnion({a}, {b})")
            uf.union(a, b)
        else:
            print(f"\n같은 집합? ({a}, {b})")
            ra, rb = uf.find(a), uf.find(b)
            print(f"  → {'YES' if ra == rb else 'NO'}")


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("유니온 파인드 예제 실행")
    print("=" * 60)

    # 기본 사용
    print("\n[기본 사용]")
    uf = UnionFind(6)
    print(f"초기 집합 수: {uf.group_count()}")  # 6

    uf.union(0, 1)
    print(f"Union(0,1) → 집합 수: {uf.group_count()}")  # 5
    uf.union(2, 3)
    print(f"Union(2,3) → 집합 수: {uf.group_count()}")  # 4
    uf.union(0, 3)
    print(f"Union(0,3) → 집합 수: {uf.group_count()}")  # 3

    print(f"0과 3 연결? {uf.connected(0, 3)}")  # True
    print(f"0과 4 연결? {uf.connected(0, 4)}")  # False

    # 사이클 검출
    print("\n[사이클 검출]")
    edges1 = [(0, 1), (1, 2), (2, 3)]  # 사이클 없음
    edges2 = [(0, 1), (1, 2), (2, 0)]  # 사이클 있음
    print(f"[0-1, 1-2, 2-3] 사이클? {has_cycle(4, edges1)}")
    print(f"[0-1, 1-2, 2-0] 사이클? {has_cycle(3, edges2)}")

    # 크루스칼 MST
    print("\n[크루스칼 MST]")
    mst_edges = [
        (1, 0, 1), (2, 0, 2), (3, 1, 2),
        (4, 1, 3), (5, 2, 3)
    ]
    cost, mst = kruskal(4, mst_edges)
    print(f"MST 비용: {cost}")
    print(f"MST 간선: {mst}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    trace_example()


"""
================================================================================
9. 유니온 파인드 활용 팁
================================================================================

[경로 압축은 필수!]
- 없으면 O(n), 있으면 O(α(n)) ≈ O(1)
- 코테에서 시간 초과 방지

[코테에서 빠르게 쓰는 팁]
- 클래스 대신 함수 + 전역 배열로 구현하면 더 빠름
- parent = list(range(n+1)) 로 1-indexed 처리

[유니온 파인드 vs DFS/BFS]
- 연결 여부만 판별: 유니온 파인드 (더 빠름)
- 경로 탐색 필요: DFS/BFS
- 동적으로 간선 추가: 유니온 파인드 (DFS는 매번 재탐색)

[주의사항]
- Union-Find는 합치기만 가능, 분리는 불가!
- 분리가 필요하면 오프라인 쿼리로 역순 처리


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 1717번: 집합의 표현 (기본)
- 백준 1976번: 여행 가자
- 백준 4195번: 친구 네트워크

중급:
- 백준 1922번: 네트워크 연결 (크루스칼 MST)
- 백준 1043번: 거짓말
- 백준 20040번: 사이클 게임

고급:
- 백준 4386번: 별자리 만들기
- 백준 10775번: 공항
================================================================================
"""
