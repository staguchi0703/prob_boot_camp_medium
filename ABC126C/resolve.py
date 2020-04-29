def resolve():
    '''
    code here

    コイン振りの条件をちゃんと読む
    　K-1だと振る
    　K以上だと振らない
    　コインをまったく降らないでwinになる場合がある
    '''
    import math
    N, K = [int(item) for item in input().split()]

    res = 0

    for i in range(1,N+1):
        for n in range(int(math.log2(K))+3):
            if i * 2 ** n >= K:
                res += 1/N * 2 ** (-1 * n)
                break

        # print(i, n, res)
    print(res)

if __name__ == "__main__":
    resolve()
