def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    students = [[int(item) for item in input().split()] for _ in range(N)]
    cps = [[int(item) for item in input().split()] for _ in range(M)]

    for i in range(N):
        min_dist = 10**9
        min_dist_index = 0
        for j in range(M):
            x_dist = abs(students[i][0] - cps[j][0])
            y_dist = abs(students[i][1] - cps[j][1])
            man_dist = x_dist + y_dist

            if min_dist > man_dist:
                min_dist = man_dist
                min_dist_index = j

        print(min_dist_index+1)

if __name__ == "__main__":
    resolve()
