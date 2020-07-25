def resolve():
    '''
    code here
    '''
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(10**6)

    N, M = [int(item) for item in input().split()]
    As = [int(input()) for _ in range(M)]
    memo = [False for _ in range(N+1)]

    for item in As:
        memo[item] = True

    res_list = []

    prev = 0
    for i in range(1,N+1):
        if memo[i] == True:
            res_list.append(i-1 - prev)
            prev = i+1
    else:
        if memo[N] == False and memo[N] == False:
            res_list.append(N - prev)

    @lru_cache
    def cal(num):
        if 0 <= num <= 1:
            return 1
        elif num == -1:
            return 0
        else:
            return cal(num-1) + cal(num-2)
    # print(res_list)
    res = 1
    for item in res_list:
        res *= cal(item)% (10**9 + 7)

    print(res % (10**9 + 7))



if __name__ == "__main__":
    resolve()
