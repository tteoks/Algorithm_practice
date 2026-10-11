from collections import defaultdict

def solution(phone_book):
    prefix_hash = defaultdict(list)
    answer = True

    for p in phone_book:
        prefix_hash[p[0]].append(p)
    
    for v in prefix_hash.values():
        v.sort()

    for v in prefix_hash.values():
        if (len(v) == 1):
            continue

        for i in range(len(v) - 1):
            if (v[i + 1].startswith(v[i])):
                answer = False
                break

    return answer

print(solution(["119", "97674223", "1234", "1195524421"]))
