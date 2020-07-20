def resolve():
    '''
    code here
    '''
    import math
    N = int(input())
    As = [int(item) for item in input().split()]

    
    res = 2000**2

    for mid in range(min(As), max(As)+1):
        temp_res = 0
        for item in As:
            temp_res += (item - mid)**2
        res = min(temp_res, res)
    print(res)

if __name__ == "__main__":
    resolve()
