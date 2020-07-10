def resolve():
    '''
    code here
    '''
    import collections
    S = input()

    cnt_S_dict = collections.Counter(S)

    num = len(S)
    if num == 1:
        res = 'YES'
    elif num == 2:
        if len(cnt_S_dict.keys()) == 2:
            res = 'YES'
        else:
            res = 'NO'
    else:
        if len(cnt_S_dict.keys()) <= 2:
            res = 'NO'
        else:
            num_a = cnt_S_dict['a']
            num_b = cnt_S_dict['b']
            num_c = cnt_S_dict['c']
            if abs(num_a - num_b) <= 1 and abs(num_a - num_c) <= 1 and abs(num_b - num_c) <= 1:
                res = 'YES'
            else:
                res = 'NO'
    
    print(res)




if __name__ == "__main__":
    resolve()
