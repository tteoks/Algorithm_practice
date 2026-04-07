"""
================================================================================
                              그리디 (Greedy)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
그리디 알고리즘은 "현재 상황에서 가장 좋아 보이는 선택"을 하는 방법입니다.
매 순간 최적의 선택을 하면 전체적으로도 최적이 될 것이라는 가정.

핵심 특징:
- 현재 선택이 이후 선택에 영향을 주지 않음
- 부분 최적해가 전체 최적해가 됨
- 한번 선택하면 번복하지 않음

그리디가 되는 조건:
1. 탐욕적 선택 속성: 지금 최선의 선택이 전체 최선으로 이어짐
2. 최적 부분 구조: 부분 문제의 최적해가 전체 최적해에 포함됨

주의! 그리디가 항상 정답은 아님:
    - 반례가 없는지 꼭 확인해야 함
    - 안 되면 DP나 완전탐색을 고려


2. 동작 원리
--------------------------------------------------------------------------------

[거스름돈 문제 예시]
    800원을 거슬러 줄 때, 동전 개수를 최소화하려면?
    동전: 500원, 100원, 50원, 10원

    그리디 접근:
    1. 가장 큰 동전부터 최대한 사용!
    2. 500원 → 1개 (남은 돈: 300원)
    3. 100원 → 3개 (남은 돈: 0원)
    4. 총 4개

    이 경우 그리디가 최적해를 보장함
    (단, 동전이 배수 관계일 때만! 예: 400원짜리가 있으면 안 됨)


[그리디가 안 되는 예]
    동전: 500원, 400원, 100원
    800원 거스름돈

    그리디: 500 + 100 + 100 + 100 = 4개
    최적해: 400 + 400 = 2개!

    → 이 경우는 DP로 풀어야 함


3. 그리디 문제 패턴
--------------------------------------------------------------------------------

[패턴 1] 정렬 후 선택
    - 대부분의 그리디 문제는 정렬이 핵심!
    - 예: 회의실 배정, 체육복

[패턴 2] 큰 것/작은 것 먼저
    - 거스름돈, 배낭 문제(분할 가능)

[패턴 3] 조건을 만족하는 최소/최대
    - 구명보트, 단속카메라


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

# ================================
# 거스름돈 문제
# ================================

def min_coins(money: int, coins: list[int]) -> int:
    """
    거스름돈을 줄 때 필요한 최소 동전 개수

    Args:
        money: 거슬러 줄 금액
        coins: 동전 종류 (배수 관계일 때만 그리디 가능)

    Returns:
        최소 동전 개수
    """
    coins.sort(reverse=True)  # 큰 동전부터
    count = 0

    for coin in coins:
        count += money // coin
        money %= coin

    return count


# ================================
# 활동 선택 문제 (회의실 배정)
# ================================

def max_meetings(meetings: list[tuple[int, int]]) -> int:
    """
    겹치지 않게 최대한 많은 회의 배정

    Args:
        meetings: [(시작시간, 종료시간), ...]

    Returns:
        최대 회의 수
    """
    # 종료 시간 기준 정렬 (핵심!)
    meetings.sort(key=lambda x: x[1])

    count = 0
    last_end = 0

    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    return count


# ================================
# 분할 가능 배낭 문제
# ================================

def fractional_knapsack(capacity: int, items: list[tuple[int, int]]) -> float:
    """
    배낭에 물건을 담아 최대 가치 얻기 (물건을 쪼갤 수 있음)

    Args:
        capacity: 배낭 용량
        items: [(무게, 가치), ...]

    Returns:
        최대 가치
    """
    # 무게 대비 가치 (가성비) 기준 정렬
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for weight, value in items:
        if capacity >= weight:
            # 물건 전체를 담음
            capacity -= weight
            total_value += value
        else:
            # 물건의 일부만 담음
            total_value += value * (capacity / weight)
            break

    return total_value


"""
================================================================================
5. 대표 문제: 회의실 배정
================================================================================

[문제]
N개의 회의가 있고, 각 회의의 시작 시간과 종료 시간이 주어집니다.
한 회의실에서 겹치지 않게 최대한 많은 회의를 진행하려면
몇 개의 회의를 할 수 있나요?

[제약]
- 회의가 끝나는 즉시 다음 회의 시작 가능 (종료시간 == 시작시간 OK)

[예시]
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4

선택된 회의: (1,4) → (5,7) → (8,11) → (12,14)


6. 문제 해설
--------------------------------------------------------------------------------
왜 종료 시간 기준으로 정렬하나?

    목표: 최대한 많은 회의
    전략: 빨리 끝나는 회의부터 선택!

    빨리 끝나면 → 남는 시간이 많음 → 더 많은 회의 가능

    만약 시작 시간 기준으로 정렬하면?
        (0, 100)이 먼저 선택될 수 있음
        → 너무 긴 회의로 인해 다른 회의 못 함!


동작 과정:

    입력: [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]

    종료시간 기준 정렬:
    [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]

    시간표:
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
    |--|--|--|--|--|--|--|--|--|--|--|--|--|--|

    탐색 과정 (last_end = 0):

    (1, 4): start(1) >= last_end(0)? Yes!
            → 선택! last_end = 4, count = 1

    (3, 5): start(3) >= last_end(4)? No (3 < 4)
            → 패스

    (0, 6): start(0) >= last_end(4)? No
            → 패스

    (5, 7): start(5) >= last_end(4)? Yes!
            → 선택! last_end = 7, count = 2

    (3, 8): start(3) >= last_end(7)? No
            → 패스

    (5, 9): start(5) >= last_end(7)? No
            → 패스

    (6, 10): start(6) >= last_end(7)? No
             → 패스

    (8, 11): start(8) >= last_end(7)? Yes!
             → 선택! last_end = 11, count = 3

    (8, 12): start(8) >= last_end(11)? No
             → 패스

    (2, 13): start(2) >= last_end(11)? No
             → 패스

    (12, 14): start(12) >= last_end(11)? Yes!
              → 선택! last_end = 14, count = 4

    결과: 4개 [(1,4), (5,7), (8,11), (12,14)]


