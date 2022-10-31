import sys
sys.stdin = open('1520.txt')


def check(i,j):
     global cnt
     if record[i][j]:
          record[0][0] -= 1
          cnt += record[i][j]
          for a,b,idx in stack:
               if a!=i or b!=j:
                    record[a][b] += record[i][j]
          return True

M, N = map(int,input().split())    # M세로, N가로
arr = [list(map(int,input().split()))for _ in range(M)]
cnt = 0
record = [[0]*N for _ in range(M)]
record[-1][-1] = 1
visited = [[0]*N for _ in range(M)]
delta = [(0,1),(0,-1),(1,0),(-1,0)]
i,j,idx =0,0,0
stack = [(0,0,0)]
while stack:
     for d in range(idx,4):
          ni, nj = i+delta[d][0], j+delta[d][1]
          if 0<=ni<M and 0<=nj<N and visited[ni][nj] ==0 and arr[i][j]>arr[ni][nj] and record[ni][nj] != -1:
               stack.append((i,j,d+1))
               visited[i][j] = 1
               i,j,idx = ni, nj, 0 
               if check(ni,nj):
                    i, j, idx= stack.pop()
                    visited[i][j] = 0
                    
               break
     # 4방향 모두 갈곳이 없다
     else:
          if record[i][j] == 0:
               record[i][j] = -1
          i, j, idx= stack.pop()
          visited[i][j] = 0
print(cnt)
# 0, 1, 2, 3 /
# 우,좌,하,상