def resolve():
    '''
    code here
    '''
    N, P = [int(item) for item in input().split()]
    As = [int(item)%2 for item in input().split()]

    is_all_even = True
    for item in As:
        if item == 1:
            is_all_even = False
    
    res = 0
    if is_all_even:
        if P == 0:
            res = 2 ** N
        else:
            res = 0
    else:
        res = 2**(N-1)
    
    print(res)

if __name__ == "__main__":
    resolve()
