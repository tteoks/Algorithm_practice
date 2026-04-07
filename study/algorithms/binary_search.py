"""
================================================================================
                           이진 탐색 (Binary Search)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
이진 탐색은 **정렬된** 배열에서 원하는 값을 찾는 알고리즘입니다.
배열의 중간값과 비교하여 탐색 범위를 절반씩 줄여나갑니다.

핵심 특징:
- 시간복잡도: O(log n) - 매우 빠름!
- 전제 조건: 배열이 정렬되어 있어야 함
- 응용: 값 찾기, 조건을 만족하는 최소/최대값 찾기

언제 사용하나?
- 정렬된 배열에서 특정 값 찾기
- "최소 얼마 이상", "최대 얼마 이하" 같은 조건 문제
- 파라메트릭 서치 (결정 문제로 변환)


2. 동작 원리
--------------------------------------------------------------------------------
[1, 3, 5, 7, 9, 11, 13]에서 7을 찾는 과정:

    초기: left=0, right=6

    Step 1:
    [1, 3, 5, 7, 9, 11, 13]
     L        M          R
    mid = (0+6)//2 = 3
    arr[3] = 7 == target
    → 찾았다! return 3

[1, 3, 5, 7, 9, 11, 13]에서 9를 찾는 과정:

    Step 1:
    [1, 3, 5, 7, 9, 11, 13]
     L        M          R
    mid = 3, arr[3] = 7 < 9
    → 오른쪽 탐색! left = mid + 1 = 4

    Step 2:
    [1, 3, 5, 7, 9, 11, 13]
              L  M      R
    mid = (4+6)//2 = 5
    arr[5] = 11 > 9
    → 왼쪽 탐색! right = mid - 1 = 4

    Step 3:
    [1, 3, 5, 7, 9, 11, 13]
              LR
              M
    mid = 4, arr[4] = 9 == target
    → 찾았다! return 4


3. 시간복잡도
--------------------------------------------------------------------------------
| 방법         | 시간복잡도  |
|-------------|-----------|
| 순차 탐색    | O(n)      |
| 이진 탐색    | O(log n)  |

n = 1,000,000일 때:
- 순차 탐색: 최대 1,000,000번 비교
- 이진 탐색: 최대 20번 비교 (log₂(1000000) ≈ 20)


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

import bisect

# ================================
# 기본 이진 탐색
# ================================

def binary_search(arr: list[int], target: int) -> int:
    """
    정렬된 배열에서 target의 인덱스를 찾음
    없으면 -1 반환
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 탐색
        else:
            right = mid - 1  # 왼쪽 탐색

    return -1


# ================================
# Lower Bound / Upper Bound
# ================================

def lower_bound(arr: list[int], target: int) -> int:
    """
    target 이상인 첫 번째 위치 반환
    (target이 들어갈 수 있는 가장 왼쪽 위치)

    예: arr = [1, 2, 2, 2, 3], target = 2
        → return 1 (첫 번째 2의 위치)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr: list[int], target: int) -> int:
    """
    target 초과인 첫 번째 위치 반환
    (target이 들어갈 수 있는 가장 오른쪽 위치)

    예: arr = [1, 2, 2, 2, 3], target = 2
        → return 4 (마지막 2 다음 위치)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


# ================================
# Python bisect 모듈 사용
# ================================

"""
bisect_left(arr, x)  = lower_bound (x 이상인 첫 위치)
bisect_right(arr, x) = upper_bound (x 초과인 첫 위치)

활용:
- x의 개수: bisect_right(arr, x) - bisect_left(arr, x)
- x 존재 여부: arr[bisect_left(arr, x)] == x
"""

arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

left_idx = bisect.bisect_left(arr, x)   # 1
right_idx = bisect.bisect_right(arr, x)  # 4
count = right_idx - left_idx  # 3 (2가 3개)


# ================================
# 파라메트릭 서치 템플릿 (중요!)
# ================================

