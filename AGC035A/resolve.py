def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    As = [int(item) for item in input().split()]
    As.sort()
    temp_set = set(As)
    is_true = True
    # print(temp_set)
    if len(temp_set) == 1:
        if As[0] != 0:
            is_true = False
    elif len(temp_set) == 2:
        x_num = As.count(max(As))
        zero_num = As.count(0)
        if x_num != 2*zero_num:
            is_true = False

    elif len(temp_set) == 3:
        temp_cnt = collections.Counter(As)
        # print(temp_cnt)
        temp_set = list(set(As))
        if temp_cnt[temp_set[0]] == temp_cnt[temp_set[1]] == temp_cnt[temp_set[2]]:
            temp_keys = list(temp_cnt.keys())
            if temp_keys[0] ^ temp_keys[1] ^ temp_keys[2] == 0:
                is_true = True
            else:
                is_true = False
        else:
            is_true = False
        
    else:
        is_true = False

    print('Yes') if is_true else print('No')
        



if __name__ == "__main__":
    resolve()
