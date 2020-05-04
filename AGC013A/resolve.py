def resolve():
    '''
    code here
    わざと短く切っても、結局同じ区切り数になるので、先頭から順に単調増加or単調減少を評価すればよい。
    
    '''

    N = int(input())
    A_list = [int(item) for item in input().split()]

    if N >=2:
        prev_num = A_list[0]
        new_list = []
        prev_direction = 0
        cnt = 1
        for item in A_list[1:]:
            # print(item - prev_num)
            if item != prev_num:
                if prev_direction == 1:
                    if item - prev_num >= 0:
                        pass
                    else:
                        cnt += 1
                        prev_direction = 0
                elif prev_direction == -1:
                    if item - prev_num <= 0:
                        pass
                    else:
                        cnt += 1
                        prev_direction = 0
                else:
                    if item - prev_num > 0:
                        prev_direction = 1
                    elif item - prev_num < 0:
                        prev_direction = -1
    
            prev_num = item
    else:
        cnt = 1

    print(cnt)

if __name__ == "__main__":
    resolve()
