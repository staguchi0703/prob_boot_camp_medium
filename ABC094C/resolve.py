def resolve():
    '''
    code here
    '''
    N = int(input())
    Xs = [int(item) for item in input().split()]

    sorted_xs = sorted(Xs)

    for item in Xs:
        if item <= sorted_xs[(N-1)//2]:
            print(sorted_xs[N//2])
        else:
            print(sorted_xs[(N-1)//2])

if __name__ == "__main__":
    resolve()
