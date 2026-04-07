"""
================================================================================
                           투 포인터 (Two Pointer)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
투 포인터는 두 개의 포인터(인덱스)를 사용해서 배열을 탐색하는 기법입니다.
보통 정렬된 배열에서 O(n²)을 O(n)으로 줄일 수 있습니다.

두 가지 유형:
1. 양끝에서 시작해서 중간으로 이동 (left, right)
2. 같은 방향으로 이동 (start, end 또는 slow, fast)

핵심 특징:
- 시간복잡도: O(n) - 각 포인터가 배열을 한 번씩만 순회
- 공간복잡도: O(1) - 추가 메모리 거의 없음

언제 사용하나?
- "두 수의 합이 X인 쌍 찾기"
- "정렬된 배열에서 특정 조건 만족하는 쌍"
- "연속 부분 배열" (슬라이딩 윈도우와 유사)
- "중복 제거", "원소 이동"


2. 동작 원리
--------------------------------------------------------------------------------

[유형 1: 양끝에서 시작 (Two Sum in Sorted Array)]

    정렬된 배열 [1, 2, 3, 4, 6]에서 합이 6인 두 수 찾기

    초기: left=0, right=4
    [1, 2, 3, 4, 6]
     L           R

    Step 1: arr[L] + arr[R] = 1 + 6 = 7 > 6
            → 합이 크다 → right를 줄임
    [1, 2, 3, 4, 6]
     L        R

    Step 2: arr[L] + arr[R] = 1 + 4 = 5 < 6
            → 합이 작다 → left를 늘림
    [1, 2, 3, 4, 6]
        L     R

    Step 3: arr[L] + arr[R] = 2 + 4 = 6 == 6
            → 찾았다! return (1, 3)


[유형 2: 같은 방향 (Fast & Slow - 중복 제거)]

    배열 [1, 1, 2, 2, 3]에서 중복 제거

    slow=0: 유니크한 원소의 마지막 위치
    fast=1: 탐색 중인 위치

    [1, 1, 2, 2, 3]
     S  F

    arr[F]=1 == arr[S]=1 → 중복! fast만 이동
    [1, 1, 2, 2, 3]
     S     F

    arr[F]=2 != arr[S]=1 → 새로운 값!
    slow++, arr[slow] = arr[fast]
    [1, 2, 2, 2, 3]
        S  F

    arr[F]=2 == arr[S]=2 → 중복! fast만 이동
    [1, 2, 2, 2, 3]
        S     F

    arr[F]=3 != arr[S]=2 → 새로운 값!
    slow++, arr[slow] = arr[fast]
    [1, 2, 3, 2, 3]
           S     F

    끝! 유니크 원소 개수 = slow + 1 = 3


3. 시간복잡도
--------------------------------------------------------------------------------
| 방법                | 시간복잡도  |
|--------------------|-----------|
| 브루트포스 (이중 루프)| O(n²)     |
| 투 포인터           | O(n)      |


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

# ================================
# 유형 1: 양끝에서 시작
# ================================

def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int]:
    """
    정렬된 배열에서 합이 target인 두 수의 인덱스

    전제: 배열이 정렬되어 있음
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1  # 합을 키우려면 left를 오른쪽으로
        else:
            right -= 1  # 합을 줄이려면 right를 왼쪽으로

    return (-1, -1)  # 못 찾음


def three_sum(arr: list[int], target: int) -> list[tuple[int, int, int]]:
    """
    세 수의 합이 target인 모든 조합 (중복 제외)

    방법: 하나를 고정하고 나머지 두 개는 투 포인터
    """
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):
        # 중복 건너뛰기
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == target:
                result.append((arr[i], arr[left], arr[right]))
                # 중복 건너뛰기
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


# ================================
# 유형 2: 같은 방향
# ================================

def remove_duplicates(arr: list[int]) -> int:
    """
    정렬된 배열에서 중복 제거 (in-place)
    유니크한 원소 개수 반환
    """
    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


def move_zeros(arr: list[int]) -> None:
    """
    0을 배열 끝으로 이동 (in-place)

    예: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
    """
    slow = 0  # 0이 아닌 원소가 들어갈 위치

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1


# ================================
# 유형 3: 구간 탐색 (연속 부분 배열)
# ================================

