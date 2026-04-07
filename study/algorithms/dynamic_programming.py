"""
================================================================================
                       동적 프로그래밍 (Dynamic Programming, DP)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
DP는 큰 문제를 작은 부분 문제로 나누어 해결하는 방법입니다.
한 번 계산한 결과를 저장(메모이제이션)해서 중복 계산을 피합니다.

핵심 특징:
- 최적 부분 구조: 부분 문제의 최적해로 전체 최적해 구성
- 중복 부분 문제: 같은 부분 문제가 여러 번 등장
- 메모이제이션: 계산 결과를 저장해서 재사용

DP vs 그리디:
- 그리디: 현재 최선만 고려 (되돌아가지 않음)
- DP: 모든 경우를 고려 (저장해두고 비교)

DP 접근법:
- Top-down (하향식): 재귀 + 메모이제이션
- Bottom-up (상향식): 반복문 + 테이블


2. 동작 원리
--------------------------------------------------------------------------------
[피보나치 수열로 이해하기]

일반 재귀:
    fib(5)
    ├── fib(4)
    │   ├── fib(3)
    │   │   ├── fib(2)
    │   │   └── fib(1)
    │   └── fib(2)
    └── fib(3)
        ├── fib(2)
        └── fib(1)

    → fib(3)이 2번, fib(2)가 3번 계산됨 (중복!)
    → 시간복잡도: O(2^n) - 매우 느림

DP (메모이제이션):
    memo = {}
    fib(5) 계산 시:
    1. fib(1) = 1, fib(2) = 1 저장
    2. fib(3) = fib(2) + fib(1) = 2 저장
    3. fib(4) = fib(3) + fib(2) = 3 저장
    4. fib(5) = fib(4) + fib(3) = 5 저장

    → 각 값을 한 번만 계산!
    → 시간복잡도: O(n)


3. DP 문제 풀이 단계
--------------------------------------------------------------------------------
1. 상태 정의: dp[i]가 무엇을 의미하는지 정의
2. 점화식 도출: dp[i]를 이전 값들로 표현
3. 초기값 설정: dp[0], dp[1] 등 기저 조건
4. 계산 순서 결정: 어떤 순서로 채울지 (보통 작은 것부터)
5. 정답 도출: dp 테이블에서 정답 위치 확인


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

from functools import lru_cache

# ================================
# 피보나치 - 여러 방식 비교
# ================================

# 방식 1: 일반 재귀 (느림 - O(2^n))
def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 방식 2: Top-down (메모이제이션)
def fib_top_down(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]


# 방식 3: Top-down (lru_cache 사용 - 가장 간편!)
@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


# 방식 4: Bottom-up (반복문)
def fib_bottom_up(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 방식 5: Bottom-up (공간 최적화)
def fib_optimized(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# ================================
# DP 기본 패턴들
# ================================

# 패턴 1: 1차원 DP (계단 오르기)
def climb_stairs(n: int) -> int:
    """n개의 계단을 1칸 또는 2칸씩 오를 때 경우의 수"""
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 패턴 2: 2차원 DP (격자 경로)
def unique_paths(m: int, n: int) -> int:
    """m x n 격자에서 (0,0)에서 (m-1,n-1)까지 가는 경로 수"""
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


# 패턴 3: 최대/최소 DP
def max_subarray(nums: list[int]) -> int:
    """최대 부분합 (카데인 알고리즘)"""
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)


"""
================================================================================
5. 대표 문제: 동전 거스름돈 (Coin Change)
================================================================================

[문제]
동전의 종류가 주어집니다.
금액 amount를 만들기 위해 필요한 최소 동전 개수를 구하세요.
만들 수 없으면 -1을 반환합니다.

[제약]
- 각 동전은 무한히 사용 가능
- 동전 종류는 배수 관계가 아닐 수 있음 (그리디 불가!)

[예시]
Input: coins = [1, 2, 5], amount = 11
Output: 3
설명: 5 + 5 + 1 = 11 (3개)

Input: coins = [2], amount = 3
Output: -1
설명: 3을 만들 수 없음


6. 문제 해설
--------------------------------------------------------------------------------
왜 그리디가 안 되나?

    coins = [1, 3, 4], amount = 6
    그리디: 4 + 1 + 1 = 3개
    최적해: 3 + 3 = 2개!

DP 접근:
    dp[i] = 금액 i를 만드는 최소 동전 개수

점화식:
    dp[i] = min(dp[i - coin] + 1) for each coin
    → "coin을 하나 쓰고, 나머지 금액(i - coin)의 최소 개수 + 1"

