def resolve():
    '''
    code here
    '''
    N = int(input())
    a_list = [int(input()) for _ in range(N)]

    is_not_found = True
    cnt = 1
    idx = a_list[0] - 1
    while is_not_found:
        if idx == 1:
            is_not_found = False
            print(cnt)
        elif cnt >= N:
            is_not_found = False
            print(-1)
        
        idx = a_list[idx] - 1
        cnt += 1


if __name__ == "__main__":
    resolve()
