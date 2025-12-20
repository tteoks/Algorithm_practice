import heapq as hq

from sys import stdin
input = stdin.readline

def heap_sort(arr):
    res = []
    hq.heapify(arr)
    while arr:
        res.append(hq.heappop(arr))

    return res

def merge_sort(arr):
    l  = len(arr)
    if l <= 1:
        return arr[:]

    mid = l // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

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

def solve(arr):
    sum_arr = sum(arr)
    del_num = sum_arr - 100

    f1, f2 = 0, 0
    for idx in range(len(arr)):
        f1 = arr[idx]
        f2 = del_num - f1
        if f2 <= 0:
            continue

        if f2 in arr[idx + 1:]:
            break
    arr.remove(f1)
    arr.remove(f2)

    # res = sorted(arr)
    # res = heap_sort(arr)
    res = merge_sort(arr)
    print("\n".join(map(str, res)))
    
    return res

if __name__=="__main__":
    arr = []
    for i in range(9):
        arr.append(int(input()))
    solve(arr)