"""
파라메트릭 서치란?
- "최적화 문제"를 "결정 문제"로 바꿔서 이진 탐색으로 해결
- "최소 X를 구하라" → "X가 가능한가?"를 이진 탐색

예: "조건을 만족하는 최소 길이는?"
→ "길이가 L일 때 조건을 만족하나?" (Yes/No)
→ 만족하는 최소 L을 이진 탐색으로 찾기
"""

def parametric_search_template(arr: list, target: int) -> int:
    """
    조건을 만족하는 최소값 찾기 템플릿
    """
    def is_possible(value: int) -> bool:
        """value로 조건을 만족할 수 있는가?"""
        # 문제에 따라 구현
        pass

    left, right = 1, max(arr)  # 탐색 범위
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid):
            answer = mid
            right = mid - 1  # 더 작은 값 탐색
        else:
            left = mid + 1

    return answer


"""
================================================================================
5. 대표 문제: 나무 자르기
================================================================================

[문제]
나무 N개가 있고, 각 나무의 높이가 주어집니다.
절단기에 높이 H를 지정하면, H보다 높은 나무는 H 위의 부분이 잘립니다.
잘린 나무들의 길이 합이 최소 M 미터가 되도록 하는
절단기 높이 H의 최댓값을 구하세요.

[예시]
나무 높이: [20, 15, 10, 17]
필요한 나무: M = 7

H = 15일 때:
- 20 → 5m 획득
- 15 → 0m
- 10 → 0m (H보다 낮으므로 안 잘림)
- 17 → 2m 획득
- 총 7m → 조건 만족!

H = 16일 때:
- 20 → 4m
- 17 → 1m
- 총 5m → 부족!

답: H = 15


6. 문제 해설
--------------------------------------------------------------------------------
왜 이진 탐색?
    H는 0부터 가장 높은 나무 높이까지 가능
    H가 커지면 → 잘리는 양 감소
    H가 작아지면 → 잘리는 양 증가

    즉, H와 잘리는 양은 반비례!
    → 이진 탐색으로 조건을 만족하는 최대 H를 찾을 수 있음

파라메트릭 서치 적용:
    "H의 최댓값" 문제 → "H로 M 이상 자를 수 있나?" 결정 문제

    H = 15로 7m 이상 자를 수 있나? → Yes
    H = 16으로 7m 이상 자를 수 있나? → No
    ...
    Yes인 최대 H를 이진 탐색으로 찾기!

동작 과정 (trees = [20, 15, 10, 17], M = 7):

    left = 0, right = 20 (최대 높이)

    Step 1: mid = 10
        잘리는 양 = (20-10) + (15-10) + (10-10) + (17-10)
                 = 10 + 5 + 0 + 7 = 22 >= 7
        → 가능! answer = 10, left = 11

    Step 2: mid = 15
        잘리는 양 = 5 + 0 + 0 + 2 = 7 >= 7
        → 가능! answer = 15, left = 16

    Step 3: mid = 18
        잘리는 양 = 2 + 0 + 0 + 0 = 2 < 7
        → 불가능! right = 17

    Step 4: mid = 16
        잘리는 양 = 4 + 0 + 0 + 1 = 5 < 7
        → 불가능! right = 15

    left > right, 종료!
    answer = 15


7. 코드 구현
--------------------------------------------------------------------------------
"""


