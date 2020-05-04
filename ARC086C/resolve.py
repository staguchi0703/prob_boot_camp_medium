def resolve():
    '''
    code here
    '''
    import collections
    N, K = [int(item) for item in input().split()]
    A_list = [int(item) for item in input().split()]

    cnt_dict = collections.Counter(A_list)

    temp_dict = sorted(cnt_dict.items(), key=lambda x:x[1])

    delta = len(cnt_dict) - K

    if delta > 0:
        res = 0
        cnt = 0
        for i, v in temp_dict:
            if cnt < delta:
                res += v
                cnt += 1
            else:
                break
    else:
        res = 0

    print(res)
if __name__ == "__main__":
    resolve()
