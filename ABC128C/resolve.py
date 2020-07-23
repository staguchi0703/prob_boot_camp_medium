def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    tube_to_s = [[int(item) for item in input().split()] for _ in range(M)]
    mods = [int(item) for item in input().split()]

    to_list = [[] for _ in range(M)]

    for i in range(M):
        k, *arg = tube_to_s[i]
        to_list[i] += arg
    
    res = 0
    for i in range(2**N):
        temp_s = format(i, '0{}b'.format(N))
        for j in range(M):
            temp_on_num = 0
            for item in to_list[j]:
                temp_on_num += int(temp_s[item-1])
            
            if temp_on_num % 2 == mods[j]:
                pass
            else:
                break
        else:
            res += 1

    print(res)


if __name__ == "__main__":
    resolve()
