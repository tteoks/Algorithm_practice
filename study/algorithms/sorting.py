"""
================================================================================
                              정렬 (Sorting)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
정렬은 데이터를 특정 순서대로 나열하는 것입니다.
코딩 테스트에서는 직접 구현보다 "언제, 어떻게 쓰는지"가 더 중요합니다!

파이썬에서는 sort()와 sorted()를 사용:
- list.sort(): 원본 리스트를 정렬 (in-place)
- sorted(list): 새 리스트를 반환 (원본 유지)

코딩 테스트 핵심:
1. 기본 정렬
2. 커스텀 정렬 (key 함수)
3. 다중 조건 정렬
4. 안정 정렬 (Stable Sort) 이해


2. 정렬 알고리즘 종류와 시간복잡도
--------------------------------------------------------------------------------
| 알고리즘      | 평균       | 최악       | 공간    | 안정성 |
|--------------|-----------|-----------|--------|-------|
| 버블 정렬     | O(n²)     | O(n²)     | O(1)   | 안정   |
| 선택 정렬     | O(n²)     | O(n²)     | O(1)   | 불안정 |
| 삽입 정렬     | O(n²)     | O(n²)     | O(1)   | 안정   |
| 병합 정렬     | O(n log n)| O(n log n)| O(n)   | 안정   |
| 퀵 정렬       | O(n log n)| O(n²)     | O(log n)| 불안정 |
| 힙 정렬       | O(n log n)| O(n log n)| O(1)   | 불안정 |
| 팀소트 (Python)| O(n log n)| O(n log n)| O(n)  | 안정   |

* 파이썬의 sort()는 팀소트(Timsort)로 구현되어 있음


3. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

# ================================
# 기본 정렬
# ================================

# 오름차순
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# 내림차순
arr.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# 원본 유지하고 새 리스트
arr = [3, 1, 4, 1, 5]
sorted_arr = sorted(arr)  # arr는 그대로, sorted_arr는 정렬됨


# ================================
# 커스텀 정렬 (key 함수)
# ================================

# 절대값 기준 정렬
arr = [-5, 2, -3, 1, 4]
arr.sort(key=abs)  # [1, 2, -3, 4, -5]

# 문자열 길이 기준 정렬
words = ["banana", "pie", "apple", "hi"]
words.sort(key=len)  # ['hi', 'pie', 'apple', 'banana']

# 튜플의 특정 요소 기준 정렬
students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
students.sort(key=lambda x: x[1])  # 점수 기준
# [('Bob', 85), ('Alice', 90), ('Charlie', 90)]


# ================================
# 다중 조건 정렬 (중요!)
# ================================

# 방법 1: 튜플 반환 (가장 많이 사용)
students = [("Alice", 90), ("Bob", 85), ("Charlie", 90), ("David", 85)]

# 점수 내림차순, 점수 같으면 이름 오름차순
students.sort(key=lambda x: (-x[1], x[0]))
# [('Alice', 90), ('Charlie', 90), ('Bob', 85), ('David', 85)]

# 방법 2: operator.itemgetter
from operator import itemgetter

# 1번 인덱스(점수) 기준 정렬
students.sort(key=itemgetter(1))


# ================================
# 안정 정렬 (Stable Sort) 이해
# ================================

"""
안정 정렬: 같은 값을 가진 요소들의 상대적 순서가 유지됨

예시:
    원본: [(A, 2), (B, 1), (C, 2)]
    2번째 요소 기준 정렬:

    안정 정렬 결과:   [(B, 1), (A, 2), (C, 2)]  ← A가 C 앞에 (원래 순서 유지)
    불안정 정렬 결과: [(B, 1), (C, 2), (A, 2)]  ← 순서 바뀔 수 있음

파이썬의 sort()는 안정 정렬!
→ 다중 조건 정렬 시, 여러 번 정렬해도 됨
"""


# ================================
# 자주 쓰는 정렬 패턴
# ================================

# 패턴 1: 인덱스와 함께 정렬
arr = [40, 10, 30, 20]
indexed = [(val, i) for i, val in enumerate(arr)]
indexed.sort()  # [(10, 1), (20, 3), (30, 2), (40, 0)]

# 패턴 2: 사전 순서 정렬 (문자열)
words = ["apple", "Apply", "banana"]
words.sort()  # 대문자가 먼저: ['Apply', 'apple', 'banana']
words.sort(key=str.lower)  # 대소문자 무시: ['apple', 'Apply', 'banana']

# 패턴 3: 숫자 문자열 정렬
nums = ["10", "2", "1", "20"]
nums.sort()  # 문자열 순서: ['1', '10', '2', '20']
nums.sort(key=int)  # 숫자 순서: ['1', '2', '10', '20']


"""
================================================================================
4. 대표 문제: 가장 큰 수
================================================================================

[문제]
0 또는 양의 정수가 주어집니다.
정수를 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 return 하세요.

[예시]
Input: [6, 10, 2]
Output: "6210"

Input: [3, 30, 34, 5, 9]
Output: "9534330"


5. 문제 해설
--------------------------------------------------------------------------------
왜 단순 정렬이 안 될까?

    [6, 10, 2]를 내림차순 정렬하면?
    → [10, 6, 2] → "1062"

    하지만 정답은 "6210"!
    → 6을 10보다 앞에 놓는 게 더 큼

핵심 아이디어:
    두 수 A, B를 비교할 때,
    "AB"와 "BA" 중 더 큰 쪽이 앞에 오도록 정렬!

    예: 6 vs 10
    "610" vs "106"
    610 > 106 이므로 6이 10보다 앞에!

