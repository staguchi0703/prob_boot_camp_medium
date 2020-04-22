def resolve():
    '''
    code here
    '''

    A, B, C = [int(item) for item in input().split()]

    for i in range(B+1):
        if A * i % B == C:
            print('YES')
            break
    else:
        print('NO')


if __name__ == "__main__":
    resolve()
