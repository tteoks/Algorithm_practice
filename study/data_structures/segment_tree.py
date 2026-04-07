"""
================================================================================
                         세그먼트 트리 (Segment Tree)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
세그먼트 트리는 "구간에 대한 질의(query)"를 빠르게 처리하는 자료구조입니다.
배열의 특정 구간에 대한 합, 최솟값, 최댓값 등을 효율적으로 구합니다.

핵심 연산:
- 구간 질의 (Query): 특정 범위의 합/최솟값/최댓값 → O(log n)
- 점 갱신 (Update): 특정 인덱스의 값 변경 → O(log n)

왜 필요한가?
- 단순 배열: 구간 합 O(n), 갱신 O(1)
- 누적 합: 구간 합 O(1), 갱신 O(n)
- 세그먼트 트리: 구간 합 O(log n), 갱신 O(log n) ← 둘 다 빠름!

언제 사용하나?
- "구간 합 + 값 변경"이 반복되는 문제
- "구간 최솟값/최댓값"
- "구간 GCD"
- 값 변경이 빈번한 구간 질의


2. 동작 원리
--------------------------------------------------------------------------------

배열: [1, 3, 5, 7, 9, 11]

[세그먼트 트리 구조] - 구간 합 기준

              36 [0-5]           ← 전체 합
            /        \
        9 [0-2]      27 [3-5]    ← 반으로 나눔
       /    \        /     \
    4 [0-1]  5[2]  16[3-4]  11[5]
    /  \           /    \
  1[0] 3[1]     7[3]  9[4]

    각 노드: 해당 구간의 합을 저장
    리프 노드: 원본 배열의 각 원소


[구간 합 질의] - query(1, 4) = arr[1]+arr[2]+arr[3]+arr[4]

              36 [0-5]
            /        \
        9 [0-2]      27 [3-5]
       /    \        /     \
    4 [0-1]  5[2]  16[3-4]  11[5]
    /  \           /    \
  1[0] 3[1]     7[3]  9[4]

    탐색 과정:
    [0-5]: 부분 겹침 → 양쪽 탐색
    [0-2]: 부분 겹침 → 양쪽 탐색
    [0-1]: 부분 겹침 → 양쪽 탐색
    [0]: 범위 밖 → 0
    [1]: 범위 안 → 3
    [2]: 범위 안 → 5
    [3-5]: 부분 겹침 → 양쪽 탐색
    [3-4]: 범위 안 → 16 (한 번에 반환!)
    [5]: 범위 밖 → 0

    결과: 3 + 5 + 16 = 24 ✓ (3+5+7+9 = 24)


[점 갱신] - update(2, 10) : arr[2]를 5→10으로

    변경된 값의 차이: 10 - 5 = 5

              36+5=41 [0-5]      ← 루트까지 갱신
            /        \
       9+5=14 [0-2]   27 [3-5]
       /    \
    4 [0-1]  10[2]   ← 리프 갱신
    /  \
  1[0] 3[1]


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산              | 세그먼트 트리  | 단순 배열  | 누적 합    |
|------------------|-------------|---------|----------|
| 구간 질의 (Query) | O(log n)    | O(n)    | O(1)     |
| 점 갱신 (Update)  | O(log n)    | O(1)    | O(n)     |
| 트리 생성 (Build) | O(n)        | -       | O(n)     |

* 질의와 갱신이 모두 빈번할 때 세그먼트 트리가 유리!


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""


# ================================
# 기본 구현 (구간 합)
# ================================

class SegmentTree:
    def __init__(self, arr: list):
        """배열로 세그먼트 트리 생성 - O(n)"""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 넉넉하게 4배
        self.arr = arr
        self._build(1, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int):
        """트리 생성 (재귀)"""
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)        # 왼쪽 자식
        self._build(2 * node + 1, mid + 1, end)  # 오른쪽 자식
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, left: int, right: int) -> int:
        """구간 [left, right]의 합 - O(log n)"""
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        # 범위 밖
        if right < start or end < left:
            return 0

        # 완전히 범위 안
        if left <= start and end <= right:
            return self.tree[node]

        # 부분 겹침 → 양쪽 탐색
        mid = (start + end) // 2
        return (self._query(2 * node, start, mid, left, right) +
                self._query(2 * node + 1, mid + 1, end, left, right))

    def update(self, idx: int, val: int):
        """arr[idx]를 val로 변경 - O(log n)"""
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


# ================================
# 구간 최솟값 세그먼트 트리
# ================================

class MinSegmentTree:
    def __init__(self, arr: list):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.arr = arr
        self._build(1, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return float('inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self._query(2 * node, start, mid, left, right),
                   self._query(2 * node + 1, mid + 1, end, left, right))

    def update(self, idx: int, val: int):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])


# ================================
# 간결한 구현 (코테용 - 비재귀)
# ================================

class SegTree:
    """비재귀 세그먼트 트리 (Bottom-up, 더 빠름)"""

    def __init__(self, arr: list):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        # 리프 채우기
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # 내부 노드 채우기 (아래에서 위로)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx: int, val: int):
        """idx번째 값을 val로 변경"""
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, left: int, right: int) -> int:
        """[left, right] 구간 합"""
        res = 0
        left += self.n
        right += self.n + 1
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res


"""
================================================================================
5. 대표 문제: 구간 합 구하기 (백준 2042)
================================================================================