동작 과정 ([3, 30, 34, 5, 9]):

    비교 예시:
    - 3 vs 30: "330" vs "303" → 330 > 303 → 3이 앞
    - 3 vs 34: "334" vs "343" → 343 > 334 → 34가 앞
    - 34 vs 30: "3430" vs "3034" → 3430 > 3034 → 34가 앞

    정렬 결과: [9, 5, 34, 3, 30]
    이어붙이기: "9534330"


6. 코드 구현
--------------------------------------------------------------------------------
"""

from functools import cmp_to_key


def largest_number(numbers: list[int]) -> str:
    """
    가장 큰 수 만들기

    Args:
        numbers: 0 이상의 정수 리스트

    Returns:
        이어붙여서 만든 가장 큰 수 (문자열)
    """
    # 숫자를 문자열로 변환
    str_nums = [str(n) for n in numbers]

    # 커스텀 비교 함수
    # A+B > B+A 이면 A가 앞에 와야 함
    def compare(a, b):
        if a + b > b + a:
            return -1  # a가 앞
        elif a + b < b + a:
            return 1   # b가 앞
        else:
            return 0

    # 정렬
    str_nums.sort(key=cmp_to_key(compare))

    # 이어붙이기
    result = "".join(str_nums)

    # 예외 처리: 모두 0인 경우 ("000" → "0")
    return "0" if result[0] == "0" else result


# 더 간단한 방법 (트릭)
def largest_number_simple(numbers: list[int]) -> str:
    """
    트릭: 문자열을 3번 반복해서 비교

    "3"  → "333"
    "30" → "303030"
    "34" → "343434"

    "333" > "343434" > "303030"
    따라서: 34 > 3 > 30

    * 왜 3번? 숫자가 최대 1000이므로 4자리.
      4자리 * 3 = 12자리로 비교하면 안전.
    """
    str_nums = [str(n) for n in numbers]
    str_nums.sort(key=lambda x: x * 3, reverse=True)

    result = "".join(str_nums)
    return "0" if result[0] == "0" else result


"""
7. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def largest_number_with_trace(numbers: list[int]) -> str:
    """동작 과정을 출력하면서 실행"""
    print(f"입력: {numbers}")
    print("=" * 50)

    str_nums = [str(n) for n in numbers]
    print(f"문자열 변환: {str_nums}")

    print("\n[비교 과정]")
    comparisons = []

    for i in range(len(str_nums)):
        for j in range(i + 1, len(str_nums)):
            a, b = str_nums[i], str_nums[j]
            ab, ba = a + b, b + a
            if ab > ba:
                result = f"{a} > {b}"
            elif ab < ba:
                result = f"{b} > {a}"
            else:
                result = f"{a} = {b}"
            print(f"  {a} vs {b}: \"{ab}\" vs \"{ba}\" → {result}")

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    str_nums.sort(key=cmp_to_key(compare))

    print(f"\n정렬 결과: {str_nums}")

    result = "".join(str_nums)
    result = "0" if result[0] == "0" else result

    print(f"최종 답: {result}")
    return result


# ================================
# 기본 정렬 알고리즘 구현 (참고용)
# ================================

def bubble_sort(arr: list) -> list:
    """버블 정렬 - O(n²)"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr: list) -> list:
    """선택 정렬 - O(n²)"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: list) -> list:
    """삽입 정렬 - O(n²)"""
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr: list) -> list:
    """퀵 정렬 - O(n log n) 평균"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: list) -> list:
    """병합 정렬 - O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 병합
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("정렬 예제 실행")
    print("=" * 60)

    # 기본 정렬 테스트
    print("\n[기본 정렬]")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"원본: {arr}")
    print(f"버블 정렬: {bubble_sort(arr)}")
    print(f"선택 정렬: {selection_sort(arr)}")
    print(f"삽입 정렬: {insertion_sort(arr)}")
    print(f"퀵 정렬: {quick_sort(arr)}")
    print(f"병합 정렬: {merge_sort(arr)}")

    # 커스텀 정렬 테스트
    print("\n[커스텀 정렬]")
    students = [("Alice", 90), ("Bob", 85), ("Charlie", 90), ("David", 85)]
    print(f"원본: {students}")
    students_sorted = sorted(students, key=lambda x: (-x[1], x[0]))
    print(f"점수 내림차순, 이름 오름차순: {students_sorted}")

    # 가장 큰 수 테스트
    print("\n" + "=" * 60)
    print("가장 큰 수 문제")
    print("=" * 60)

    test_cases = [
        [6, 10, 2],
        [3, 30, 34, 5, 9],
        [0, 0, 0],
    ]

    for nums in test_cases:
        result = largest_number(nums)
        print(f"{nums} → \"{result}\"")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    largest_number_with_trace([3, 30, 34, 5, 9])


"""
================================================================================
8. 연습 문제 추천
================================================================================

기초:
- 백준 2750번: 수 정렬하기
- 백준 2751번: 수 정렬하기 2 (O(n log n) 필요)

커스텀 정렬:
- 백준 1181번: 단어 정렬 (길이순, 사전순)
- 백준 10814번: 나이순 정렬 (안정 정렬)
- 프로그래머스: 가장 큰 수
- 프로그래머스: H-Index

응용:
- 백준 11650번: 좌표 정렬하기
- 백준 11651번: 좌표 정렬하기 2
- 백준 1931번: 회의실 배정 (정렬 + 그리디)
================================================================================
"""
