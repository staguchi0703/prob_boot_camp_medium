def resolve():
    '''
    code here
    '''
    S = input()
    N = len(S)

    res = 0
    for i in range(N):
        # print(S[i])
        if S[i] == 'U':
            res += N - (i+1)
            res += (N - (N - i)) * 2
        else:
            res += (N - (i+1)) * 2
            res += (N - (N - i))

    print(res)

if __name__ == "__main__":
    resolve()
