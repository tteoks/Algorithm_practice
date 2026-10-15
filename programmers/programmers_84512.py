import itertools
from bisect import bisect_left

WORD="AEIOU"

def solution(word):
    answer = 0
    word_dict = []
    for i in range(1, len(WORD) + 1):
        for n in itertools.product(WORD, repeat=i):
            word_dict.append("".join(n))

    word_dict.sort()
    answer = bisect_left(word_dict, word) + 1
            
    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
