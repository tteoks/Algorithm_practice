"""
================================================================================
                         트리 (Tree) / 이진 트리 (Binary Tree)
================================================================================

1. 상세한 설명
--------------------------------------------------------------------------------
트리는 "계층적 구조"를 표현하는 자료구조입니다.
노드와 간선으로 이루어져 있고, 사이클이 없는 연결 그래프입니다.

종류:
- 이진 트리 (Binary Tree): 각 노드의 자식이 최대 2개
- 이진 탐색 트리 (BST): 왼쪽 < 부모 < 오른쪽
- 완전 이진 트리: 마지막 레벨 제외 모든 레벨이 꽉 참
- 균형 이진 트리 (AVL, Red-Black): 높이 차이가 1 이하

핵심 용어:
- 루트 (Root): 최상위 노드
- 리프 (Leaf): 자식이 없는 노드
- 깊이 (Depth): 루트에서 해당 노드까지의 거리
- 높이 (Height): 리프까지의 최대 거리
- 서브트리: 특정 노드를 루트로 하는 부분 트리

언제 사용하나?
- 계층적 데이터 표현 (파일 시스템, 조직도)
- 탐색/정렬 (BST)
- 힙 (우선순위 큐)
- 트라이 (문자열 검색)
- 수식 파싱


2. 동작 원리
--------------------------------------------------------------------------------

[이진 트리 구조]
           1         ← 루트 (Root)
         /   \
        2     3      ← 깊이 1
       / \     \
      4   5     6    ← 깊이 2 (4, 5, 6은 리프)

    높이 = 2


[트리 순회 (Traversal)] - 가장 중요!

    전위 순회 (Preorder):  루트 → 왼쪽 → 오른쪽
        1 → 2 → 4 → 5 → 3 → 6

    중위 순회 (Inorder):   왼쪽 → 루트 → 오른쪽
        4 → 2 → 5 → 1 → 3 → 6

    후위 순회 (Postorder): 왼쪽 → 오른쪽 → 루트
        4 → 5 → 2 → 6 → 3 → 1

    레벨 순회 (Level-order): BFS와 동일
        1 → 2 → 3 → 4 → 5 → 6


    암기법:
    - 전위: "루"왼오 (루트 먼저)
    - 중위: 왼"루"오 (루트 중간)
    - 후위: 왼오"루" (루트 마지막)


[이진 탐색 트리 (BST)]

           8
         /   \
        3     10
       / \      \
      1   6     14
         / \    /
        4   7  13

    특징: 왼쪽 서브트리의 모든 값 < 부모 < 오른쪽 서브트리의 모든 값
    중위 순회하면 정렬된 순서!: 1, 3, 4, 6, 7, 8, 10, 13, 14


3. 시간복잡도
--------------------------------------------------------------------------------
| 연산              | BST (평균)  | BST (최악)  | 균형 BST    |
|------------------|-----------|-----------|-----------|
| 탐색 (Search)    | O(log n)  | O(n)      | O(log n)  |
| 삽입 (Insert)    | O(log n)  | O(n)      | O(log n)  |
| 삭제 (Delete)    | O(log n)  | O(n)      | O(log n)  |
| 순회 (Traversal) | O(n)      | O(n)      | O(n)      |

* 최악: 편향 트리 (1-2-3-4-5 일자로 연결)


4. 예시 코드 (템플릿)
--------------------------------------------------------------------------------
"""

from collections import deque


# ================================
# 트리 노드 정의
# ================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ================================
# 트리 순회 (가장 중요!)
# ================================

# 전위 순회: 루트 → 왼쪽 → 오른쪽
def preorder(root: TreeNode) -> list:
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


# 중위 순회: 왼쪽 → 루트 → 오른쪽
def inorder(root: TreeNode) -> list:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# 후위 순회: 왼쪽 → 오른쪽 → 루트
def postorder(root: TreeNode) -> list:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# 레벨 순회 (BFS)
def level_order(root: TreeNode) -> list[list]:
    """레벨별로 묶어서 반환"""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ================================
# 자주 쓰는 패턴
# ================================

# 패턴 1: 트리 높이 구하기
def tree_height(root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


# 패턴 2: 노드 개수 세기
def count_nodes(root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# 패턴 3: 리스트로 트리 만들기 (LeetCode 스타일)
def build_tree_from_list(vals: list) -> TreeNode:
    """
    [1, 2, 3, None, 5, None, 6] → 트리 생성
    인덱스 기준: 부모 i → 왼쪽 2i+1, 오른쪽 2i+2
    """
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1

    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1

    return root


# 패턴 4: 경로 합 (Path Sum)
def has_path_sum(root: TreeNode, target: int) -> bool:
    """루트에서 리프까지 경로 합이 target인지"""
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))


"""
================================================================================
5. 대표 문제: 이진 트리의 최대 깊이 (LeetCode 104)
================================================================================

[문제]
이진 트리의 루트가 주어질 때, 트리의 최대 깊이를 구하세요.
최대 깊이는 루트에서 가장 먼 리프 노드까지의 경로의 노드 수입니다.

[예시]
Input:
        3
       / \
      9   20
         /  \
        15   7

Output: 3 (3 → 20 → 15 또는 3 → 20 → 7)


6. 문제 해설
--------------------------------------------------------------------------------
왜 재귀를 쓰나?
    - 트리는 재귀적 구조 (서브트리도 트리)
    - "전체 트리 높이 = 1 + max(왼쪽 높이, 오른쪽 높이)"

알고리즘:
    1. base case: 노드가 None이면 깊이 0
    2. 왼쪽 서브트리 깊이 재귀 계산
    3. 오른쪽 서브트리 깊이 재귀 계산
    4. 1 + max(왼쪽, 오른쪽) 반환

동작 과정:
        3
       / \
      9   20
         /  \
        15   7

    max_depth(3)
    ├── max_depth(9)
    │   ├── max_depth(None) → 0
    │   └── max_depth(None) → 0
    │   → 1 + max(0, 0) = 1
    └── max_depth(20)
        ├── max_depth(15)
        │   ├── max_depth(None) → 0
        │   └── max_depth(None) → 0
        │   → 1 + max(0, 0) = 1
        └── max_depth(7)
            ├── max_depth(None) → 0
            └── max_depth(None) → 0
            → 1 + max(0, 0) = 1
        → 1 + max(1, 1) = 2
    → 1 + max(1, 2) = 3


7. 코드 구현
--------------------------------------------------------------------------------
"""


