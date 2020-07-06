def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]

    if K == 2:
        print(N-1)
    elif N == K:
        print(1)
    else:
        if (N-1) % (K-1) == 0:
            print((N-1)//(K-1))
        else:
            print((N-1)//(K-1) + 1)

if __name__ == "__main__":
    resolve()
