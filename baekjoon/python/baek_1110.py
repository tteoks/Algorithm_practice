N = int(input())

def calc(n):
    if n < 10:
        new = n * 10 + n
    else:
        first = n // 10
        second = n % 10
        tmp_sum = first + second
        new = second * 10 + (tmp_sum % 10)
    return new

def solve(n):
    res = 1
    org, tmp = n, n
    tmp_new = -1
    calc(n)

    while True:
        tmp_new = calc(tmp)
        if tmp_new == org:
            break
        tmp = tmp_new
        res += 1

    return res
print(solve(N))
