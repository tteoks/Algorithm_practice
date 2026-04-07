"""
================================================================================
                              해시 (Hash)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
해시(Hash)는 키(Key)를 값(Value)에 매핑하는 자료구조입니다.
Python에서는 딕셔너리(dict)가 해시 테이블로 구현되어 있습니다.

핵심 특징:
- 검색, 삽입, 삭제가 평균 O(1) 시간복잡도
- 키를 통해 값에 즉시 접근 가능
- 순서가 보장되지 않음 (Python 3.7+부터는 삽입 순서 유지)

언제 사용하나?
- 빠른 검색이 필요할 때
- 중복을 체크할 때
- 데이터를 카운팅할 때
- 두 데이터 간의 매핑이 필요할 때


2. 동작 원리
--------------------------------------------------------------------------------
해시 함수가 키를 받아서 배열의 인덱스(해시값)로 변환합니다.

[키] → [해시 함수] → [해시값(인덱스)] → [값 저장/조회]

예시:
    "apple" → hash("apple") → 3 → 배열[3]에 저장
    "banana" → hash("banana") → 7 → 배열[7]에 저장

충돌(Collision): 서로 다른 키가 같은 해시값을 가질 때
    → 체이닝(Chaining) 또는 개방 주소법으로 해결


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산      | 평균     | 최악     |
|----------|---------|---------|
| 검색      | O(1)    | O(n)    |
| 삽입      | O(1)    | O(n)    |
| 삭제      | O(1)    | O(n)    |

* 최악의 경우는 모든 키가 충돌할 때 (거의 발생하지 않음)


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

# ================================
# 기본 사용법
# ================================

# 1) 딕셔너리 생성
hash_map = {}
hash_map = dict()

# 2) 값 추가/수정
hash_map["key1"] = "value1"
hash_map["key2"] = "value2"

# 3) 값 조회
value = hash_map["key1"]  # "value1"
value = hash_map.get("key3", "default")  # 없으면 "default" 반환

# 4) 키 존재 여부 확인
if "key1" in hash_map:
    print("존재함")

# 5) 값 삭제
del hash_map["key1"]
hash_map.pop("key2", None)  # 없어도 에러 안남


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 카운팅
def count_elements(arr):
    """배열 요소의 개수를 세는 함수"""
    counter = {}
    for item in arr:
        counter[item] = counter.get(item, 0) + 1
    return counter

# 패턴 2: collections.Counter 사용 (더 간단)
from collections import Counter
arr = [1, 2, 2, 3, 3, 3]
counter = Counter(arr)  # Counter({3: 3, 2: 2, 1: 1})

# 패턴 3: defaultdict 사용
from collections import defaultdict
counter = defaultdict(int)  # 기본값 0
for item in arr:
    counter[item] += 1

# 패턴 4: 그룹핑
def group_by_length(words):
    """단어를 길이별로 그룹화"""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return groups


"""
================================================================================
5. 대표 문제: 두 수의 합 (Two Sum)
================================================================================

[문제]
정수 배열 nums와 정수 target이 주어집니다.
nums에서 두 수를 더해서 target이 되는 두 수의 인덱스를 반환하세요.

[제약]
- 정확히 하나의 정답이 존재
- 같은 요소를 두 번 사용할 수 없음

[예시]
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
설명: nums[0] + nums[1] = 2 + 7 = 9


6. 문제 해설
--------------------------------------------------------------------------------
브루트포스로 풀면?
    - 모든 쌍을 비교: O(n²)
    - nums[i] + nums[j] == target 인지 확인

해시로 풀면?
    - O(n) 으로 해결 가능!
    - 핵심 아이디어: "target - 현재값"이 이전에 나왔는지 확인

동작 과정 (nums = [2, 7, 11, 15], target = 9):

    hash_map = {}  # {값: 인덱스}

    i=0, num=2:
        필요한 값 = 9 - 2 = 7
        7이 hash_map에 있나? → 없음
        hash_map에 저장: {2: 0}

    i=1, num=7:
        필요한 값 = 9 - 7 = 2
        2가 hash_map에 있나? → 있음! (인덱스 0)
        정답: [0, 1]

왜 해시를 쓰나?
    - "어떤 값이 이전에 나왔는지"를 O(1)에 확인 가능
    - 리스트로 하면 O(n), 해시로 하면 O(1)


7. 코드 구현
--------------------------------------------------------------------------------
"""

def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    """
    브루트포스 방법 - O(n²)
    모든 쌍을 확인
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash(nums: list[int], target: int) -> list[int]:
    """
    해시 방법 - O(n)
    이전에 나온 숫자들을 해시에 저장하고,
    현재 숫자와 더해서 target이 되는 숫자가 있는지 확인
    """
    # {숫자: 인덱스} 형태로 저장
    seen = {}

    for i, num in enumerate(nums):
        # target을 만들기 위해 필요한 숫자
        complement = target - num

        # 필요한 숫자가 이전에 나왔는지 확인
        if complement in seen:
            return [seen[complement], i]

        # 현재 숫자를 해시에 저장
        seen[num] = i

    return []


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""

def two_sum_with_trace(nums: list[int], target: int) -> list[int]:
    """동작 과정을 출력하면서 실행"""
    print(f"입력: nums = {nums}, target = {target}")
    print("=" * 50)

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        print(f"\n[Step {i+1}] 현재 숫자: {num} (인덱스: {i})")
        print(f"  - 필요한 숫자: {target} - {num} = {complement}")
        print(f"  - 현재 해시맵: {seen}")

        if complement in seen:
            print(f"  - {complement}이(가) 해시맵에 있음! (인덱스: {seen[complement]})")
            print(f"\n정답: [{seen[complement]}, {i}]")
            return [seen[complement], i]
        else:
            print(f"  - {complement}이(가) 해시맵에 없음")
            print(f"  - 해시맵에 추가: {{{num}: {i}}}")

        seen[num] = i

    return []


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("해시(Hash) 예제 실행")
    print("=" * 60)

    # 기본 테스트
    nums = [2, 7, 11, 15]
    target = 9

    print("\n[브루트포스 방법]")
    result1 = two_sum_bruteforce(nums, target)
    print(f"결과: {result1}")

    print("\n[해시 방법]")
    result2 = two_sum_hash(nums, target)
    print(f"결과: {result2}")

    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    two_sum_with_trace(nums, target)

    # 추가 테스트
    print("\n\n" + "=" * 60)
    print("추가 테스트")
    print("=" * 60)

    test_cases = [
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 3, 7, 2], 9),
    ]

    for nums, target in test_cases:
        result = two_sum_hash(nums, target)
        print(f"nums={nums}, target={target} → {result}")


"""
================================================================================
9. 연습 문제 추천
================================================================================

쉬움:
- 백준 1920번: 수 찾기
- 프로그래머스: 완주하지 못한 선수

중간:
- 백준 1764번: 듣보잡
- 프로그래머스: 전화번호 목록
- LeetCode 49: Group Anagrams

어려움:
- 백준 7785번: 회사에 있는 사람
- LeetCode 128: Longest Consecutive Sequence
================================================================================
"""
