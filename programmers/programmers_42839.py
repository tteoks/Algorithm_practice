import itertools

def check_prime(n):
    if (n <= 1):
        return False

    for x in range(2, n):
        if (n % x == 0):
            return False
    return True
        

def solution(numbers):
    answer = 0
    num_list = [x for x in numbers]
    num_set = set()

    for i in range(len(num_list)):
        for x in itertools.permutations(num_list, i + 1):
            num_set.add(int("".join(x)))

    for x in num_set:
        if (check_prime(x)):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))
