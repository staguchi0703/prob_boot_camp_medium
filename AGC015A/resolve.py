def resolve():
    '''
    code here

    パターンを書いてみると、とり得る最大値と最小値の間の数はすべて表現できることが分かる。
    ※ちょっとずつオーバラップするので
    よって最大値と最小値の間の数の個数を計算して解となる
    　最大値 - 最小値　+ 1　（0から10まで１１個のイメージの計算）

    '''
    N, A, B = [int(item) for item in input().split()]

    if A <= B:
        if N >=3:
            res = (N-1)*B + A - ((N-1)*A + B) + 1

        elif N == 2:
            res = 1
        else:
            if A == B:
                res = 1
            else:
                res = 0
    else:
        res = 0

    print(res)

if __name__ == "__main__":
    resolve()
