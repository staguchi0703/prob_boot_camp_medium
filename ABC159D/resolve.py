def resolve():
    '''
    code here

    求めるものは
    　k番目のボールを除いた N−1個のボールから、書かれている整数が等しいような異なる2つのボールを選び出す方法
    言い換えて
    　①同じ数から2個選ぶ組み合わせの和
    　②k番目のボールを除いた N−1個のボールから、K番目のボールと同じ数を選ぶ数
        ※選ぶボールとペアになっていた個数を数え上げて引く
    　①-②
    
    '''

    import collections

    N = int(input())
    A_list = [int(item) for item in input().split()]
    origin_dict = collections.Counter(A_list)

    twopair_in_N = 0
    for i in origin_dict.values():
        twopair_in_N += i*(i-1)//2

    for j in range(N):
        deff = origin_dict[A_list[j]] -1

        print(twopair_in_N - deff)
    

if __name__ == "__main__":
    resolve()
