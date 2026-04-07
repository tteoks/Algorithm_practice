"""
================================================================================
                         힙 (Heap) / 우선순위 큐 (Priority Queue)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
힙은 "가장 큰(또는 작은) 값을 빠르게 찾을 수 있는" 자료구조입니다.
완전 이진 트리 형태로 구현됩니다.

종류:
- 최소 힙 (Min Heap): 부모 <= 자식 (루트가 최솟값)
- 최대 힙 (Max Heap): 부모 >= 자식 (루트가 최댓값)

Python의 heapq는 최소 힙만 지원!
(최대 힙은 값을 음수로 변환해서 사용)

핵심 특징:
- 최솟값/최댓값 조회: O(1)
- 삽입: O(log n)
- 삭제(최솟값/최댓값): O(log n)

언제 사용하나?
- "가장 큰/작은 k개"
- "매번 최솟값/최댓값을 선택"
- 다익스트라 알고리즘
- 작업 스케줄링


2. 동작 원리
--------------------------------------------------------------------------------
[최소 힙 구조]
           1         ← 루트 (최솟값)
         /   \
        3     2
       / \   /
      7   4 5

    배열로 표현: [1, 3, 2, 7, 4, 5]
    인덱스:       0  1  2  3  4  5

    부모-자식 관계:
    - 부모 인덱스: (i - 1) // 2
    - 왼쪽 자식: 2 * i + 1
    - 오른쪽 자식: 2 * i + 2


[삽입 (Push) - 값 6 삽입]
    1. 맨 끝에 추가: [1, 3, 2, 7, 4, 5, 6]

           1
         /   \
        3     2
       / \   / \
      7   4 5   6  ← 새로 추가

    2. 부모와 비교하며 위로 이동 (heapify up)
       6 > 2 → 이동 안 함
       완료: [1, 3, 2, 7, 4, 5, 6]


[삭제 (Pop) - 최솟값 삭제]
    1. 루트(최솟값)를 반환

           1         ← 이걸 반환
         /   \
        3     2
       / \   /
      7   4 5

    2. 마지막 원소를 루트로 이동

           5
         /   \
        3     2
       / \
      7   4

    3. 자식과 비교하며 아래로 이동 (heapify down)
       5 > 2 → 2와 교환

           2
         /   \
        3     5
       / \
      7   4

       5 > 4? 5 > 7? 둘 다 아니므로 완료
       결과: [2, 3, 5, 7, 4]


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산              | 시간복잡도  |
|------------------|-----------|
| 최솟값 조회       | O(1)      |
| 삽입 (push)      | O(log n)  |
| 삭제 (pop)       | O(log n)  |
| 힙 생성 (heapify)| O(n)      |


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

import heapq

# ================================
# 기본 사용법 (최소 힙)
# ================================

# 힙 생성
heap = []

# 삽입 (push)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print(f"힙: {heap}")  # [1, 1, 4, 3, 5] - 내부 순서는 힙 속성 유지

# 최솟값 조회 (삭제 안 함)
min_val = heap[0]
print(f"최솟값: {min_val}")  # 1

# 삭제 + 반환 (pop)
min_val = heapq.heappop(heap)
print(f"Pop: {min_val}")  # 1
print(f"힙: {heap}")  # [1, 3, 4, 5]

# 리스트를 힙으로 변환
arr = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(arr)  # O(n) - 제자리 변환
print(f"힙으로 변환: {arr}")


# ================================
# 최대 힙 (음수 트릭)
# ================================

# Python heapq는 최소 힙만 지원
# 최대 힙을 쓰려면 값을 음수로!

max_heap = []
values = [3, 1, 4, 1, 5]

# 삽입 시 음수로
for v in values:
    heapq.heappush(max_heap, -v)

# 꺼낼 때 음수로 복원
max_val = -heapq.heappop(max_heap)  # 5
print(f"최댓값: {max_val}")


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: k번째 작은 값
def kth_smallest(arr: list[int], k: int) -> int:
    """배열에서 k번째로 작은 값"""
    heapq.heapify(arr)
    for _ in range(k - 1):
        heapq.heappop(arr)
    return arr[0]


# 패턴 2: k번째 큰 값
def kth_largest(arr: list[int], k: int) -> int:
    """배열에서 k번째로 큰 값"""
    # 방법 1: 최대 힙
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    return -max_heap[0]


# 패턴 3: 가장 작은 k개
def k_smallest(arr: list[int], k: int) -> list[int]:
    """배열에서 가장 작은 k개"""
    return heapq.nsmallest(k, arr)


# 패턴 4: 튜플로 우선순위 지정
def process_tasks():
    """(우선순위, 작업) 형태로 관리"""
    tasks = []
    heapq.heappush(tasks, (2, "밥 먹기"))
    heapq.heappush(tasks, (1, "코딩하기"))  # 우선순위 높음 (숫자 작음)
    heapq.heappush(tasks, (3, "잠자기"))

    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"처리: {task} (우선순위 {priority})")


"""
================================================================================
5. 대표 문제: 더 맵게 (프로그래머스)
================================================================================