def subarray_sum(arr: list[int], target: int) -> tuple[int, int]:
    """
    합이 target인 연속 부분 배열 찾기 (양수만 있는 경우)

    예: [1, 2, 3, 7, 5], target=12 → (2, 4) [3, 7, 5가 아니라 2, 3+7=10 아님]
        실제로는 [2, 3, 7] 인덱스 (1, 3)
    """
    n = len(arr)
    start = 0
    current_sum = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return (start, end)

    return (-1, -1)


"""
================================================================================
5. 대표 문제: 주어진 합을 가지는 부분 연속 수열
================================================================================

[문제]
N개의 자연수로 이루어진 수열이 있습니다.
이 중 연속된 몇 개의 수의 합이 M이 되는 경우의 수를 구하세요.

[예시]
Input: arr = [1, 2, 3, 2, 5], M = 5
Output: 3

경우:
1. [2, 3] → 2 + 3 = 5
2. [3, 2] → 3 + 2 = 5
3. [5] → 5 = 5


6. 문제 해설
--------------------------------------------------------------------------------
브루트포스로 풀면?
    모든 시작점과 끝점 조합: O(n²)
    각 구간의 합 계산: O(n)
    총: O(n³) 또는 누적합 사용 시 O(n²)

투 포인터로 풀면?
    두 포인터가 배열을 한 번씩만 순회: O(n)

핵심 아이디어:
    - start, end 두 포인터로 구간 [start, end]를 관리
    - 구간 합이 M보다 작으면 end를 늘림 (합 증가)
    - 구간 합이 M 이상이면 start를 늘림 (합 감소)

    왜 가능한가?
    → 모든 원소가 양수이므로:
      - end를 늘리면 합이 증가
      - start를 늘리면 합이 감소
    → 단조성(monotonic)이 있어서 투 포인터 가능!

동작 과정 (arr = [1, 2, 3, 2, 5], M = 5):

    초기: start=0, end=0, sum=0, count=0

    [1, 2, 3, 2, 5]
     S
     E

    end=0: sum += arr[0] = 1
           sum(1) < M(5) → 다음

    end=1: sum += arr[1] = 3
           sum(3) < M(5) → 다음

    end=2: sum += arr[2] = 6
           sum(6) >= M(5)!
           → sum(6) > M(5)이므로 start 이동

           sum -= arr[0] = 5
           start=1
           sum(5) == M(5)! count++ (count=1)

           sum(5) >= M(5)이므로 계속
           sum -= arr[1] = 3
           start=2

    end=3: sum += arr[3] = 5
           sum(5) == M(5)! count++ (count=2)
           sum(5) >= M(5)이므로
           sum -= arr[2] = 2
           start=3

    end=4: sum += arr[4] = 7
           sum(7) > M(5)
           sum -= arr[3] = 5
           start=4
           sum(5) == M(5)! count++ (count=3)

    종료! 답: 3


7. 코드 구현
--------------------------------------------------------------------------------
"""


def count_subarray_sum(arr: list[int], M: int) -> int:
    """
    합이 M인 연속 부분 수열의 개수

    Args:
        arr: 자연수 배열
        M: 목표 합

    Returns:
        합이 M인 부분 수열의 개수
    """
    n = len(arr)
    start = 0
    current_sum = 0
    count = 0

    for end in range(n):
        # end 포인터 확장 (원소 추가)
        current_sum += arr[end]

        # 합이 M 이상이면 start 포인터 이동
        while current_sum >= M:
            if current_sum == M:
                count += 1
            current_sum -= arr[start]
            start += 1

    return count


