def resolve():
    '''
    code here
    '''
    W, H, x, y = [int(item) for item in input().split()]

    if 2*x == W and 2*y == H:
        res = 1
    else:
        res = 0

    print(W*H/2, res)


if __name__ == "__main__":
    resolve()
