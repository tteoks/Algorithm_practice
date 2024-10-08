# 그리디 알고리즘 (Greedy algorithm)
"""
그리디 알고리즘은글로벌 최적을 찾기 위해 각 단계에서 로컬의 최적을 선택하는 알고리즘이다. (휴리스틱 문제 해결 알고리즘)
  * 바로 눈앞의 이익만을 좇는 알고리즘
  * 대부분의 경우 뛰어난 결과 도출에 실패, 드물게 최적해를 보장하기도 함
  * 그리디 알고리즘은 최적화 문제를 대상으로 수행
  * 최적해를 찾을 수 있다면 그것을 목표로 삼음
  * 최적해를 찾을 수 없는 경우, 그런대로 괜찮은 해를 찾는 것을 목표로 삼음
  * 대부분의 문제는 로컬 최적해를 찾는 탐욕스러운 방법으로는 문제를 해결할수 없음
  * 그러나 합리적인 시간 내에 최적에 가까운 답을 찾을 수 있다는 점에서 유용하다
"""
"""
그리디 알고리즘이 잘 작동하는 문제
  * 탐욕 선택 속성 (Greedy Choice Property)을 갖는 최적 부분 구조 (Optimal Substrcture) 문제들
  * 탐욕 선택 속성: 앞의 선택이 이후 선택에 영향을 주지 않는 것
  * 최적 부분 구조: 문제의 최적 해결 방법이 부분 문제에 대한 해결 방법으로 구성되는 경우
  * 즉, 그리디 알고리즘은 선택을 다시 고려하지 않음

그리디 알고리즘의 대표적인 문제해결
  * 최단 경로 문제: Dijkstra algorithm
  * 압축 알고리즘: Huffman Coding
  * 머신러닝 분야: 의사 결정 트리 (Decision Tree)


Greedy algorithm vs Dynamic algorithm
그리디 알고리즘은 최적 부분 구조 문제를 푼다는 점에서 동적 프로그래밍과 자주 비교함
하지만, 서로 풀수 있는 문제의 성격이 다르며 접근 방식 또한 다름
다이나믹 프로그래밍
하위 문제에 대한 최적의 솔루션을 찾음
이 결과들을 결합한 정보를 통해 전역 최적 솔루션을 선택

그리디 알고리즘
각 단계마다 로컬 최적해를 찾는 문제로 접근
문제를 더 작게 줄여나가는 형태로 접근
"""

# 그리디 알고리즘으로 풀수 있는 문제와 풀 수 없는 문제
"""
배낭 문제 (Knapsack Problem) -> 조합 최적화
배낭이 담을 수 있는 무게의 최대값 (15kg)이 정해져 있고, 짐이 (가치, 무게)가 존재할 때
짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록 짐을 고르는 방법

배낭 문제는 아래 2가지 문제 종류로 나뉠 수 있음
짐을 쪼갤 수 있는 분할 가능 배낭 문제 -> Greedy
짐을 쪼갤 수 없는 경우의 배낭 문제 -> Dynamic

동전 바꾸기 문제 (Coin-Change Problem)
동전 액수가 10원, 50원, 100원 배수 이상으로 증가하는 경우 그리디 알고리즘으로 풀 수 있음
ex) 160원을 거슬러 주기 위해 100원 1개, 50원 1개 10원 1개로 활용하는것
    - 80원이 있는 경우 FAIL -> BEST: 80원 2개 / Greedy: 100원 50원 10원

가장 큰 합 (트리에서 노드를 탐색하며 더하다 마지막에 가장 큰 합이 되는 경로 찾기)
정렬 되지 않은 트리의 경우 두 가지 간선 중 더 큰 경우를 따라감 -> FAIL
그리디 알고리즘으로 풀기 위해서는 이진 트리를 정렬하는 등 추가 작업 필요
"""

# 짐을 쪼갤 수 있는 분할 가능 배낭 문제 -> Greedy
def fractional_knapsack(carge):
    capacity = 15
    pack = []
    for c in carge:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value





























