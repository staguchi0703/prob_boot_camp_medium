def resolve():
    '''
    code here
    '''
    X = int(input())
    memo = 0
    res = 0
    for i in range(1, X+3):
        memo += i
        if memo >= X:
            res = i
            break
    print(res)

if __name__ == "__main__":
    resolve()
