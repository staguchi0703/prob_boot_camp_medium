
def resolve():
    '''
    code here
    '''
    import collections

    N = int(input())
    A_list = [int(input()) for _ in range(N)]
    cnt_dic = collections.Counter(A_list)

    cnt = 0
    for v in cnt_dic.values():
        if v % 2 == 1:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
