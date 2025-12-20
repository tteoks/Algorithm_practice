from sys import stdin
input = stdin.readline

def merge_sort_B(B):
    l = len(B)
    if l <= 1:
        return B[:]

    mid = l // 2
    left = merge_sort_B(B[:mid])
    right = merge_sort_B(B[mid:])

    res = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i][1] > right[j][1]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(right[j:])
    res.extend(left[i:])

    return res


def solve(A, B):
    idx_B = []
    for idx, b in enumerate(B):
        idx_B.append((idx, b))

    sorted_A = sorted(A)
    sorted_idx_B = merge_sort_B(idx_B)
    # sorted_idx_B = sorted(idx_B, key=lambda x: (x[1], x[0]), reverse=True)

    res = 0
    for i in range(len(sorted_A)):
        res += (sorted_A[i] * sorted_idx_B[i][1])
    
    print(res)

if __name__=="__main__":
    n = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    solve(A, B)
    
