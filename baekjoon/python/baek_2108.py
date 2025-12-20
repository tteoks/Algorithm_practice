from collections import Counter
from sys import stdin
input = stdin.readline

def custom_merge_sort(arr):
    l = len(arr)
    if (l <= 1):
        return arr[:]

    mid = l // 2
    left = custom_merge_sort(arr[:mid])
    right = custom_merge_sort(arr[mid:])

    res = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i][1] > right[j][1]):
            res.append(left[i])
            i += 1
        elif (left[i][1] < right[j][1]):
            res.append(right[j])
            j += 1
        else:
            if (left[i][0] < right[j][0]):
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


def func_1(arr):
    return int(round(sum(arr) / len(arr), 0))

def func_2(arr):
    return round(arr[len(arr) // 2])

def func_3(arr):
    if len(arr) == 1:
        return arr[0]
    tmp = dict(Counter(arr))

    # cnt = [(x, y) for x, y in tmp.items()]
    # sorted_cnt = custom_merge_sort(cnt)
    
    sorted_cnt = sorted(tmp.items(), key=lambda x: (-x[1], x[0]))
    return sorted_cnt[1][0] if sorted_cnt[0][1] == sorted_cnt[1][1] else sorted_cnt[0][0]

def func_4(arr):
    return 0 if (len(arr) == 1) else arr[-1] - arr[0]

def solve(arr):
    sorted_arr = sorted(arr)
    print(func_1(sorted_arr))
    print(func_2(sorted_arr))
    print(func_3(sorted_arr))
    print(func_4(sorted_arr))


if __name__=="__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    solve(arr)
