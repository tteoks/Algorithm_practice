import heapq as hq

# def heap_sort(wait_times):
#     res = []
#     hq.heapify(wait_times)
#     while wait_times:
#         res.append(hq.heappop(wait_times))
# 
#     return res
#

def heap_sort(wait_times):
    res = []
    hq.heapify(wait_times)
    while wait_times:
        res.append(hq.heappop(wait_times))

    return res

def merge_sort(wait_times):
    l = len(wait_times)
    if l <= 1:
        return wait_times[:]

    mid = l // 2
    left = merge_sort(wait_times[:mid])
    right = merge_sort(wait_times[mid:])

    res = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res
            


def solve(n, wait_times):
    # sorted_times = sorted(wait_times)
    # sorted_times = heap_sort(wait_times)
    sorted_times = merge_sort(wait_times)
    res_times = []
    
    for idx in range(1, n + 1):
        res_times.append(sum(sorted_times[:idx]))

    print(sum(res_times))

if __name__=="__main__":
    n = int(input())
    wait_times = list(map(int, input().split()))

    solve(n, wait_times)
