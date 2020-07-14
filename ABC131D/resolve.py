def resolve():
    '''
    code here
    '''
    N = int(input())
    task = [[int(item) for item in input().split()] for _ in range(N)]

    task.sort(key=lambda x:x[1] ,reverse=True)


    res = task[0][1]
    for time, lim in task:
        if res > lim:
            res = lim
            
        res -= time

    print('Yes') if res >= 0 else print('No')

if __name__ == "__main__":
    resolve()
