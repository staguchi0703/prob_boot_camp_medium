def resolve():
    '''
    code here
    '''
    import collections
    N, M = [int(item) for item in input().split()]
    Xs = [int(item) for item in input().split()]
    if N < M:
        Xs.sort()
        memo = N-1
        prev = Xs[0]
        for i in range(1, M):
            memo += min(Xs[i] - prev, N-1)
            prev = Xs[i]
        print(Xs[-1] - Xs[0] - memo)
            
    else:
        print(0)


if __name__ == "__main__":
    resolve()