[문제]
모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
스코빌 지수가 가장 낮은 두 음식을 다음과 같이 섞습니다:

    새 스코빌 = 가장 낮은 스코빌 + (두 번째로 낮은 스코빌 * 2)

모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복합니다.
섞어야 하는 최소 횟수를 return하세요.
만들 수 없으면 -1을 return합니다.

[예시]
Input: scoville = [1, 2, 3, 9, 10, 12], K = 7
Output: 2

과정:
1. 섞기 전: [1, 2, 3, 9, 10, 12], 최솟값 1 < 7
2. 1회: 1 + 2*2 = 5 → [3, 5, 9, 10, 12]
3. 2회: 3 + 5*2 = 13 → [9, 10, 12, 13]
4. 최솟값 9 >= 7, 완료!


6. 문제 해설
--------------------------------------------------------------------------------
왜 힙을 쓰나?
    - 매번 "가장 작은 값 2개"를 찾아야 함
    - 정렬하면? 섞을 때마다 O(n log n)
    - 힙 사용하면? 삽입/삭제가 O(log n)

알고리즘:
    1. 배열을 최소 힙으로 변환
    2. 최솟값이 K 미만인 동안:
       - 가장 작은 값 pop
       - 두 번째로 작은 값 pop
       - 새 값 = 첫 번째 + 두 번째 * 2
       - 새 값을 힙에 push
       - 횟수 증가
    3. 힙에 1개만 남았는데 K 미만이면 -1

동작 과정 (scoville = [1, 2, 3, 9, 10, 12], K = 7):

    힙으로 변환: [1, 2, 3, 9, 10, 12]
    (최소 힙이므로 1이 루트)

    [반복 1]
    최솟값: 1 (K=7 미만) → 섞기!
    first = heappop() = 1
    second = heappop() = 2
    new = 1 + 2*2 = 5
    heappush(5)
    힙: [3, 9, 5, 12, 10]  (내부적으로 heapify됨 → [3, 5, 9, 12, 10] 형태)
    실제 최소 힙: [3, 5, ...]

    [반복 2]
    최솟값: 3 (K=7 미만) → 섞기!
    first = 3, second = 5
    new = 3 + 5*2 = 13
    힙: [9, 10, 13, 12]

    [반복 3]
    최솟값: 9 >= 7 → 종료!

    답: 2회


