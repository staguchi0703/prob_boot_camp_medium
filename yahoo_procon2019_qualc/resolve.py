def resolve():
    '''
    code here
    '''
    K, A, B = [int(item) for item in input().split()]

    if B - A > 1:
        num = K - (A - 1)
        print(num//2 * (B-A) + num%2 + A)
    else:
        print(1 + K)


if __name__ == "__main__":
    resolve()
