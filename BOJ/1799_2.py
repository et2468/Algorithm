import sys
sys.stdin = open('1799.txt')
def f(depth):
    global maxV
    if depth == n:
        max(maxV,sum(D))
    else:
        for spot in new_arr[depth]:
            i,j = spot
            k = N-1-i+j
            if D[k] == 0:
                D[k] = 1
                f(depth+1)
                D[k] = 0
                f(depth+1)
            else:
                f(depth+1)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxV=0
n = 2*N-1
new_arr = [[] for _ in range(n)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            new_arr[i+j].append((i,j))
D = [0]*n
f(0)
print(maxV)