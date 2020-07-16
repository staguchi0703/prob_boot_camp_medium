def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [0] + [int(item) for item in input().split()] + [0]
    
    all_sum = 0
    prev = 0
    for i in range(N+2):
        all_sum += abs(As[i] - prev)
        prev = As[i]

    prev = As[0]
    for i in range(N):
        print(all_sum + abs(As[i] - As[i+2]) - (abs(As[i]-As[i+1]) + abs(As[i+1] - As[i+2])))

if __name__ == "__main__":
    resolve()
