def resolve():
    '''
    code here
    '''
    S = [item for item in input()]

    res = 0
    w_cnt = 0
    for i, v in enumerate(S):
        if v == 'W':
            res += i+1
            w_cnt += 1

    res -= w_cnt * (w_cnt + 1)//2
    print(res)
if __name__ == "__main__":
    resolve()
