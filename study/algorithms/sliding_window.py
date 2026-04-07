"""
================================================================================
                          슬라이딩 윈도우 (Sliding Window)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
슬라이딩 윈도우는 배열에서 일정한 "윈도우(창)"를 유지하면서
한 칸씩 이동하며 문제를 해결하는 기법입니다.

핵심 아이디어:
- 윈도우가 오른쪽으로 한 칸 이동할 때
- 왼쪽 원소 하나가 빠지고 (제거)
- 오른쪽 원소 하나가 들어옴 (추가)
- 전체를 다시 계산하지 않고 "차이"만 반영!

두 가지 유형:
1. 고정 크기 윈도우: 크기가 K로 고정
2. 가변 크기 윈도우: 조건에 따라 크기가 변함

시간복잡도:
- 브루트포스: O(n × k) 또는 O(n²)
- 슬라이딩 윈도우: O(n)

언제 사용하나?
- "길이가 K인 구간의 합/평균/최대/최소"
- "연속된 K개의 ~"
- "특정 조건을 만족하는 최소/최대 길이 부분 배열"


2. 동작 원리
--------------------------------------------------------------------------------
[고정 크기: 길이 3인 부분 배열의 최대 합]

    배열: [2, 1, 5, 1, 3, 2]
    윈도우 크기: K = 3

    브루트포스:
    [2, 1, 5] → 2+1+5 = 8
    [1, 5, 1] → 1+5+1 = 7
    [5, 1, 3] → 5+1+3 = 9
    [1, 3, 2] → 1+3+2 = 6
    → 매번 K개 더함: O(n × K)

    슬라이딩 윈도우:
    초기 윈도우: [2, 1, 5] → sum = 8

    이동 1: [1, 5, 1]
            sum = 8 - 2 + 1 = 7
            (빠지는 것 빼고, 들어오는 것 더함)

    이동 2: [5, 1, 3]
            sum = 7 - 1 + 3 = 9

    이동 3: [1, 3, 2]
            sum = 9 - 5 + 2 = 6

    → 각 이동에서 O(1): 총 O(n)


[가변 크기: 합이 7 이상인 최소 길이]

    배열: [2, 3, 1, 2, 4, 3]
    목표: 합 >= 7

    start=0, end=0, sum=0

    end 확장하며 합 증가:
    [2] sum=2 < 7
    [2,3] sum=5 < 7
    [2,3,1] sum=6 < 7
    [2,3,1,2] sum=8 >= 7! → 길이 4, start 이동

    start 이동하며 합 감소:
    [3,1,2] sum=6 < 7 → end 확장
    [3,1,2,4] sum=10 >= 7! → 길이 4, start 이동
    [1,2,4] sum=7 >= 7! → 길이 3, start 이동
    [2,4] sum=6 < 7 → end 확장
    [2,4,3] sum=9 >= 7! → 길이 3
    [4,3] sum=7 >= 7! → 길이 2!

    최소 길이: 2


3. 시간복잡도
--------------------------------------------------------------------------------
| 방법           | 시간복잡도  |
|---------------|-----------|
| 브루트포스     | O(n × k)  |
| 슬라이딩 윈도우 | O(n)      |


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

from collections import defaultdict, Counter

# ================================
# 고정 크기 윈도우
# ================================

def max_sum_subarray_fixed(arr: list[int], k: int) -> int:
    """
    길이가 k인 부분 배열 중 최대 합
    """
    n = len(arr)
    if n < k:
        return 0

    # 첫 윈도우 계산
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # 윈도우 이동
    for i in range(k, n):
        # 왼쪽 원소 빼고, 오른쪽 원소 더함
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def average_subarray_fixed(arr: list[int], k: int) -> list[float]:
    """
    길이가 k인 모든 부분 배열의 평균
    """
    n = len(arr)
    if n < k:
        return []

    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum / k)

    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]
        result.append(window_sum / k)

    return result


# ================================
# 가변 크기 윈도우
# ================================

def min_length_subarray_sum(arr: list[int], target: int) -> int:
    """
    합이 target 이상인 최소 길이 부분 배열
    없으면 0 반환
    """
    n = len(arr)
    min_length = float('inf')
    start = 0
    current_sum = 0

    for end in range(n):
        current_sum += arr[end]

        # 조건 만족하는 동안 윈도우 축소
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return min_length if min_length != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    서로 다른 문자가 최대 k개인 가장 긴 부분 문자열의 길이
    """
    char_count = defaultdict(int)
    max_length = 0
    start = 0

    for end in range(len(s)):
        char_count[s[end]] += 1

        # 서로 다른 문자가 k개 초과면 윈도우 축소
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 윈도우 내 최대/최소
def max_in_sliding_window(arr: list[int], k: int) -> list[int]:
    """
    길이 k 윈도우의 최댓값들 (deque 활용)
    """
    from collections import deque

    result = []
    dq = deque()  # 인덱스 저장 (값 내림차순 유지)

    for i in range(len(arr)):
        # 윈도우 범위 벗어난 것 제거
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # 현재 값보다 작은 것들 제거 (절대 최대가 될 수 없음)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # 윈도우 크기가 k가 되면 결과 추가
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# 패턴 2: 아나그램 찾기
def find_anagrams(s: str, p: str) -> list[int]:
    """
    문자열 s에서 p의 아나그램이 시작하는 인덱스들
    """
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    result = []

    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # 새 문자 추가
        window_count[s[i]] += 1
        # 오래된 문자 제거
        old_char = s[i - len(p)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result


"""
================================================================================
5. 대표 문제: DNA 비밀번호 (백준 12891)
================================================================================

[문제]
DNA 문자열은 A, C, G, T로만 구성됩니다.
문자열 S에서 길이가 P인 부분 문자열 중에서,
A, C, G, T의 최소 개수 조건을 만족하는 것의 개수를 구하세요.

[예시]
S = "CCTGGATTG" (길이 9)
P = 8 (부분 문자열 길이)
최소 조건: A=2개, C=1개, G=1개, T=1개

길이 8인 부분 문자열:
1. "CCTGGATT": A=1, C=2, G=1, T=3 → A 부족 (X)
2. "CTGGATTG": A=1, C=1, G=2, T=2 → A 부족 (X)

답: 0


[다른 예시]
S = "GATA" (길이 4)
P = 2
최소 조건: A=1개, C=0개, G=0개, T=0개

길이 2인 부분 문자열:
1. "GA": A=1, G=1 → 만족! (O)
2. "AT": A=1, T=1 → 만족! (O)
3. "TA": A=1, T=1 → 만족! (O)

답: 3


6. 문제 해설
--------------------------------------------------------------------------------
왜 슬라이딩 윈도우?
    - 고정 길이(P)의 부분 문자열을 확인
    - 매번 전체 문자 수를 세면 O(n × P)
    - 슬라이딩 윈도우로 O(n)

알고리즘:
    1. 첫 윈도우(0 ~ P-1)의 A,C,G,T 개수를 셈
    2. 조건 만족 여부 확인
    3. 윈도우를 한 칸씩 이동:
       - 빠지는 문자의 카운트 감소
       - 들어오는 문자의 카운트 증가
       - 조건 만족 여부 확인

최적화:
    매번 4개 문자를 모두 비교하지 않고,
    "조건을 만족하는 문자 종류 수"를 관리

동작 과정 (S = "GATA", P = 2, 조건: A>=1):

    char_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    required = {'A': 1, 'C': 0, 'G': 0, 'T': 0}

    첫 윈도우 "GA":
    char_count = {'A': 1, 'G': 1, ...}
    A >= 1? Yes! → count = 1

    이동 → "AT":
    'G' 빠짐: char_count['G'] = 0
    'T' 들어옴: char_count['T'] = 1
    char_count = {'A': 1, 'T': 1, 'G': 0, ...}
    A >= 1? Yes! → count = 2

    이동 → "TA":
    'A' 빠짐: char_count['A'] = 0
    'A' 들어옴: char_count['A'] = 1
    A >= 1? Yes! → count = 3

    답: 3


7. 코드 구현
--------------------------------------------------------------------------------
"""


def dna_password(S: str, P: int, required: dict) -> int:
    """
    DNA 비밀번호 - 슬라이딩 윈도우

    Args:
        S: DNA 문자열
        P: 부분 문자열 길이
        required: {'A': a, 'C': c, 'G': g, 'T': t} 최소 개수

    Returns:
        조건을 만족하는 부분 문자열의 개수
    """
    # 현재 윈도우의 문자 개수
    char_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    def is_valid() -> bool:
        """조건 만족 여부 확인"""
        for char in 'ACGT':
            if char_count[char] < required.get(char, 0):
                return False
        return True

    # 첫 윈도우 계산
    for i in range(P):
        char_count[S[i]] += 1

    count = 1 if is_valid() else 0

    # 윈도우 이동
    for i in range(P, len(S)):
        # 들어오는 문자
        char_count[S[i]] += 1
        # 빠지는 문자
        char_count[S[i - P]] -= 1

        if is_valid():
            count += 1

    return count


# 최적화 버전: 만족하는 조건 수를 관리
def dna_password_optimized(S: str, P: int, required: dict) -> int:
    """
    최적화 버전 - 만족 조건 수 관리
    """
    char_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    satisfied = 0  # 조건을 만족하는 문자 종류 수

    def check_satisfied(char: str, delta: int):
        """문자 개수 변화에 따른 satisfied 업데이트"""
        nonlocal satisfied
        req = required.get(char, 0)

        # 변화 전 만족 여부
        was_satisfied = char_count[char] >= req
        # 개수 변경
        char_count[char] += delta
        # 변화 후 만족 여부
        is_satisfied = char_count[char] >= req

        if was_satisfied and not is_satisfied:
            satisfied -= 1
        elif not was_satisfied and is_satisfied:
            satisfied += 1

    # 조건이 0인 것은 처음부터 만족
    for char in 'ACGT':
        if required.get(char, 0) == 0:
            satisfied += 1

    # 첫 윈도우
    for i in range(P):
        check_satisfied(S[i], 1)

    count = 1 if satisfied == 4 else 0

    # 윈도우 이동
    for i in range(P, len(S)):
        check_satisfied(S[i], 1)      # 들어오는 문자
        check_satisfied(S[i - P], -1)  # 빠지는 문자

        if satisfied == 4:
            count += 1

    return count


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def dna_password_with_trace(S: str, P: int, required: dict) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"DNA 문자열: {S}")
    print(f"부분 문자열 길이: {P}")
    print(f"최소 조건: {required}")
    print("=" * 60)

    char_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    def is_valid() -> bool:
        for char in 'ACGT':
            if char_count[char] < required.get(char, 0):
                return False
        return True

    def show_status(window: str, valid: bool):
        status = "O" if valid else "X"
        counts = f"A={char_count['A']}, C={char_count['C']}, G={char_count['G']}, T={char_count['T']}"
        print(f'  "{window}" → {counts} → {status}')

    # 첫 윈도우
    for i in range(P):
        char_count[S[i]] += 1

    count = 0
    print(f"\n[윈도우 탐색]")

    window = S[:P]
    valid = is_valid()
    if valid:
        count += 1
    show_status(window, valid)

    # 윈도우 이동
    for i in range(P, len(S)):
        out_char = S[i - P]
        in_char = S[i]

        char_count[in_char] += 1
        char_count[out_char] -= 1

        window = S[i - P + 1:i + 1]
        valid = is_valid()
        if valid:
            count += 1
        show_status(window, valid)

    print(f"\n{'=' * 60}")
    print(f"정답: {count}")
    return count


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("슬라이딩 윈도우 예제 실행")
    print("=" * 60)

    # 고정 크기: 최대 합
    print("\n[고정 크기 - 최대 합]")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sum_subarray_fixed(arr, k)
    print(f"배열: {arr}, k={k}")
    print(f"최대 합: {result}")

    # 고정 크기: 평균
    print("\n[고정 크기 - 평균]")
    result = average_subarray_fixed(arr, k)
    print(f"각 윈도우 평균: {result}")

    # 가변 크기: 최소 길이
    print("\n[가변 크기 - 최소 길이]")
    arr = [2, 3, 1, 2, 4, 3]
    target = 7
    result = min_length_subarray_sum(arr, target)
    print(f"배열: {arr}, 목표 합: {target}")
    print(f"최소 길이: {result}")

    # 아나그램 찾기
    print("\n[아나그램 찾기]")
    s, p = "cbaebabacd", "abc"
    result = find_anagrams(s, p)
    print(f"s: {s}, p: {p}")
    print(f"아나그램 시작 위치: {result}")

    # 슬라이딩 윈도우 최대값
    print("\n[슬라이딩 윈도우 최대값]")
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = max_in_sliding_window(arr, k)
    print(f"배열: {arr}, k={k}")
    print(f"각 윈도우 최대: {result}")

    # DNA 비밀번호
    print("\n" + "=" * 60)
    print("DNA 비밀번호")
    print("=" * 60)

    # 테스트 1
    S = "GATA"
    P = 2
    required = {'A': 1, 'C': 0, 'G': 0, 'T': 0}
    result = dna_password(S, P, required)
    print(f"\nS={S}, P={P}, 조건={required}")
    print(f"결과: {result}")

    # 테스트 2
    S = "CCTGGATTG"
    P = 8
    required = {'A': 2, 'C': 1, 'G': 1, 'T': 1}
    result = dna_password(S, P, required)
    print(f"\nS={S}, P={P}, 조건={required}")
    print(f"결과: {result}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    dna_password_with_trace("GATA", 2, {'A': 1, 'C': 0, 'G': 0, 'T': 0})


"""
================================================================================
9. 슬라이딩 윈도우 패턴 정리
================================================================================

[고정 크기]
for i in range(k, n):
    # 빠지는 것 처리: arr[i-k]
    # 들어오는 것 처리: arr[i]
    # 결과 업데이트

[가변 크기]
for end in range(n):
    # end 확장 (원소 추가)
    while 조건 만족:
        # 결과 업데이트
        # start 축소 (원소 제거)


================================================================================
10. 연습 문제 추천
================================================================================

고정 크기:
- 백준 12891번: DNA 비밀번호
- 백준 2559번: 수열
- LeetCode 643: Maximum Average Subarray I

가변 크기:
- 백준 1806번: 부분합
- LeetCode 3: Longest Substring Without Repeating Characters
- LeetCode 76: Minimum Window Substring

고급:
- 백준 11003번: 최솟값 찾기 (deque)
- LeetCode 239: Sliding Window Maximum
- LeetCode 438: Find All Anagrams in a String
================================================================================
"""
