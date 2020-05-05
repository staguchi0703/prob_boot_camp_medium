def resolve():
    '''
    code here
    1x1の場合に気が付いて格納先を準備してやれるかがポイント
    境界条件は真っ先にチェックする必要あり
    '''

    N, M = [int(item) for item in input().split()]
    res_dict = {0:0, 1:0, 2:0, 3:0, 5:0, 8:0}

    if N > M:
        N, M = M, N
    
    if N == 1:
        if M >= 2:
            res_dict[1] = 2
            res_dict[2] = M -2
        else:
            res_dict[0] = 1 #1x1のとき一枚だけひっくり返る
    else:
        res_dict[3] = 4
        res_dict[5] = 2* (N - 2 + M - 2)
        res_dict[8] = M*N - (2*(N+M) -4)
    
    # print(res_dict)
    cnt = 0
    for i, v in res_dict.items():
        if i % 2 == 0:
            cnt += v

    print(cnt)            


if __name__ == "__main__":
    resolve()
