from sys import stdin
from bisect import bisect_left

input = stdin.readline

def solve(A, B):
    res = 0

    A.sort()
    B.sort()
    
    b_min = B[0]
    for va in A:
        if (va <= b_min):
            continue

        for vb in B:
            if (va > vb):
                res += 1
            else:
                break

    return res


if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().strip().split(" "))
        A = list(map(int, input().strip().split(" ")))
        B = list(map(int, input().strip().split(" ")))
        print(solve(A, B))
