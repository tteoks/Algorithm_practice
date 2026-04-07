"""
================================================================================
                         트라이 (Trie) / 접두사 트리 (Prefix Tree)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
트라이는 "문자열을 빠르게 검색"하기 위한 트리 자료구조입니다.
각 간선이 하나의 문자를 나타내고, 루트에서 특정 노드까지의 경로가 하나의 문자열입니다.

핵심 특징:
- 문자열 검색: O(M) (M = 문자열 길이)
- 접두사(prefix) 검색에 매우 강력
- 자동완성, 사전 구현에 활용

언제 사용하나?
- 문자열 검색/존재 여부 확인
- 접두사 기반 검색 (자동완성)
- 사전 구현
- 문자열 집합에서 공통 접두사
- XOR 최대값 (비트 트라이)


2. 동작 원리
--------------------------------------------------------------------------------

["apple", "app", "april", "bat"] 삽입 후 트라이:

    (root)
     / \
    a   b
    |   |
    p   a
    |   |
    p*  t*
   / \
  l   r
  |   |
  e*  i
      |
      l*

    * = 단어의 끝 표시

    경로를 따라가면 문자열이 됨:
    root → a → p → p = "app" (*)
    root → a → p → p → l → e = "apple" (*)
    root → a → p → r → i → l = "april" (*)
    root → b → a → t = "bat" (*)


[검색 과정]

    "app" 검색:
    root → a (있음) → p (있음) → p (있음, 끝 표시 있음) → 찾음!

    "ap" 검색:
    root → a (있음) → p (있음, 끝 표시 없음) → 단어로는 없음!
    (하지만 접두사로는 존재)

    "ace" 검색:
    root → a (있음) → c (없음!) → 없음!


[삽입 과정] - "apt" 삽입:

    root → a (이미 있음) → p (이미 있음) → t (새로 생성, 끝 표시)

    (root)
     / \
    a   b
    |   |
    p   a
    |   |
    p*  t*
   /|\
  l  r  t*   ← 새로 추가!
  |  |
  e* i
     |
     l*


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산          | 시간복잡도  | 비교 (해시맵)  |
|--------------|-----------|-------------|
| 삽입         | O(M)      | O(M)        |
| 검색         | O(M)      | O(M)        |
| 접두사 검색   | O(M)      | O(N × M)    |
| 삭제         | O(M)      | O(M)        |

* M: 문자열 길이, N: 저장된 문자열 수
* 접두사 검색에서 트라이가 압도적으로 유리!


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""


# ================================
# 기본 구현 (딕셔너리 기반)
# ================================

class TrieNode:
    def __init__(self):
        self.children = {}  # {문자: TrieNode}
        self.is_end = False  # 단어의 끝인지


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """단어 삽입 - O(M)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """단어가 존재하는지 - O(M)"""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """접두사로 시작하는 단어가 있는지 - O(M)"""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        """접두사의 마지막 노드를 반환"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 자동완성 (접두사로 시작하는 모든 단어 찾기)
class TrieWithAutocomplete(Trie):
    def autocomplete(self, prefix: str) -> list[str]:
        """접두사로 시작하는 모든 단어 반환"""
        node = self._find_node(prefix)
        if node is None:
            return []

        results = []
        self._collect_words(node, prefix, results)
        return results

    def _collect_words(self, node: TrieNode, current: str, results: list):
        if node.is_end:
            results.append(current)
        for char, child in sorted(node.children.items()):
            self._collect_words(child, current + char, results)


# 패턴 2: 단어 수 세기 (count 저장)
class TrieWithCount:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = node.get('#', 0) + 1  # '#'으로 끝 표시 + 횟수

    def count(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node:
                return 0
            node = node[char]
        return node.get('#', 0)

    def count_prefix(self, prefix: str) -> int:
        """접두사로 시작하는 단어 수"""
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return self._count_all(node)

    def _count_all(self, node: dict) -> int:
        total = node.get('#', 0)
        for key, child in node.items():
            if key != '#':
                total += self._count_all(child)
        return total


# 패턴 3: 간결한 딕셔너리 트라이 (코테용)
def make_trie(words: list[str]) -> dict:
    """딕셔너리로 간단하게 트라이 만들기"""
    root = {}
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True  # 끝 표시
    return root


def search_trie(trie: dict, word: str) -> bool:
    """트라이에서 단어 검색"""
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '$' in node


"""
================================================================================
5. 대표 문제: Trie 구현 (LeetCode 208)
================================================================================

[문제]
트라이를 구현하세요. 다음 연산을 지원해야 합니다:
- insert(word): 단어를 트라이에 삽입
- search(word): 단어가 트라이에 있는지 반환
- startsWith(prefix): 접두사로 시작하는 단어가 있는지 반환

[예시]
trie = Trie()
trie.insert("apple")
trie.search("apple")     → True
trie.search("app")       → False
trie.startsWith("app")   → True
trie.insert("app")
trie.search("app")       → True


6. 문제 해설
--------------------------------------------------------------------------------
핵심 포인트:
    - search vs startsWith의 차이:
      search: 정확히 그 단어가 있는지 (is_end == True)
      startsWith: 접두사까지의 경로만 존재하면 됨

