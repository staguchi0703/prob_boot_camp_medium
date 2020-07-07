def resolve():
    '''
    code here
    '''
    import bisect
    N = int(input())
    Ds = [int(item) for item in input().split()]
    M = int(input())
    Ts = [int(item) for item in input().split()]
    Ds.sort()
    Ts.sort()

    for item in Ts:
        index = bisect.bisect_left(Ds, item)
        if Ds[index] != item:
            print('NO')
            break
        else:
            Ds[index] = -1
    else:
        print('YES')
        



if __name__ == "__main__":
    resolve()
