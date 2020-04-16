def resolve():
    '''
    code here
    '''

    S = input()
    N = len(S)

    a_list = [ 0 for _ in range(N+1)]


    for i in range(N):
        if S[i] == '<':
            a_list[i+1] = a_list[i] + 1
    # print(a_list)
    for i in range(N):
        if S[-1*(i+1)] == '>':
            a_list[-1*(i+2)] = max(a_list[-1*(i+1)] + 1, a_list[-1*(i+2)])

    # print(a_list)
    
    print(sum(a_list))


if __name__ == "__main__":
    resolve()