동작 과정 (coins = [1, 2, 5], amount = 11):

    초기화: dp = [0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                 0   1    2    3    4    5    6    7    8    9   10   11

    금액 1 (coins: 1)
        dp[1] = dp[1-1] + 1 = dp[0] + 1 = 1
        dp = [0, 1, INF, ...]

    금액 2 (coins: 1, 2)
        dp[2] = min(dp[2-1]+1, dp[2-2]+1) = min(2, 1) = 1
        dp = [0, 1, 1, INF, ...]

    금액 3 (coins: 1, 2)
        dp[3] = min(dp[2]+1, dp[1]+1) = min(2, 2) = 2
        dp = [0, 1, 1, 2, ...]

    금액 5 (coins: 1, 2, 5)
        dp[5] = min(dp[4]+1, dp[3]+1, dp[0]+1) = min(3, 3, 1) = 1
        dp = [0, 1, 1, 2, 2, 1, ...]

    ... 계속 진행 ...

    최종: dp[11] = 3 (5 + 5 + 1)


7. 코드 구현
--------------------------------------------------------------------------------
"""


def coin_change(coins: list[int], amount: int) -> int:
    """
    동전 거스름돈 - 최소 동전 개수

    Args:
        coins: 동전 종류 리스트
        amount: 목표 금액

    Returns:
        최소 동전 개수, 불가능하면 -1
    """
    # dp[i] = 금액 i를 만드는 최소 동전 개수
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0  # 0원은 동전 0개

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != INF:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1


# 더 직관적인 버전
def coin_change_v2(coins: list[int], amount: int) -> int:
    """동전별로 업데이트하는 버전"""
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def coin_change_with_trace(coins: list[int], amount: int) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"동전: {coins}")
    print(f"목표 금액: {amount}")
    print("=" * 60)

    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0
    used = [[] for _ in range(amount + 1)]  # 사용한 동전 추적

    print("\n[DP 테이블 채우기]")

    for i in range(1, amount + 1):
        print(f"\n금액 {i}:")
        for coin in coins:
            if coin <= i and dp[i - coin] != INF:
                new_count = dp[i - coin] + 1
                print(f"  동전 {coin} 사용 시: dp[{i}-{coin}] + 1 = dp[{i-coin}] + 1 = {dp[i-coin]} + 1 = {new_count}", end="")
                if new_count < dp[i]:
                    dp[i] = new_count
                    used[i] = used[i - coin] + [coin]
                    print(" → 갱신!")
                else:
                    print(" → 패스")

        if dp[i] == INF:
            print(f"  → dp[{i}] = INF (불가능)")
        else:
            print(f"  → dp[{i}] = {dp[i]}, 사용 동전: {used[i]}")

    print(f"\n{'=' * 60}")
    print(f"최종 DP 테이블:")
    for i in range(min(amount + 1, 15)):
        val = dp[i] if dp[i] != INF else "X"
        print(f"  dp[{i}] = {val}")
    if amount >= 15:
        print(f"  ...")
        print(f"  dp[{amount}] = {dp[amount] if dp[amount] != INF else 'X'}")

    if dp[amount] != INF:
        print(f"\n정답: {dp[amount]}개")
        print(f"사용한 동전: {used[amount]}")
    else:
        print(f"\n정답: -1 (불가능)")

    return dp[amount] if dp[amount] != INF else -1


# ================================
# 추가 예제: 0/1 배낭 문제
# ================================

def knapsack_01(capacity: int, weights: list[int], values: list[int]) -> int:
    """
    0/1 배낭 문제: 물건을 쪼갤 수 없음

    Args:
        capacity: 배낭 용량
        weights: 물건별 무게
        values: 물건별 가치

    Returns:
        최대 가치
    """
    n = len(weights)
    # dp[i][w] = i번째 물건까지 고려, 용량 w일 때 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # 현재 물건을 안 넣는 경우
            dp[i][w] = dp[i - 1][w]
            # 현재 물건을 넣는 경우
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]


# ================================
# 추가 예제: LCS (최장 공통 부분 수열)
# ================================

def lcs(s1: str, s2: str) -> int:
    """
    Longest Common Subsequence

    예: "ABCDE"와 "ACE" → LCS = "ACE" (길이 3)
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("동적 프로그래밍 예제 실행")
    print("=" * 60)

    # 피보나치 비교
    print("\n[피보나치 - 여러 방식]")
    n = 10
    print(f"fib({n}) = {fib_bottom_up(n)}")

    # 계단 오르기
    print("\n[계단 오르기]")
    for n in [3, 4, 5]:
        print(f"계단 {n}개: {climb_stairs(n)}가지")

    # 동전 거스름돈
    print("\n" + "=" * 60)
    print("동전 거스름돈 문제")
    print("=" * 60)

    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1, 3, 4], 6),
    ]

    for coins, amount in test_cases:
        result = coin_change(coins, amount)
        print(f"coins={coins}, amount={amount} → {result}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    coin_change_with_trace([1, 2, 5], 7)

    # 배낭 문제
    print("\n" + "=" * 60)
    print("0/1 배낭 문제")
    print("=" * 60)
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    result = knapsack_01(capacity, weights, values)
    print(f"무게: {weights}, 가치: {values}, 용량: {capacity}")
    print(f"최대 가치: {result}")


"""
================================================================================
9. DP 문제 유형 정리
================================================================================

[1차원 DP]
- 피보나치, 계단 오르기
- 최대 부분합

[2차원 DP]
- 격자 경로
- LCS, LIS
- 배낭 문제

[구간 DP]
- 행렬 곱셈
- 팰린드롬 분할

[트리 DP]
- 트리의 독립 집합


================================================================================
10. 연습 문제 추천
================================================================================

1차원 DP:
- 백준 1003번: 피보나치 함수
- 백준 9095번: 1, 2, 3 더하기
- 백준 11726번: 2×n 타일링

2차원 DP:
- 백준 11053번: 가장 긴 증가하는 부분 수열 (LIS)
- 백준 9251번: LCS
- 백준 12865번: 평범한 배낭

응용:
- 프로그래머스: N으로 표현
- 프로그래머스: 정수 삼각형
- 백준 2156번: 포도주 시식
================================================================================
"""
