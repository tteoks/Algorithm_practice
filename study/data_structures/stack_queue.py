"""
================================================================================
                           스택 (Stack) & 큐 (Queue)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------

[스택 (Stack)]
- LIFO (Last In, First Out): 마지막에 넣은 것이 먼저 나옴
- 접시 쌓기와 같음: 맨 위에 올리고, 맨 위에서 꺼냄
- 주요 연산: push(삽입), pop(제거), peek/top(맨 위 확인)

[큐 (Queue)]
- FIFO (First In, First Out): 먼저 넣은 것이 먼저 나옴
- 줄 서기와 같음: 뒤에 서고, 앞에서 나감
- 주요 연산: enqueue(삽입), dequeue(제거), front(맨 앞 확인)

언제 사용하나?
- 스택: 괄호 매칭, 뒤로가기, 재귀 대체, DFS
- 큐: BFS, 프로세스 스케줄링, 버퍼


2. 동작 원리
--------------------------------------------------------------------------------

[스택]
    push(1), push(2), push(3) 후:

    |  3  | ← top (마지막에 넣은 것)
    |  2  |
    |  1  | ← bottom (처음에 넣은 것)
    +-----+

    pop() → 3 반환
    pop() → 2 반환
    pop() → 1 반환


[큐]
    enqueue(1), enqueue(2), enqueue(3) 후:

    front                     rear
      ↓                        ↓
    [  1  |  2  |  3  ]
      ↑
    dequeue() → 1 반환

    남은 상태:
    [  2  |  3  ]


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산          | 스택    | 큐 (deque) |
|--------------|--------|-----------|
| push/enqueue | O(1)   | O(1)      |
| pop/dequeue  | O(1)   | O(1)      |
| peek/front   | O(1)   | O(1)      |

* 주의: 파이썬 리스트의 pop(0)은 O(n)이므로 큐는 deque를 사용!


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

from collections import deque

# ================================
# 스택 (Stack)
# ================================

# 파이썬에서 스택은 리스트로 구현
stack = []

# push (삽입)
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Push 후: {stack}")  # [1, 2, 3]

# pop (제거 + 반환)
top = stack.pop()
print(f"Pop: {top}")  # 3
print(f"Pop 후: {stack}")  # [1, 2]

# peek (제거 없이 확인)
if stack:  # 비어있는지 확인 중요!
    top = stack[-1]
    print(f"Peek: {top}")  # 2

# 스택이 비어있는지 확인
is_empty = len(stack) == 0
# 또는
is_empty = not stack


# ================================
# 큐 (Queue)
# ================================

# 파이썬에서 큐는 deque로 구현 (리스트 pop(0)은 느림!)
queue = deque()

# enqueue (삽입)
queue.append(1)
queue.append(2)
queue.append(3)
print(f"Enqueue 후: {list(queue)}")  # [1, 2, 3]

# dequeue (제거 + 반환)
front = queue.popleft()  # O(1) - 리스트의 pop(0)은 O(n)!
print(f"Dequeue: {front}")  # 1
print(f"Dequeue 후: {list(queue)}")  # [2, 3]

# front (제거 없이 확인)
if queue:
    front = queue[0]
    print(f"Front: {front}")  # 2


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 스택으로 문자열 뒤집기
def reverse_string(s: str) -> str:
    stack = list(s)
    result = ""
    while stack:
        result += stack.pop()
    return result


# 패턴 2: 괄호 매칭 기본
def is_valid_parentheses_simple(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


"""
================================================================================
5. 대표 문제: 유효한 괄호 (Valid Parentheses)
================================================================================

[문제]
괄호로 이루어진 문자열 s가 주어집니다.
올바른 괄호 문자열인지 판단하세요.

올바른 괄호 문자열 조건:
1. 열린 괄호는 같은 타입의 닫힌 괄호로 닫혀야 함
2. 열린 괄호는 올바른 순서로 닫혀야 함
3. 모든 닫힌 괄호에는 대응하는 같은 타입의 열린 괄호가 있어야 함

괄호 종류: (), {}, []

[예시]
Input: s = "()"       → Output: True
Input: s = "()[]{}"   → Output: True
Input: s = "(]"       → Output: False
Input: s = "([)]"     → Output: False  ← 순서가 잘못됨
Input: s = "{[]}"     → Output: True   ← 중첩 OK


6. 문제 해설
--------------------------------------------------------------------------------
왜 스택을 쓰나?
    - 가장 최근에 열린 괄호가 가장 먼저 닫혀야 함 (LIFO)
    - 예: "([)]"에서 '['가 '('보다 나중에 열렸으니 먼저 닫혀야 함

알고리즘:
    1. 열린 괄호를 만나면 스택에 push
    2. 닫힌 괄호를 만나면:
       - 스택이 비어있으면 False (대응하는 열린 괄호 없음)
       - 스택 top이 대응하는 열린 괄호가 아니면 False
       - 맞으면 pop
    3. 끝까지 처리 후 스택이 비어있으면 True

