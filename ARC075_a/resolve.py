def resolve():
    '''
    code here
    '''

    N = int(input())
    S_list = [int(input()) for _ in range(N)]
    all_sum = sum(S_list)

    if all_sum % 10 == 0:
        no_10_nums = [item for item in S_list if item % 10 != 0]
        if no_10_nums:
            res =  all_sum - min(no_10_nums)
        else:
            res = 0
        
    else:
        res = all_sum

    
    print(res)

if __name__ == "__main__":
    resolve()
