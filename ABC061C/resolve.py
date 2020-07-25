def resolve():
    '''
    code here
    '''

    N, K = [int(item) for item in input().split()]
    queries = [[int(item) for item in input().split()] for _ in range(N)]

    queries.sort(key=lambda x:x[0])

    temp_que = []
    for num, val in queries:
        temp_que = num
        K -= val
        if K <= 0:
            break

    print(temp_que)

if __name__ == "__main__":
    resolve()
