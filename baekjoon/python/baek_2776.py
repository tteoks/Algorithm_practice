from sys import stdin

input = stdin.readline

################## Solved by Binary Search (6392ms)
def binary_search(arr, val):
    if (len(arr) < 1):
        return -1

    left, right = 0, len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == val):
            return val
        
        if (arr[mid] > val):
            right = mid - 1
        else:
            left = mid + 1
    return -1
        

def solved(diary_1, diary_2):
    diary_1.sort()
    for v in diary_2:
        if (binary_search(diary_1, v) != -1):
            print("1")
        else:
            print("0")

    return 0

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = input()
        diary1 = input().strip().split(" ")

        M = input()
        diary2 = input().strip().split(" ")

        solved(diary1, diary2)


################## Solved by Set (1092ms)
from sys import stdin

input = stdin.readline


def solved(diary_1, diary_2):
    for v in diary_2:
        if (v in diary_1):
            print("1")
        else:
            print("0")

    return 0

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = input()
        diary1 = set(input().strip().split(" "))

        M = input()
        diary2 = input().strip().split(" ")

        solved(diary1, diary2)
