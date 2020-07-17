def resolve():
    '''
    code here
    '''
    N = int(input())
    Ss = [input() for _ in range(N)]

    # MARCHで最大5C3の組み合わせ　（20）
    # 各組合せの中は (n, m, l) = n*m*l個
    # 全部足せばよい
    # collections.Counter()でイニシャル同じの集める


if __name__ == "__main__":
    resolve()
