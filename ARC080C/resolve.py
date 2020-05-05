def resolve():
    '''
    code here
    二の倍数の扱いがポイント
    二の倍数は連続していないといけないので全てつなげる
    2でも4でもない数と2が隣り合うとNGなので必ず４と隣になる必要がある
    よって2でも4でもない数の個数＋１（二の塊）より4の数が多くなければならない
    '''
    N = int(input())
    A_list = [int(item) for item in input().split()]

    cnt_list = [0,0]

    for i in A_list:
        if i % 4 == 0:
            cnt_list[1] += 1
        elif i % 2 == 0:
            cnt_list[0] += 1

    is_flag = False

    if N - cnt_list[1] <= cnt_list[1]+1:
        is_flag = True
    
    else:
        if N - sum(cnt_list) <= cnt_list[1]:
            is_flag = True


    print('Yes') if is_flag else print('No')


if __name__ == "__main__":
    resolve()
