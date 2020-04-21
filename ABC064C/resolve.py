def resolve():
    '''
    code here
    最小値が0にはならないので1 or 計算結果にするとところが味噌
    上記を忘れていると全ての値が3200を超えていた時にバグる
    '''
    import collections

    N = int(input())
    A_list = [int(item)//400 for item in input().split()]

    cnt_dict = collections.Counter(A_list)

    res_low = 0
    res_high = 0
    for i in range(4800//400 + 1):
        if i <= 7:
            if cnt_dict[i] >= 1:
                res_low += 1
        else:
            res_high += cnt_dict[i]

    print(max(res_low, 1), res_low + res_high)

if __name__ == "__main__":
    resolve()
