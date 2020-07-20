def resolve():
    '''
    code here
    '''
    N = int(input())

    num_lists = [[int(item) for item in input().split()] for _ in range(N)]

    res = 0

    for a, b in num_lists[::-1]:
        temp_mod = (a + res ) % b
        if temp_mod > 0:
            res += b - temp_mod

    print(res)

if __name__ == "__main__":
    resolve()
