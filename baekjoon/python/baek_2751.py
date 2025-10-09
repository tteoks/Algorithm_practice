import sys
import heapq

N = int(sys.stdin.readline())
ds = [int(sys.stdin.readline()) for _ in range(N)]

def sort_by_heapq(N, datas):
    res = []
    heapq.heapify(datas)
    for _ in range(N):
        res.append(heapq.heappop(datas))
    return res

def merge(left, right):
    l, r = 0, 0

    res = []
    while l < len(left) and r < len(right):
        if (left[l] < right[r]):
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res

def sort_by_merge(datas):
    if len(datas) <= 1:
        return datas
    
    mid = len(datas) // 2
    left = sort_by_merge(datas[:mid])
    right = sort_by_merge(datas[mid:])

    return merge(left, right)

def sort_by_internal(datas):
    return sorted(datas)

def solve(N, datas):
    res = sort_by_internal(datas)
    # res = sort_by_heapq(N, datas)
    # res = sort_by_merge(datas)
    for data in res:
        print(data)

solve(N, ds)
