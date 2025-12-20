### 기억하자
"""
heapify는 생각보다 오래 걸린다.
heap 구조를 계속 유지해야 할 것 같으면, 그냥 heappush O(log N)를 하는게 낫다.
heapify 할 array가 커지면, 오히려 heapify O(N)할 때 오래걸린다.
"""

import heapq as hq

from sys import stdin
input = stdin.readline

def print_minimum(arr):
    hq.heapify(arr)
    print(hq.heappop(arr))

def solve(cmds):
    arr = []
    for c in cmds:
        if (c == 0):
            if (len(arr) == 0):
                print(0)
            else:
                print(hq.heappop(arr))
        else:
            hq.heappush(arr, c)

if __name__=="__main__":
    n = int(input())
    cmds = []
    for _ in range(n):
        cmds.append(int(input()))
    solve(cmds)
