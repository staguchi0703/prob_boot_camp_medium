def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    cnt = 0
    is_not_found = True
    while is_not_found:
        for i in range(N):
            if As[i] % 2 == 0:
                As[i] //= 2
            else:
                is_not_found = False
                break
        else:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    resolve()
