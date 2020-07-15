def resolve():
    '''
    code here
    '''
    N, C, K = [int(item) for item in input().split()]
    Ts = [int(input()) for _ in range(N)]
    Ts.sort()

    res = 0
    temp_psg = 0
    lim = Ts[0] + K

    for i in range(N):
        temp_psg += 1
        if Ts[i] > lim:
            res += 1
            temp_psg = 1
            lim = Ts[i] + K
        else:
            if temp_psg == C and i < N-1:
                res += 1
                temp_psg = 0
                lim = Ts[i+1] + K
        # print(Ts[i], temp_psg, res, lim)
    
    if temp_psg > 0:
        res += 1
    print(res)


if __name__ == "__main__":
    resolve()
