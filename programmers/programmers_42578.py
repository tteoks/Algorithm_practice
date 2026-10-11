from collections import defaultdict

def solution(clothes):
    answer = 0

    num_t = defaultdict(int)
    for _, t in clothes:
        num_t[t] += 1

    num_comb = 1
    for n in num_t.values():
        num_comb *= (n + 1)
    answer += num_comb

    return answer - 1


# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["a1", "A"], ["a2", "A"],["b1", "B"],["b2", "B"],["b3", "B"],["c1", "C"]]))
