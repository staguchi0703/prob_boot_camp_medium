def resolve():
    '''
    code here
    '''
    from functools import lru_cache

    N, M = [int(item) for item in input().split()]
    As = [int(input()) for _ in range(M)]
    memo = [1 for _ in range(N+1)]

    for item in As:
        memo[item] = 0

    res_list = []
    for i in range(1,N+1):
        if i == 1 and memo[i] == 0:
            memo[i] = 0
            res_list.append(2)
        elif memo[i] == 0:
            memo[i] = 0
            res_list.append(memo[i-1])
        else:
            memo[i] += memo[i-1]
    else:
        res_list.append(memo[N])

    
    @lru_cache
    def cal(num):
        if num <= 1:
            return 0
        elif num == 2:
            return 1
        elif num == 3:
            return 2
        else:
            return cal(num-1) + cal(num-2)
    
    res = 1
    for item in res_list:
        res *= cal(item)
    print(res % (10**9 + 7))



if __name__ == "__main__":
    resolve()
