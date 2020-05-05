def resolve():
    '''
    code here
    '''
    N = int(input())
    s = input()
    t = input()

    cnt = 0
    for i in range(N):
        if i == 0:
            if s[-1] == t[0]:
                cnt = 1
        else:
            if s[-1* (i+1):] == t[:(i+1)]:
                cnt = i + 1
    
    print(2*N - cnt)

if __name__ == "__main__":
    resolve()
