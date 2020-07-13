def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    As = [int(item) for item in input().split()]

    cnt = collections.Counter(As)
    cnt = sorted(cnt.items(), reverse=True)
    # print(sorted(cnt.items(), reverse=True))
    edges = []
    lim = 0
    res = 0
    if len(cnt) >=2:
        for i, v in cnt:
            if v >= 4:
                edges.append(i)
                edges.append(i)
                lim += 2
            elif v>=2:
                edges.append(i)
                lim += 1

            if lim >= 2:
                res = edges[0]*edges[1]
                break
    print(res)

if __name__ == "__main__":
    resolve()
