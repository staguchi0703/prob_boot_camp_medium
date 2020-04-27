def resolve():
    '''
    code here
    '''
    N = int(input())
    chp = [[int(item) for item in input().split()] for _ in range(N)]

    def root_chk(a, b):

        delta_t = b[0] - a[0]
        shortest_path = abs(a[1] - b[1]) + abs(a[2] - b[2])

        if shortest_path > delta_t:
            return False

        elif (delta_t - shortest_path) % 2 == 1:
            return False
        else:
            return True
    


    for i in range(N):

        if i == 0:
            # print(root_chk([0,0,0], chp[0]))
            if root_chk([0,0,0], chp[0]):
                pass
            else:
                print('No')
                break
        else:
            # print(root_chk(chp[i-1], chp[i]))
            if root_chk(chp[i-1], chp[i]):
                pass
            else:
                print('No')
                break
    else:
        print('Yes')


if __name__ == "__main__":
    resolve()
