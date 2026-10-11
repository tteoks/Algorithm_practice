from collections import defaultdict

def solution(participant, completion):

    dict_participants = defaultdict(int)
    answer = ''

    for p in participant:
        dict_participants[p] += 1

    for c in completion:
        dict_participants[c] -= 1

    for k, v in dict_participants.items():
        if(v >= 1):
            answer = k

    return answer


solution(["leo", "kiki", "eden"], ["eden", "kiki"])
