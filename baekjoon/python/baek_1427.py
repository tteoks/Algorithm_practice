import heapq as hq

def rev_merge_sort(arr):
    l = len(arr)
    if l <= 1:
        return arr
    
    mid = l // 2
    left = rev_merge_sort(arr[:mid])
    right = rev_merge_sort(arr[mid:])

    res = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if (left[i] > right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])

    return res


def rev_heap_sort(arr):
    minus_arr = [c * -1 for c in arr]
    res = []
    hq.heapify(minus_arr)
    while minus_arr:
        res.append(hq.heappop(minus_arr) * -1)

    return res

def solve(arr):
    # sorted_arr = sorted(arr, reverse=True)
    # sorted_arr = rev_heap_sort(arr)
    sorted_arr = rev_merge_sort(arr)
    for e in sorted_arr:
        print(e, end="")
    print()

if __name__=="__main__":
    in_arr = input()
    arr = [int(c) for c in in_arr]
    solve(arr)
