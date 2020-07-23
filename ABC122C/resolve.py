def resolve():
    '''
    code here
    '''
    N, Q = [int(item) for item in input().split()]
    S = input()
    queries = [[int(item) for item in input().split()] for _ in range(Q)]

    memo = [0 for _ in range(N)]

    prev = S[0]
    for i in range(1, N):
        memo[i] = memo[i-1]
        if S[i] == 'C' and prev == 'A':
            memo[i] += 1
        prev = S[i]
    
    for l, r in queries:
        print(memo[r-1] - memo[l-1])




if __name__ == "__main__":
    resolve()
