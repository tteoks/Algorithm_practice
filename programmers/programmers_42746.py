def solution_1(numbers):
    answer = ''
    str_num = list(map(str, numbers))

    str_num.sort(reverse=True, key=lambda x: x*4)
    answer = "".join(str_num)
    
    if (str_num[0] == '0'):
        return '0'

    return answer

import functools 

def solution(numbers):
    str_num = list(map(str, numbers))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    str_num.sort(key=functools.cmp_to_key(compare), reverse=True)

    if (str_num[0] == '0'):
        return '0'

    answer = "".join(str_num)
    return answer




print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))
print(solution([1000, 100, 10, 1]))
print(solution([0, 0, 0, 0]))
