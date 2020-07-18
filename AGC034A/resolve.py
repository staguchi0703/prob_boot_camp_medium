def resolve():
    '''
    code here
    '''
    N, A, B, C, D = [int(item) for item in input().split()]
    S = input()


    if C < D:
        is_goal = True
        for i in range(A, D+1):
            if S[i-1:i+1] == '##':
                is_goal = False
                break
    else:
        is_goal = False
        for i in range(A, C+1):
            if S[i-1:i+1] == '##':
                is_goal = False

            if B <= i <= D:
                if S[i-2:i+1] == '...' :
                    is_goal = True

    print('Yes') if is_goal else print('No')

if __name__ == "__main__":
    resolve()