동작 과정 (s = "{[]}"):

    스택: []

    '{' → 열린 괄호 → push
    스택: ['{']

    '[' → 열린 괄호 → push
    스택: ['{', '[']

    ']' → 닫힌 괄호
        - 스택 top: '[' ← ']'와 매칭! → pop
    스택: ['{']

    '}' → 닫힌 괄호
        - 스택 top: '{' ← '}'와 매칭! → pop
    스택: []

    끝! 스택이 비어있으므로 True


동작 과정 (s = "([)]"):

    스택: []

    '(' → push
    스택: ['(']

    '[' → push
    스택: ['(', '[']

    ')' → 닫힌 괄호
        - 스택 top: '[' ← ')'와 매칭 안됨!
    → False 반환


7. 코드 구현
--------------------------------------------------------------------------------
"""


def is_valid_parentheses(s: str) -> bool:
    """
    유효한 괄호 검사 - O(n)

    Args:
        s: 괄호로 이루어진 문자열

    Returns:
        올바른 괄호 문자열이면 True
    """
    # 닫힌 괄호 → 열린 괄호 매핑
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        if char in matching:  # 닫힌 괄호인 경우
            # 스택이 비어있거나, top이 매칭되지 않으면 False
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:  # 열린 괄호인 경우
            stack.append(char)

    # 스택이 비어있어야 모든 괄호가 매칭된 것
    return len(stack) == 0


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def is_valid_with_trace(s: str) -> bool:
    """동작 과정을 출력하면서 실행"""
    print(f"입력: s = \"{s}\"")
    print("=" * 50)

    matching = {')': '(', '}': '{', ']': '['}
    bracket_names = {'(': '소괄호 열기', ')': '소괄호 닫기',
                     '{': '중괄호 열기', '}': '중괄호 닫기',
                     '[': '대괄호 열기', ']': '대괄호 닫기'}

    stack = []

    for i, char in enumerate(s):
        print(f"\n[Step {i+1}] 문자: '{char}' ({bracket_names.get(char, '?')})")

        if char in matching:  # 닫힌 괄호
            print(f"  → 닫힌 괄호 발견!")
            print(f"  현재 스택: {stack}")

            if not stack:
                print(f"  → 스택이 비어있음! 매칭 실패")
                print(f"\n결과: False")
                return False

            if stack[-1] != matching[char]:
                print(f"  → 스택 top '{stack[-1]}'과 매칭 안됨! (필요: '{matching[char]}')")
                print(f"\n결과: False")
                return False

            popped = stack.pop()
            print(f"  → 스택 top '{popped}'과 매칭 성공! pop 수행")
            print(f"  스택 상태: {stack}")

        else:  # 열린 괄호
            stack.append(char)
            print(f"  → 열린 괄호, 스택에 push")
            print(f"  스택 상태: {stack}")

    print(f"\n처리 완료!")
    print(f"최종 스택: {stack}")

    if len(stack) == 0:
        print(f"스택이 비어있음 → 모든 괄호 매칭 성공!")
        print(f"\n결과: True")
        return True
    else:
        print(f"스택에 남은 괄호 있음 → 매칭 실패")
        print(f"\n결과: False")
        return False


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("스택/큐 예제 실행")
    print("=" * 60)

    # 스택 기본 동작
    print("\n[스택 기본 동작]")
    stack = []
    for i in [1, 2, 3]:
        stack.append(i)
        print(f"push({i}) → 스택: {stack}")

    while stack:
        val = stack.pop()
        print(f"pop() = {val} → 스택: {stack}")

    # 큐 기본 동작
    print("\n[큐 기본 동작]")
    queue = deque()
    for i in [1, 2, 3]:
        queue.append(i)
        print(f"enqueue({i}) → 큐: {list(queue)}")

    while queue:
        val = queue.popleft()
        print(f"dequeue() = {val} → 큐: {list(queue)}")

    # 괄호 검사 테스트
    print("\n" + "=" * 60)
    print("유효한 괄호 검사")
    print("=" * 60)

    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "((()))",
        "(()",
    ]

    print("\n[빠른 테스트]")
    for s in test_cases:
        result = is_valid_parentheses(s)
        status = "O" if result else "X"
        print(f'  "{s}" → {status}')

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)

    print("\n--- 성공 케이스 ---")
    is_valid_with_trace("{[]}")

    print("\n\n--- 실패 케이스 (순서 오류) ---")
    is_valid_with_trace("([)]")

    print("\n\n--- 실패 케이스 (닫히지 않음) ---")
    is_valid_with_trace("(()")


"""
================================================================================
9. 추가: 스택/큐 응용 문제들
================================================================================

[스택 응용]
- 후위 표기식 계산
- 히스토그램에서 가장 큰 직사각형
- 주식 가격 (이전 값들과 비교)
- 탑 (레이저 쏘기)

[큐 응용]
- BFS (너비 우선 탐색)
- 요세푸스 문제
- 프린터 큐


================================================================================
10. 연습 문제 추천
================================================================================

스택:
- 백준 10828번: 스택 (기초)
- 백준 9012번: 괄호 (괄호 매칭)
- 백준 4949번: 균형잡힌 세상 (여러 종류 괄호)
- 프로그래머스: 주식가격

큐:
- 백준 10845번: 큐 (기초)
- 백준 1158번: 요세푸스 문제
- 프로그래머스: 프린터
================================================================================
"""
