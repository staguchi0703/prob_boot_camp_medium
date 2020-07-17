def resolve():
    '''
    code here
    '''
    N = int(input())
    ps = [int(item) for item in input().split()]


    temp_cnt = 0
    res = 0
    for i, item in enumerate(ps):
        if item == i+1:
            temp_cnt += 1
        else:
            if temp_cnt == 1:
                res += 1
                temp_cnt = 0

        if temp_cnt == 2:
            res += 1
            temp_cnt = 0
    else:
        if temp_cnt == 1:
            res += 1

    print(res)

if __name__ == "__main__":
    resolve()
