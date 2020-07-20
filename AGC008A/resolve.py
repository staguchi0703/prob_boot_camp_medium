def resolve():
    '''
    code here
    '''
    x, y = [int(item) for item in input().split()]
    res = 0

    if x < 0 and abs(y) - abs(x) >= 0:
        res += 1
    elif x > 0 and abs(y) - abs(x) <= 0:
        res += 1

    res += abs(abs(x) - abs(y))


    if y > 0 and abs(y) - abs(x) < 0:
        res += 1
    elif y < 0 and abs(y) - abs(x) > 0:
        res += 1

    print(res)

if __name__ == "__main__":
    resolve()
