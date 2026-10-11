def solution(nums):
    poke_set = set(nums)
    num_chance = len(nums) // 2
    answer = 0

    answer = min(len(poke_set), num_chance)

    return answer

print(solution([3, 3, 3, 2, 2, 4]))
