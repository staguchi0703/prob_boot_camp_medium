def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    queries = [[int(item)-1 for item in input().split()] for _ in range(M)]

    memo = [['w'] for _ in range(N)]
    memo[0] = ['r']
    is_first_0 = True
    for x, y in queries:
        if 'r' in memo[x]:
            memo[y] += ['r']
            if 'w' in memo[x]:
                memo[x].remove('w')
            else:
                memo[x].remove('r')
        else:
            memo[y] += ['w']
            memo[x].remove('w')
    res = 0
    for line in memo:
        for item in set(line):
            if item == 'r':
                res += 1
    print(res)



if __name__ == "__main__":
    resolve()
