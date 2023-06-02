import sys
from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    cnt = 1
    while queue:
        i,j = queue.popleft()
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and graph[ni][nj] == 1 and visited[ni][nj] == 0:
                cnt += 1
                visited[ni][nj] = 1
                queue.append((ni,nj))
    return cnt

N = int(input())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
for i in answer:
    print(i)