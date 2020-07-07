def resolve():
    '''
    code here
    '''
    N = int(input())
    hs = [int(item) for item in input().split()]

    cnt = 0
    flag = False
    while any(hs):
        # print(hs)
        for i in range(N):
            if hs[i] > 0:
                flag = True
                hs[i] -= 1
            else:
                if flag:
                    cnt += 1
                    flag = False
        else:
            if flag:
                cnt += 1
            flag = False

    print(cnt)



if __name__ == "__main__":
    resolve()