동작 과정:

    insert("apple"):
    root → a(새) → p(새) → p(새) → l(새) → e(새, end=True)

    search("apple"):
    root → a(있음) → p(있음) → p(있음) → l(있음) → e(있음, end=True) → True

    search("app"):
    root → a(있음) → p(있음) → p(있음, end=False) → False

    startsWith("app"):
    root → a(있음) → p(있음) → p(있음) → True (끝까지 탐색 가능)

    insert("app"):
    root → a(있음) → p(있음) → p(있음, end=True로 변경!)

    search("app"):
    root → a(있음) → p(있음) → p(있음, end=True) → True


7. 코드 구현
--------------------------------------------------------------------------------
"""


class TrieSolution:
    """LeetCode 208 풀이"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # 끝 표시 확인!

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # 경로만 존재하면 됨!


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


class TrieWithTrace:
    """동작 과정을 출력하는 트라이"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        print(f"\nInsert('{word}')")
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
                print(f"  '{word[:i+1]}' → '{char}' 노드 새로 생성")
            else:
                print(f"  '{word[:i+1]}' → '{char}' 노드 이미 존재")
            node = node.children[char]
        node.is_end = True
        print(f"  '{word}' 끝 표시!")

    def search(self, word: str) -> bool:
        print(f"\nSearch('{word}')")
        node = self.root
        for char in word:
            if char not in node.children:
                print(f"  '{char}' 없음 → False")
                return False
            print(f"  '{char}' 있음 →", end=" ")
            node = node.children[char]
        result = node.is_end
        print(f"\n  끝 표시: {result} → {result}")
        return result

    def starts_with(self, prefix: str) -> bool:
        print(f"\nStartsWith('{prefix}')")
        node = self.root
        for char in prefix:
            if char not in node.children:
                print(f"  '{char}' 없음 → False")
                return False
            print(f"  '{char}' 있음 →", end=" ")
            node = node.children[char]
        print(f"\n  접두사 경로 존재 → True")
        return True

    def display(self, node=None, prefix="", indent=""):
        """트라이 구조 시각화"""
        if node is None:
            node = self.root
            print("\n[트라이 구조]")

        for char, child in sorted(node.children.items()):
            end_mark = "*" if child.is_end else ""
            print(f"{indent}{char}{end_mark}")
            self.display(child, prefix + char, indent + "  ")


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("트라이 예제 실행")
    print("=" * 60)

    # 기본 사용
    print("\n[기본 사용]")
    trie = Trie()
    words = ["apple", "app", "april", "bat", "ball"]
    for word in words:
        trie.insert(word)
        print(f"Insert: '{word}'")

    print(f"\nSearch 'apple': {trie.search('apple')}")   # True
    print(f"Search 'app': {trie.search('app')}")         # True
    print(f"Search 'ap': {trie.search('ap')}")           # False
    print(f"StartsWith 'ap': {trie.starts_with('ap')}")  # True
    print(f"StartsWith 'ba': {trie.starts_with('ba')}")  # True
    print(f"StartsWith 'ca': {trie.starts_with('ca')}")  # False

    # 자동완성
    print("\n[자동완성]")
    ac_trie = TrieWithAutocomplete()
    for word in words:
        ac_trie.insert(word)

    print(f"'ap' 자동완성: {ac_trie.autocomplete('ap')}")
    print(f"'ba' 자동완성: {ac_trie.autocomplete('ba')}")
    print(f"'b' 자동완성: {ac_trie.autocomplete('b')}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)

    trace = TrieWithTrace()
    trace.insert("apple")
    trace.insert("app")
    trace.insert("april")

    trace.display()

    trace.search("apple")
    trace.search("app")
    trace.search("ap")
    trace.starts_with("ap")

    # 간결한 딕셔너리 트라이
    print("\n" + "=" * 60)
    print("딕셔너리 트라이 (코테용)")
    print("=" * 60)

    trie_dict = make_trie(["apple", "app", "bat"])
    print(f"Search 'apple': {search_trie(trie_dict, 'apple')}")
    print(f"Search 'app': {search_trie(trie_dict, 'app')}")
    print(f"Search 'ap': {search_trie(trie_dict, 'ap')}")


"""
================================================================================
9. 트라이 활용 팁
================================================================================

[트라이 vs 해시맵]
- 정확한 단어 검색만: 해시맵이 더 간단
- 접두사 검색, 자동완성: 트라이가 필수
- 사전순 정렬 필요: 트라이 (children을 정렬하며 순회)

[메모리 최적화]
- 딕셔너리 기반: 유연하지만 메모리 많이 사용
- 배열 기반 (26 크기): 소문자만 쓸 때 더 빠름
  children = [None] * 26
  index = ord(char) - ord('a')

[코테에서 트라이가 필요한 힌트]
- "접두사" 키워드
- "자동완성"
- "사전에서 검색"
- "문자열 집합에서 ~"


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- LeetCode 208번: Implement Trie
- LeetCode 14번: Longest Common Prefix
- 백준 5052번: 전화번호 목록

중급:
- LeetCode 211번: Design Add and Search Words Data Structure
- LeetCode 648번: Replace Words
- 백준 14425번: 문자열 집합

고급:
- LeetCode 212번: Word Search II
- LeetCode 421번: Maximum XOR of Two Numbers (비트 트라이)
- 백준 13505번: 두 수 XOR
================================================================================
"""
