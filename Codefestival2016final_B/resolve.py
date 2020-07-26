def resolve():
    '''
    code here
    '''
    N = int(input())

    delta = 0
    if N > 1:
        for i in range(1, N+1):
            if (i-1)*i < 2*N < i*(i+1):
                delta = i*(i+1)//2 - N
                res_list = list(range(1, i+1))
                break
            elif 2*N == i*(i+1):
                res_list = range(1, i+1)
    else:
        res_list = [1]

    if delta > 0:
        # while delta > res_list[-1]:
        #     delta -= res_list[-1]
        #     del res_list[-1]

        res_list.remove(delta)    
    

    for item in res_list:
        print(item)



if __name__ == "__main__":
    resolve()
