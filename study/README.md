# 코딩 테스트 준비 로드맵

## 급하게 준비할 때 우선순위

### 1순위 (필수, 가장 자주 출제)
| 주제 | 설명 | 예상 빈도 |
|------|------|-----------|
| **해시 (Hash)** | 딕셔너리 활용, 중복 체크, 카운팅 | 매우 높음 |
| **정렬 (Sorting)** | 기본 정렬, 커스텀 정렬 | 매우 높음 |
| **스택/큐 (Stack/Queue)** | 괄호 매칭, BFS 기본 | 매우 높음 |
| **DFS/BFS** | 그래프 탐색, 최단 경로 | 매우 높음 |
| **그리디 (Greedy)** | 최적해 선택 | 높음 |

### 2순위 (중요, 자주 출제)
| 주제 | 설명 | 예상 빈도 |
|------|------|-----------|
| **이진 탐색 (Binary Search)** | 탐색 최적화, parametric search | 높음 |
| **DP (Dynamic Programming)** | 점화식, 메모이제이션 | 높음 |
| **힙 (Heap/Priority Queue)** | 우선순위 처리 | 중간 |
| **투 포인터 (Two Pointer)** | 연속 부분 배열 | 중간 |
| **슬라이딩 윈도우** | 구간 합, 부분 문자열 | 중간 |

### 3순위 (심화)
| 주제 | 설명 | 예상 빈도 |
|------|------|-----------|
| **트리 (Tree)** | 이진 트리, 순회 | 중간 |
| **그래프 (Graph)** | 다익스트라, 플로이드-워셜 | 중간 |
| **유니온 파인드 (Union-Find)** | 집합 연산, 사이클 판별 | 낮음 |
| **트라이 (Trie)** | 문자열 검색 | 낮음 |
| **세그먼트 트리** | 구간 쿼리 | 낮음 |

---

## 디렉터리 구조

```
study/
├── data_structures/    # 자료구조
│   ├── hash.py
│   ├── stack.py
│   ├── queue.py
│   ├── heap.py
│   ├── linked_list.py
│   ├── tree.py
│   ├── graph.py
│   ├── trie.py
│   └── union_find.py
│
└── algorithms/         # 알고리즘
    ├── sorting.py
    ├── binary_search.py
    ├── dfs_bfs.py
    ├── dynamic_programming.py
    ├── greedy.py
    ├── two_pointer.py
    ├── sliding_window.py
    ├── shortest_path.py
    └── backtracking.py
```

---

## 추천 학습 순서 (2주 집중 코스)

### Week 1: 기초 다지기
- Day 1-2: 해시, 스택, 큐
- Day 3-4: 정렬, 이진 탐색
- Day 5-7: DFS/BFS

### Week 2: 심화
- Day 1-2: 그리디
- Day 3-4: DP 기초
- Day 5-6: 힙, 투 포인터
- Day 7: 복습 및 실전 문제

---

## 체크리스트

### 1순위 (완료)
- [x] Hash - `data_structures/hash.py`
- [x] Stack/Queue - `data_structures/stack_queue.py`
- [x] DFS/BFS - `algorithms/dfs_bfs.py`
- [x] Sorting - `algorithms/sorting.py`
- [x] Greedy - `algorithms/greedy.py`

### 2순위 (완료)
- [x] Binary Search - `algorithms/binary_search.py`
- [x] DP - `algorithms/dynamic_programming.py`
- [x] Heap - `data_structures/heap.py`
- [x] Two Pointer - `algorithms/two_pointer.py`
- [x] Sliding Window - `algorithms/sliding_window.py`

### 3순위 (완료)
- [x] Tree - `data_structures/tree.py`
- [x] Graph (Dijkstra, Floyd-Warshall) - `algorithms/shortest_path.py`
- [x] Union-Find - `data_structures/union_find.py`
- [x] Trie - `data_structures/trie.py`
- [x] Segment Tree - `data_structures/segment_tree.py`