7. 코드 구현
--------------------------------------------------------------------------------
"""


def meeting_room(meetings: list[tuple[int, int]]) -> int:
    """
    회의실 배정 - 최대 회의 수

    Args:
        meetings: [(시작시간, 종료시간), ...] 리스트

    Returns:
        겹치지 않게 선택할 수 있는 최대 회의 수
    """
    # 종료 시간 기준 정렬
    # 종료 시간이 같으면 시작 시간 기준 (예외 처리)
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end = 0

    for start, end in meetings:
        # 이전 회의가 끝난 후에 시작하는 회의만 선택
        if start >= last_end:
            count += 1
            last_end = end

    return count


def meeting_room_with_list(meetings: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    선택된 회의 목록도 반환
    """
    meetings.sort(key=lambda x: (x[1], x[0]))

    selected = []
    last_end = 0

    for start, end in meetings:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def meeting_room_with_trace(meetings: list[tuple[int, int]]) -> int:
    """동작 과정을 출력하면서 실행"""
    print(f"입력: {meetings}")
    print("=" * 60)

    # 정렬
    meetings_sorted = sorted(meetings, key=lambda x: (x[1], x[0]))
    print(f"종료시간 기준 정렬: {meetings_sorted}")

    # 타임라인 시각화
    max_time = max(end for _, end in meetings)
    print(f"\n시간표 (0 ~ {max_time}):")
    print("  " + "".join(f"{i:3}" for i in range(max_time + 1)))

    print("\n[탐색 과정]")
    count = 0
    last_end = 0
    selected = []

    for i, (start, end) in enumerate(meetings_sorted):
        print(f"\n회의 {i+1}: ({start}, {end})")
        print(f"  조건: start({start}) >= last_end({last_end})?", end=" ")

        if start >= last_end:
            print(f"Yes! → 선택")
            count += 1
            last_end = end
            selected.append((start, end))
            print(f"  → last_end = {last_end}, count = {count}")
        else:
            print(f"No → 패스 (겹침)")

    print(f"\n{'=' * 60}")
    print(f"선택된 회의: {selected}")
    print(f"최대 회의 수: {count}")

    # 시각적 표현
    print(f"\n선택된 회의 시간표:")
    for start, end in selected:
        timeline = ["."] * (max_time + 1)
        for t in range(start, end):
            timeline[t] = "#"
        print(f"  ({start:2},{end:2}): {''.join(timeline)}")

    return count


# ================================
# 추가 그리디 문제들
# ================================

def rescue_boat(people: list[int], limit: int) -> int:
    """
    구명보트 문제: 최대 2명, 무게 제한 있음
    최소 보트 수 구하기
    """
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # 가장 무거운 사람은 무조건 태움
        if people[left] + people[right] <= limit:
            # 가장 가벼운 사람도 함께 태움
            left += 1
        right -= 1
        boats += 1

    return boats


def gym_clothes(n: int, lost: list[int], reserve: list[int]) -> int:
    """
    체육복 문제: 여벌이 있는 학생이 앞뒤 번호에게 빌려줄 수 있음
    수업을 들을 수 있는 최대 학생 수
    """
    # 여벌이 있는데 도난당한 학생 처리
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for r in sorted(reserve_set):
        # 앞 번호 먼저 확인 (그리디)
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("그리디 예제 실행")
    print("=" * 60)

    # 거스름돈
    print("\n[거스름돈 문제]")
    coins = [500, 100, 50, 10]
    money = 1260
    result = min_coins(money, coins.copy())
    print(f"{money}원을 {coins}로 거슬러 줄 때: {result}개")

    # 구명보트
    print("\n[구명보트 문제]")
    people = [70, 50, 80, 50]
    limit = 100
    result = rescue_boat(people.copy(), limit)
    print(f"사람들: {people}, 제한: {limit}kg → 보트 {result}개")

    # 회의실 배정
    print("\n" + "=" * 60)
    print("회의실 배정 문제")
    print("=" * 60)

    meetings = [
        (1, 4), (3, 5), (0, 6), (5, 7), (3, 8),
        (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)
    ]

    result = meeting_room(meetings.copy())
    print(f"최대 회의 수: {result}")

    selected = meeting_room_with_list(meetings.copy())
    print(f"선택된 회의: {selected}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)

    small_meetings = [(1, 3), (2, 4), (3, 5), (4, 6)]
    meeting_room_with_trace(small_meetings)


"""
================================================================================
9. 그리디 vs DP 선택 가이드
================================================================================

[그리디 사용]
- 현재 선택이 이후에 영향 없음
- 매 순간 최선의 선택 = 전체 최선
- 반례가 없음

[DP 사용]
- 현재 선택이 이후 선택에 영향
- 여러 선택지를 비교해야 함
- 그리디로 반례가 존재


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- 백준 11047번: 동전 0 (거스름돈)
- 백준 1931번: 회의실 배정
- 프로그래머스: 체육복

중급:
- 백준 11399번: ATM
- 백준 1541번: 잃어버린 괄호
- 프로그래머스: 구명보트
- 프로그래머스: 큰 수 만들기

고급:
- 백준 1744번: 수 묶기
- 백준 2457번: 공주님의 정원
- 프로그래머스: 단속카메라
================================================================================
"""
