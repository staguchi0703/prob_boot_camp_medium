def resolve():
    '''
    code here
    '''
    import collections
    N, M = [int(item) for item in input().split()]
    Xs = [int(item) for item in input().split()]
    if N < M:
        Xs.sort()
        ds = [Xs[i] - Xs[i-1] for i in range(1, M)]
        ds.sort()
        # print(ds)
        print(sum(ds[:M-N]))

    else:
        print(0)


if __name__ == "__main__":
    resolve()