[문제]
N개의 수가 있다. 다음 두 연산을 수행하시오.
- 1 b c: b번째 수를 c로 변경
- 2 b c: b번째부터 c번째까지의 합을 출력

[예시]
Input:
5 2 2
1 2 3 4 5
1 3 6        → arr[3]을 6으로 변경
2 2 5        → arr[2]+arr[3]+arr[4]+arr[5] 출력
1 5 2        → arr[5]를 2로 변경
2 3 5        → arr[3]+arr[4]+arr[5] 출력

Output:
17           → 2+6+4+5 = 17
12           → 6+4+2 = 12


6. 문제 해설
--------------------------------------------------------------------------------
왜 세그먼트 트리를 쓰나?
    - 구간 합 질의 + 값 변경이 반복
    - 단순 누적합: 갱신 O(n) → 최대 100만 번 × O(n) = TLE
    - 세그먼트 트리: 갱신 O(log n), 질의 O(log n)

동작 과정 (arr = [1, 2, 3, 4, 5]):

    초기 세그먼트 트리 (구간 합):
              15 [1-5]
            /        \
        6 [1-3]      9 [4-5]
       /    \        /    \
    3 [1-2]  3[3]  4[4]  5[5]
    /  \
  1[1] 2[2]

    [1 3 6] → arr[3] = 6 (3→6, 차이 +3)
              18 [1-5]
            /        \
        9 [1-3]      9 [4-5]
       /    \
    3 [1-2]  6[3]    ← 갱신!

    [2 2 5] → query(2, 5)
    arr[2]+arr[3]+arr[4]+arr[5] = 2+6+4+5 = 17

    [1 5 2] → arr[5] = 2 (5→2, 차이 -3)
              15 [1-5]
                     \
                  6 [4-5]
                      \
                     2[5]    ← 갱신!

    [2 3 5] → query(3, 5)
    arr[3]+arr[4]+arr[5] = 6+4+2 = 12


