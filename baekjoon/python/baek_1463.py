import sys

input = sys.stdin.readline



def solved(X):
    res = 0
    while X != 1:
        print(X)
        if X % 3 != 0:
            if (X - 1) % 3 == 0:
                res += 1
                X -= 1
                continue
        else:
            res += 1
            X //= 3
            continue

        if X % 2 == 0:
            res += 1
            X //= 2
            continue

        else:
            res += 1
            X -= 1
            continue

    return res
        
   


X = int(input(), 10)
print(solved(X))

