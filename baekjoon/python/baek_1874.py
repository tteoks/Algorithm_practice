from sys import stdin
input = stdin.readline

def solve(gt):
    stack = []
    res = ""
    cur = 1
    
    for target in gt:
        while (cur <= target):
            stack.append(cur)
            cur += 1
            res += "+"

        if (stack[-1] == target):
            stack.pop()
            res += "-"
        else:
            print("NO")
            return

    print("\n".join(res))
    return 

if __name__=="__main__":
    n = int(input())
    gt = []
    for _ in range(n):
        gt.append(int(input()))

    solve(gt)
