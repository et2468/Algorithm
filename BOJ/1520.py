import sys
sys.stdin = open('1520.txt')

def f(depth,i,j):
    global cnt
    if record[i][j]:
        cnt += record[i][j]
        for a,b in visited2:
            if a!=i or b!=j:
                record[a][b] += record[i][j]
        return    
    if depth > 900:
        return

    else:
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<M and 0<=nj<N and (ni,nj) and visited[ni][nj] == 0 and arr[i][j]>arr[ni][nj] and record[ni][nj] != -1:
                visited[ni][nj] = 1
                visited2.append((ni,nj))
                f(depth+1,ni,nj)
                visited[ni][nj] = 0
                # 경로를 찾지못하고 되돌아오는 경우일때
                visited2.pop()
                if record[ni][nj] == 0:
                    record[ni][nj] = -1
        return
M, N = map(int,input().split())    # M세로, N가로
arr = [list(map(int,input().split()))for _ in range(M)]
cnt = 0
record = [[0]*N for _ in range(M)]
record[-1][-1] = 1
visited = [[0]*N for _ in range(M)]
visited2 = [(0,0)]
f(0,0,0)
print(cnt)