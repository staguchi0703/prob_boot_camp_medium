def resolve():
    '''
    code here
    '''
    S = input()
    N = len(S)
    res = 0
    for i in range(N//2):
        a = S[:i]
        b = S[i:2*i]
        if a == b:
            res = max(i,res)

        # print(a, b)

    print(res*2)
if __name__ == "__main__":
    resolve()
