def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]
    Bs = [int(item) for item in input().split()]

    Ds = [a - b for a, b in zip(As, Bs)]

    cnt_minus = 0
    total_minus = 0
    minus_list = []

    cnt_plus_to_drow = 0
    plus_list = []

    for item in Ds:
        if item < 0:
            cnt_minus += 1
            total_minus += item
        else:
            plus_list.append(item)

    plus_list.sort()

    if sum(plus_list) >= abs(total_minus):
        for item in plus_list[::-1]:
            if total_minus >= 0:
                break

            total_minus += item
            cnt_plus_to_drow += 1

        print(cnt_minus + cnt_plus_to_drow)
    else:
        print(-1)

if __name__ == "__main__":
    resolve()
