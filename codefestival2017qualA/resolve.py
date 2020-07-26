def resolve():
    '''
    code here
    '''
    N, M, K = [int(item) for item in input().split()]
    
    is_found = False
    for i in range(N+1):
        for j in range(M+1):
            if i*M + j*N -2*j*i == K:
                is_found = True
                break
    print('Yes') if is_found else print('No')

if __name__ == "__main__":
    resolve()