def cut_tree(trees: list[int], M: int) -> int:
    """
    나무 자르기 - 파라메트릭 서치

    Args:
        trees: 나무 높이 리스트
        M: 필요한 나무 길이

    Returns:
        절단기 높이의 최댓값
    """
    def get_wood(height: int) -> int:
        """높이 H로 자를 때 얻는 나무의 총 길이"""
        total = 0
        for tree in trees:
            if tree > height:
                total += tree - height
        return total

    left, right = 0, max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if get_wood(mid) >= M:
            # 조건 만족! 더 높은 H 탐색
            answer = mid
            left = mid + 1
        else:
            # 조건 불만족! 더 낮은 H 탐색
            right = mid - 1

    return answer


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def cut_tree_with_trace(trees: list[int], M: int) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"나무 높이: {trees}")
    print(f"필요한 나무: {M}m")
    print("=" * 60)

    def get_wood(height: int) -> int:
        total = 0
        details = []
        for tree in trees:
            if tree > height:
                cut = tree - height
                total += cut
                details.append(f"{tree}-{height}={cut}")
            else:
                details.append(f"{tree}(X)")
        return total, details

    left, right = 0, max(trees)
    answer = 0
    step = 0

    print(f"\n탐색 범위: {left} ~ {right}")
    print("\n[이진 탐색 과정]")

    while left <= right:
        step += 1
        mid = (left + right) // 2
        wood, details = get_wood(mid)

        print(f"\nStep {step}: H = {mid}")
        print(f"  계산: {' + '.join(details)}")
        print(f"  획득량: {wood}m", end="")

        if wood >= M:
            print(f" >= {M} → 가능! 더 높은 H 탐색")
            print(f"  → answer = {mid}, left = {mid + 1}")
            answer = mid
            left = mid + 1
        else:
            print(f" < {M} → 불가능! 더 낮은 H 탐색")
            print(f"  → right = {mid - 1}")
            right = mid - 1

    print(f"\n{'=' * 60}")
    print(f"최종 답: H = {answer}")
    return answer


# ================================
# 추가 예제: 정렬된 배열에서 개수 세기
# ================================

def count_in_range(arr: list[int], left_val: int, right_val: int) -> int:
    """
    정렬된 배열에서 [left_val, right_val] 범위의 원소 개수
    """
    left_idx = bisect.bisect_left(arr, left_val)
    right_idx = bisect.bisect_right(arr, right_val)
    return right_idx - left_idx


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("이진 탐색 예제 실행")
    print("=" * 60)

    # 기본 이진 탐색
    print("\n[기본 이진 탐색]")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for target in [7, 9, 4]:
        idx = binary_search(arr, target)
        print(f"{arr}에서 {target} 찾기 → 인덱스: {idx}")

    # Lower/Upper Bound
    print("\n[Lower/Upper Bound]")
    arr = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    lb = lower_bound(arr, target)
    ub = upper_bound(arr, target)
    print(f"배열: {arr}, target: {target}")
    print(f"lower_bound: {lb}, upper_bound: {ub}")
    print(f"{target}의 개수: {ub - lb}")

    # bisect 사용
    print("\n[bisect 모듈 사용]")
    print(f"bisect_left: {bisect.bisect_left(arr, 2)}")
    print(f"bisect_right: {bisect.bisect_right(arr, 2)}")

    # 나무 자르기
    print("\n" + "=" * 60)
    print("나무 자르기 문제")
    print("=" * 60)

    trees = [20, 15, 10, 17]
    M = 7
    result = cut_tree(trees, M)
    print(f"\n빠른 테스트: H = {result}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    cut_tree_with_trace([20, 15, 10, 17], 7)


"""
================================================================================
9. 이진 탐색 팁
================================================================================

[경계 조건 주의!]
- while left <= right vs while left < right
- mid = (left + right) // 2 에서 오버플로우 주의
  → mid = left + (right - left) // 2 가 더 안전

[left, right 갱신]
- 값을 찾는 문제: left = mid + 1, right = mid - 1
- lower_bound: left = mid + 1, right = mid
- upper_bound: left = mid + 1, right = mid


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 1920번: 수 찾기
- 백준 10816번: 숫자 카드 2 (개수 세기)

파라메트릭 서치:
- 백준 2805번: 나무 자르기
- 백준 1654번: 랜선 자르기
- 백준 2110번: 공유기 설치

응용:
- 백준 12015번: 가장 긴 증가하는 부분 수열 2 (LIS)
- 프로그래머스: 입국심사
================================================================================
"""