7. 코드 구현
--------------------------------------------------------------------------------
"""


def solve_range_sum():
    """백준 2042 - 구간 합 구하기"""
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    seg = SegmentTree(arr)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            seg.update(b - 1, c)  # 1-indexed → 0-indexed
        else:
            print(seg.query(b - 1, c - 1))


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


class SegmentTreeWithTrace:
    """동작 과정을 출력하는 세그먼트 트리"""

    def __init__(self, arr: list):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr[:]
        print(f"배열: {arr}")
        self._build(1, 0, self.n - 1)
        print(f"트리: {self.tree[1:2*self.n+1]}")

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, left: int, right: int) -> int:
        print(f"\nQuery({left}, {right}): arr[{left}]~arr[{right}]의 합")
        result = self._query_trace(1, 0, self.n - 1, left, right, "  ")
        print(f"  결과: {result}")
        return result

    def _query_trace(self, node, start, end, left, right, indent):
        if right < start or end < left:
            print(f"{indent}[{start}-{end}] 범위 밖 → 0")
            return 0
        if left <= start and end <= right:
            print(f"{indent}[{start}-{end}] 범위 안 → {self.tree[node]}")
            return self.tree[node]
        print(f"{indent}[{start}-{end}] 부분 겹침 → 분할")
        mid = (start + end) // 2
        l = self._query_trace(2 * node, start, mid, left, right, indent + "  ")
        r = self._query_trace(2 * node + 1, mid + 1, end, left, right, indent + "  ")
        return l + r

    def update(self, idx: int, val: int):
        print(f"\nUpdate({idx}, {val}): arr[{idx}] = {self.arr[idx]} → {val}")
        self._update_trace(1, 0, self.n - 1, idx, val, "  ")
        print(f"  트리: {self.tree[1:2*self.n+1]}")

    def _update_trace(self, node, start, end, idx, val, indent):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
            print(f"{indent}[{start}] 리프 갱신 → {val}")
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update_trace(2 * node, start, mid, idx, val, indent + "  ")
        else:
            self._update_trace(2 * node + 1, mid + 1, end, idx, val, indent + "  ")
        old = self.tree[node]
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        print(f"{indent}[{start}-{end}] {old} → {self.tree[node]}")


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("세그먼트 트리 예제 실행")
    print("=" * 60)

    # 기본 사용
    print("\n[기본 사용]")
    arr = [1, 3, 5, 7, 9, 11]
    seg = SegmentTree(arr)

    print(f"배열: {arr}")
    print(f"구간 합 [1, 3]: {seg.query(1, 3)}")  # 3+5+7 = 15
    print(f"구간 합 [0, 5]: {seg.query(0, 5)}")  # 전체 = 36
    print(f"구간 합 [2, 4]: {seg.query(2, 4)}")  # 5+7+9 = 21

    seg.update(2, 10)  # arr[2] = 5 → 10
    print(f"\narr[2] = 10으로 변경 후:")
    print(f"구간 합 [1, 3]: {seg.query(1, 3)}")  # 3+10+7 = 20

    # 최솟값 세그먼트 트리
    print("\n[구간 최솟값]")
    arr2 = [5, 3, 7, 1, 9, 2]
    min_seg = MinSegmentTree(arr2)
    print(f"배열: {arr2}")
    print(f"구간 최솟값 [0, 3]: {min_seg.query(0, 3)}")  # 1
    print(f"구간 최솟값 [2, 5]: {min_seg.query(2, 5)}")  # 1

    # 비재귀 세그먼트 트리
    print("\n[비재귀 세그먼트 트리]")
    arr3 = [1, 2, 3, 4, 5]
    fast_seg = SegTree(arr3)
    print(f"배열: {arr3}")
    print(f"구간 합 [1, 3]: {fast_seg.query(1, 3)}")  # 2+3+4 = 9

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)

    print("\n[트리 생성]")
    trace = SegmentTreeWithTrace([1, 2, 3, 4, 5])

    trace.query(1, 3)
    trace.update(2, 6)
    trace.query(1, 3)

    # 백준 2042 예시
    print("\n" + "=" * 60)
    print("백준 2042 예시")
    print("=" * 60)

    arr_boj = [1, 2, 3, 4, 5]
    seg_boj = SegmentTree(arr_boj)
    print(f"배열: {arr_boj}")

    # 1 3 6 → arr[3] = 6 (1-indexed → 0-indexed: arr[2] = 6)
    seg_boj.update(2, 6)
    print(f"arr[3] = 6 → {seg_boj.arr}")

    # 2 2 5 → query(2, 5) (1-indexed → 0-indexed: query(1, 4))
    print(f"sum(2~5) = {seg_boj.query(1, 4)}")  # 2+6+4+5 = 17

    # 1 5 2 → arr[5] = 2 (0-indexed: arr[4] = 2)
    seg_boj.update(4, 2)
    print(f"arr[5] = 2 → {seg_boj.arr}")

    # 2 3 5 → query(3, 5) (0-indexed: query(2, 4))
    print(f"sum(3~5) = {seg_boj.query(2, 4)}")  # 6+4+2 = 12


"""
================================================================================
9. 세그먼트 트리 활용 팁
================================================================================

[언제 세그먼트 트리?]
- "구간 질의 + 값 변경" 조합 → 세그먼트 트리
- 값 변경 없이 구간 합만 → 누적 합 (더 간단)
- 구간 전체를 같은 값으로 변경 → Lazy Propagation

[재귀 vs 비재귀]
- 재귀: 이해하기 쉬움, 디버깅 편함
- 비재귀: 더 빠름 (상수 차이), 코테에서 속도 필요할 때

[노드 크기]
- 트리 배열 크기: 4 * n (넉넉하게)
- 정확히는 2 * (2^⌈log₂n⌉)

[자주 사용하는 변형]
- 구간 합: tree[node] = left + right
- 구간 최솟값: tree[node] = min(left, right)
- 구간 최댓값: tree[node] = max(left, right)
- 구간 GCD: tree[node] = gcd(left, right)

[Lazy Propagation]
- 구간 갱신 (Range Update)이 필요할 때
- 예: arr[2]~arr[5]에 모두 +3
- 일반 세그먼트 트리: O(n log n)
- Lazy: O(log n)


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 2042번: 구간 합 구하기 (기본)
- 백준 11505번: 구간 곱 구하기
- 백준 2357번: 최솟값과 최댓값

중급:
- 백준 10868번: 최솟값
- 백준 1275번: 커피숍2
- 백준 2243번: 사탕상자

고급:
- 백준 10999번: 구간 합 구하기 2 (Lazy Propagation)
- 백준 1168번: 요세푸스 문제 2
- 백준 7578번: 공장
================================================================================
"""
