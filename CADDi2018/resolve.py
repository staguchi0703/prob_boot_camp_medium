def resolve():
    '''
    code here
    '''
    import collections
    import copy

    N, P = [int(item) for item in input().split()]
    P_org = copy.deepcopy(P)

    fact_list = [1]

    cnt = 2
    while P > 1 and cnt**2 <= P:
        if P % cnt == 0:
            fact_list.append(cnt)
            P //= cnt
        else:
            cnt += 1
    fact_list.append(P)

    if N == 1:
        res = P_org
    else:
        cnt_num = collections.Counter(fact_list[1:])
        res_list = []
        for i, v in cnt_num.items():
            if v//N > 0:
                res_list.append(i**(v//N))
        
        res = 1
        for item in res_list:
            res *= item
    print(res)

if __name__ == "__main__":
    resolve()

