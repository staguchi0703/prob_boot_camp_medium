def resolve():
    '''
    code here
    referece https://note.nkmk.me/python-set/
    和集合　積集合の使い方説明URL
    '''
    N = int(input())
    S = input()

    res = 0
    for i in range(1, N):
        A = set(S[:i])
        B = set(S[i:])

        res = max(res, len(A & B))

    print(res)

if __name__ == "__main__":
    resolve()