# 다른 방식 (end를 먼저 체크)
def count_subarray_sum_v2(arr: list[int], M: int) -> int:
    """더 직관적인 버전"""
    n = len(arr)
    start = 0
    end = 0
    current_sum = 0
    count = 0

    while True:
        if current_sum >= M:
            # 합이 M 이상이면 start 이동 (합 줄이기)
            current_sum -= arr[start]
            start += 1
        elif end == n:
            # 끝에 도달
            break
        else:
            # 합이 M 미만이면 end 이동 (합 늘리기)
            current_sum += arr[end]
            end += 1

        if current_sum == M:
            count += 1

    return count


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def count_subarray_sum_with_trace(arr: list[int], M: int) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"배열: {arr}")
    print(f"목표 합: M = {M}")
    print("=" * 60)

    n = len(arr)
    start = 0
    current_sum = 0
    count = 0

    print("\n[투 포인터 탐색]")

    for end in range(n):
        current_sum += arr[end]

        print(f"\nend={end}, arr[end]={arr[end]} 추가")
        print(f"  구간: [{start}, {end}] = {arr[start:end+1]}")
        print(f"  현재 합: {current_sum}")

        while current_sum >= M:
            if current_sum == M:
                print(f"  → 합 == {M}! count++ (count={count+1})")
                print(f"    부분 수열: {arr[start:end+1]}")
                count += 1

            print(f"  → 합({current_sum}) >= M({M}), start 이동")
            current_sum -= arr[start]
            start += 1
            if start <= end:
                print(f"    새 구간: [{start}, {end}] = {arr[start:end+1]}, 합={current_sum}")

    print(f"\n{'=' * 60}")
    print(f"정답: {count}")
    return count


# ================================
# 추가 예제: 가장 긴 부분 수열 (합 <= K)
# ================================

def longest_subarray_sum_at_most_k(arr: list[int], K: int) -> int:
    """
    합이 K 이하인 가장 긴 연속 부분 배열의 길이
    """
    n = len(arr)
    start = 0
    current_sum = 0
    max_length = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > K:
            current_sum -= arr[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# ================================
# 추가 예제: 두 배열 합치기 (병합 정렬 스타일)
# ================================

def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    두 정렬된 배열을 합쳐서 정렬된 배열로
    """
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # 남은 원소 추가
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("투 포인터 예제 실행")
    print("=" * 60)

    # Two Sum (정렬된 배열)
    print("\n[Two Sum - 정렬된 배열]")
    arr = [1, 2, 3, 4, 6]
    target = 6
    result = two_sum_sorted(arr, target)
    print(f"배열: {arr}, 목표: {target}")
    print(f"결과: 인덱스 {result}, 값: ({arr[result[0]]}, {arr[result[1]]})")

    # Three Sum
    print("\n[Three Sum]")
    arr = [-1, 0, 1, 2, -1, -4]
    result = three_sum(arr, 0)
    print(f"배열: {arr}, 목표: 0")
    print(f"결과: {result}")

    # 중복 제거
    print("\n[중복 제거]")
    arr = [1, 1, 2, 2, 3, 3, 3]
    original = arr.copy()
    new_length = remove_duplicates(arr)
    print(f"원본: {original}")
    print(f"결과: {arr[:new_length]}, 길이: {new_length}")

    # 0 이동
    print("\n[0을 끝으로 이동]")
    arr = [0, 1, 0, 3, 12]
    original = arr.copy()
    move_zeros(arr)
    print(f"원본: {original}")
    print(f"결과: {arr}")

    # 부분 수열 합
    print("\n" + "=" * 60)
    print("연속 부분 수열의 합")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3, 2, 5], 5),
        ([1, 1, 1, 1, 1], 2),
        ([2, 3, 4, 2, 1, 1, 1, 5], 5),
    ]

    for arr, M in test_cases:
        result = count_subarray_sum(arr, M)
        print(f"arr={arr}, M={M} → {result}개")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    count_subarray_sum_with_trace([1, 2, 3, 2, 5], 5)


"""
================================================================================
9. 투 포인터 vs 슬라이딩 윈도우
================================================================================

공통점:
- 둘 다 O(n) 시간복잡도
- 연속된 구간을 다룸

차이점:
- 투 포인터: 구간 크기가 가변적
- 슬라이딩 윈도우: 구간 크기가 고정적인 경우 많음

구분 기준:
- "길이가 K인 부분 배열" → 슬라이딩 윈도우
- "합이 K인 부분 배열" → 투 포인터


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 2003번: 수들의 합 2
- 백준 1644번: 소수의 연속합
- LeetCode 167: Two Sum II

중급:
- 백준 1806번: 부분합 (최소 길이)
- 백준 2470번: 두 용액
- LeetCode 15: 3Sum

고급:
- 백준 2230번: 수 고르기
- 백준 1484번: 다이어트
- LeetCode 42: Trapping Rain Water
================================================================================
"""
