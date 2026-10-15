import itertools

def solution(k, dungeons):
    answer = -1

    for n in itertools.permutations(dungeons):
        tmp_k = k
        tmp_answer = 0 
        for required, consumed in n:
            if (tmp_k < required):
                continue
            tmp_k -= consumed
            tmp_answer += 1
            answer = max(answer, tmp_answer)

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))
