def resolve():
    '''
    code here
    '''
    import collections
    n = int(input())
    As = collections.deque([int(item) for item in input().split()])
    bs = collections.deque()

    for i in range(n):
        if i % 2 == 0:
            bs.append(As.popleft())
        else:
            bs.appendleft(As.popleft())
    res =list(bs)
    if n % 2 == 1:
        res.reverse()

    print(*res)




if __name__ == "__main__":
    resolve()
