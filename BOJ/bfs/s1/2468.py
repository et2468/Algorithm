import sys
from collections import deque
sys.stdin = open("s1/2468.txt")

N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]

def bfs(i,j,inUndation):
    queue = deque()
    queue.append((i,j))
    while queue:
        i, j = queue.popleft()
        for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni, nj = i + di, j +dj
            if ni>=N or ni<0 or nj>=N or nj<0: 
                continue
            if visited[ni][nj] == 0 and area[ni][nj] > inUndation:
                visited[ni][nj] = 1
                queue.append((ni,nj))

def find_safety_zone(inUndation):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > inUndation and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i,j,inUndation)
                cnt += 1
                print(visited,inUndation,cnt)
    return cnt

max_cnt = 1
inUndation = 1
while True:
    visited = [[0]*N for _ in range(N)]
    cnt = find_safety_zone(inUndation)
    if cnt == 0:
        break
    elif max_cnt < cnt:
        max_cnt = cnt
    inUndation += 1
print(max_cnt)
    