def resolve():
    '''
    code here
    '''
    import collections
    N, M = [int(item) for item in input().split()]
    edges = [[int(item) for item in input().split()] for _ in range(M)]
    
    # togo列をつくってappendに使う
    togo = [0 for _ in range(N+1)]
    for f, t in edges:
        togo[f] = t
    
    fp = [0 for _ in range(N+1)]
    fp[1] = 1
    que = collections.deque([1])
    is_found = False

    while que:
        node = que.popleft()
        print(node)
        if node == N:
            que = False
            is_found = True
        if fp[node]:
            pass
        else:
            que.append(togo[node])
            fp[que] = 1
            
    print('POSSIBLE') if is_found else print('IMPOSSIBLE')

if __name__ == "__main__":
    resolve()
