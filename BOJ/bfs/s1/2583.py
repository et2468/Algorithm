import sys
from collections import deque
sys.stdin = open("BOJ/bfs/s1/input.txt")

N, M, K = map(int,input().split()) # 행 열 직-수
visited = [[0]*M for _ in range(N)]
for k in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            visited[y][x] = 1

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    area = 1
    visited[i][j] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if ni<0 or nj<0 or ni>=N or nj>=M:
                continue
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((ni,nj)) 
                area += 1
    return area
    
rectangle = 0
area = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            area.append(bfs(i,j))
            rectangle += 1
print(rectangle)
print(*sorted(area))