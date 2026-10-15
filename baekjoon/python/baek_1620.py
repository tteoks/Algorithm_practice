from sys import stdin

input = stdin.readline

def solve():
    print("solve")

if __name__=="__main__":
    n, m = map(int, input().split(' '))

    print(n, m)
    mon_dict = []
    for idx in range(1, n + 1):
        mon_dict.append((idx, input().rstrip()))

    req = []
    for _ in range(m):
        req.append(input().rstrip())
    print("-----------")

    print(mon_dict)
    print(req)

