from sys import stdin

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr[:]
    
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i][1] < right[j][1]):
            res.append(left[i])
            i += 1
        elif (left[i][1] > right[j][1]):
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

def sort_yx(xy):
    x, y = xy[0], xy[1]
    return int(y) + int(x) / 1000000

def solve(arr):
    # res = merge_sort(arr)
    # res = sorted(arr, key=sort_yx)
    res = sorted(arr, key=lambda x: (x[1], x[0]))
    for r in res:
        print(" ".join(map(str, r)))

if __name__=="__main__":
    input = stdin.readline
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(tuple(map(int, input().split())))
    
    solve(arr)