def max_depth(root: TreeNode) -> int:
    """
    이진 트리의 최대 깊이

    Args:
        root: 트리의 루트 노드

    Returns:
        최대 깊이
    """
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# BFS 풀이 (반복)
def max_depth_bfs(root: TreeNode) -> int:
    """BFS로 최대 깊이 구하기"""
    if root is None:
        return 0

    depth = 0
    queue = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


"""
8. 상세 동작 예시
--------------------------------------------------------------------------------
"""


def max_depth_with_trace(root: TreeNode, depth=1, prefix="") -> int:
    """동작 과정을 출력하면서 실행"""
    if root is None:
        print(f"{prefix}None → 깊이 0 반환")
        return 0

    print(f"{prefix}노드 {root.val} (현재 깊이 {depth})")

    left = max_depth_with_trace(root.left, depth + 1, prefix + "  L: ")
    right = max_depth_with_trace(root.right, depth + 1, prefix + "  R: ")

    result = 1 + max(left, right)
    print(f"{prefix}노드 {root.val} → 1 + max({left}, {right}) = {result}")
    return result


# ================================
# 추가 예제: 대칭 트리 판별
# ================================

def is_symmetric(root: TreeNode) -> bool:
    """
    트리가 좌우 대칭인지 판별 (LeetCode 101)

        1
       / \
      2   2     ← 대칭!
     / \ / \
    3  4 4  3
    """
    def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root.left, root.right) if root else True


# ================================
# 추가 예제: 최소 공통 조상 (LCA)
# ================================

def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> TreeNode:
    """
    두 노드의 최소 공통 조상 (LeetCode 236)

            3
           / \
          5   1
         / \ / \
        6  2 0  8

    LCA(5, 1) = 3
    LCA(5, 4) = 5
    """
    if root is None or root.val == p or root.val == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root  # p, q가 양쪽에 각각 있으면 현재 노드가 LCA
    return left or right


# ================================
# 실행 예시
# ================================

if __name__ == "__main__":
    print("=" * 60)
    print("트리 예제 실행")
    print("=" * 60)

    # 트리 생성
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # 순회
    print("\n[트리 순회]")
    print(f"전위 순회 (루→왼→오): {preorder(root)}")
    print(f"중위 순회 (왼→루→오): {inorder(root)}")
    print(f"후위 순회 (왼→오→루): {postorder(root)}")
    print(f"레벨 순회 (BFS):      {level_order(root)}")

    # 트리 정보
    print(f"\n[트리 정보]")
    print(f"높이: {tree_height(root)}")
    print(f"노드 수: {count_nodes(root)}")

    # 최대 깊이
    print("\n" + "=" * 60)
    print("최대 깊이 문제")
    print("=" * 60)

    tree2 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    print(f"\n최대 깊이: {max_depth(tree2)}")

    # 상세 동작 추적
    print("\n" + "=" * 60)
    print("동작 과정 추적")
    print("=" * 60)
    max_depth_with_trace(tree2)

    # 대칭 트리
    print("\n" + "=" * 60)
    print("대칭 트리 판별")
    print("=" * 60)

    sym_tree = build_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    print(f"[1,2,2,3,4,4,3] → 대칭? {is_symmetric(sym_tree)}")

    asym_tree = build_tree_from_list([1, 2, 2, None, 3, None, 3])
    print(f"[1,2,2,None,3,None,3] → 대칭? {is_symmetric(asym_tree)}")


"""
================================================================================
9. 트리 문제 풀이 팁
================================================================================

[재귀 사고법]
1. base case 먼저 정의 (None일 때)
2. 현재 노드에서 할 일 정의
3. 왼쪽/오른쪽 서브트리에 위임
4. 결과 합치기

[순회 선택 가이드]
- 전위: 트리 복사, 직렬화
- 중위: BST에서 정렬된 결과 (매우 중요!)
- 후위: 트리 삭제, 높이/크기 계산
- 레벨: 레벨별 처리, 최단 거리

[코딩 테스트 빈출 유형]
- 트리 높이/깊이
- 경로 합 (Path Sum)
- 대칭/동일 트리 판별
- LCA (최소 공통 조상)
- BST 검증/탐색
- 직렬화/역직렬화


================================================================================
10. 연습 문제 추천
================================================================================

기초:
- LeetCode 104번: Maximum Depth of Binary Tree
- LeetCode 226번: Invert Binary Tree
- LeetCode 101번: Symmetric Tree
- 백준 1991번: 트리 순회

중급:
- LeetCode 102번: Binary Tree Level Order Traversal
- LeetCode 112번: Path Sum
- LeetCode 236번: Lowest Common Ancestor
- 백준 11725번: 트리의 부모 찾기

고급:
- LeetCode 124번: Binary Tree Maximum Path Sum
- LeetCode 297번: Serialize and Deserialize Binary Tree
- 백준 1167번: 트리의 지름
================================================================================
"""
