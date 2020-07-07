def resolve():
    '''
    code here
    '''
    import math
    N, X = [int(item) for item in input().split()]
    xs = [int(item) for item in input().split()] + [X]
    xs.sort()

    if N > 2:
        res = math.gcd(xs[1] - xs[0], xs[2] - xs[0])

        for item in xs[3:]:
            res = math.gcd(res, item - xs[0])
    elif N == 2:
        res = math.gcd(xs[1] - xs[0], xs[2] - xs[0])
    else:
        res = xs[1] - xs[0]
    
    print(res)


if __name__ == "__main__":
    resolve()