7. 코드 구현
--------------------------------------------------------------------------------
"""


def make_spicy(scoville: list[int], K: int) -> int:
    """
    더 맵게 - 최소 힙 활용

    Args:
        scoville: 스코빌 지수 리스트
        K: 목표 스코빌 지수

    Returns:
        섞는 최소 횟수, 불가능하면 -1
    """
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    count = 0

    # 최솟값이 K 미만인 동안 반복
    while scoville[0] < K:
        # 음식이 1개만 남으면 불가능
        if len(scoville) < 2:
            return -1

        # 가장 작은 두 개를 꺼내서 섞기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + second * 2

        # 새 음식을 힙에 추가
        heapq.heappush(scoville, new_scoville)
        count += 1

    return count


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def make_spicy_with_trace(scoville: list[int], K: int) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"스코빌: {scoville}")
    print(f"목표 K: {K}")
    print("=" * 60)

    heap = scoville.copy()
    heapq.heapify(heap)
    print(f"힙으로 변환: {heap}")

    count = 0

    while heap[0] < K:
        print(f"\n[반복 {count + 1}]")
        print(f"  현재 힙: {heap}")
        print(f"  최솟값: {heap[0]} < K({K}) → 섞기!")

        if len(heap) < 2:
            print(f"  음식이 1개만 남음 → 불가능!")
            return -1

        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new_val = first + second * 2

        print(f"  first: {first}, second: {second}")
        print(f"  새 스코빌: {first} + {second}*2 = {new_val}")

        heapq.heappush(heap, new_val)
        count += 1

        print(f"  힙에 추가 후: {heap}")

    print(f"\n[종료]")
    print(f"  최솟값: {heap[0]} >= K({K})")
    print(f"\n정답: {count}회")
    return count


# ================================
# 추가 예제: 중앙값 실시간 계산
# ================================

class MedianFinder:
    """
    두 개의 힙을 사용해서 중앙값을 O(log n)에 계산

    max_heap: 작은 쪽 절반 (최대 힙)
    min_heap: 큰 쪽 절반 (최소 힙)

    예: [1, 2, 3, 4, 5]
    max_heap: [1, 2] (최대값 2)
    min_heap: [3, 4, 5] (최소값 3)
    중앙값: (2 + 3) / 2 = 2.5
    """

    def __init__(self):
        self.max_heap = []  # 작은 쪽 (음수로 저장)
        self.min_heap = []  # 큰 쪽

    def add_num(self, num: int) -> None:
        # 작은 쪽에 먼저 추가
        heapq.heappush(self.max_heap, -num)

        # 작은 쪽의 최대가 큰 쪽의 최소보다 크면 이동
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # 크기 균형 맞추기 (max_heap이 같거나 1개 많게)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("힙 예제 실행")
    print("=" * 60)

    # 기본 힙 연산
    print("\n[기본 힙 연산]")
    heap = []
    for val in [5, 3, 8, 1, 2]:
        heapq.heappush(heap, val)
        print(f"push({val}) → 힙: {heap}")

    print()
    while heap:
        val = heapq.heappop(heap)
        print(f"pop() = {val} → 힙: {heap}")

    # 최대 힙
    print("\n[최대 힙]")
    max_heap = []
    for val in [5, 3, 8, 1, 2]:
        heapq.heappush(max_heap, -val)
    print(f"원본: [5, 3, 8, 1, 2]")
    print(f"최대 힙 (음수): {max_heap}")
    print(f"최댓값: {-max_heap[0]}")

    # 더 맵게 테스트
    print("\n" + "=" * 60)
    print("더 맵게 문제")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3, 9, 10, 12], 7),
        ([1, 1, 1], 10),
    ]

    for scoville, K in test_cases:
        result = make_spicy(scoville.copy(), K)
        print(f"scoville={scoville}, K={K} → {result}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    make_spicy_with_trace([1, 2, 3, 9, 10, 12], 7)

    # 중앙값 finder
    print("\n" + "=" * 60)
    print("실시간 중앙값")
    print("=" * 60)
    mf = MedianFinder()
    for num in [1, 2, 3, 4, 5]:
        mf.add_num(num)
        print(f"add({num}) → 중앙값: {mf.find_median()}")


"""
================================================================================
9. 힙 활용 팁
================================================================================

[최대 힙 만들기]
- 값을 넣을 때 -x로, 뺄 때 -x로

[튜플 정렬]
- (우선순위, 값) 형태로 넣으면 우선순위 기준 정렬
- 우선순위 같으면 두 번째 요소 기준

[heapq 유용한 함수]
- heapq.nsmallest(k, arr): 가장 작은 k개
- heapq.nlargest(k, arr): 가장 큰 k개


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 1927번: 최소 힙
- 백준 11279번: 최대 힙
- 백준 11286번: 절댓값 힙

중급:
- 프로그래머스: 더 맵게
- 백준 1715번: 카드 정렬하기
- 프로그래머스: 디스크 컨트롤러

고급:
- 백준 1655번: 가운데를 말해요 (중앙값)
- 백준 7662번: 이중 우선순위 큐
================================================================================
"""
