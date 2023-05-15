import sys
from collections import deque
sys.stdin = open("BOJ/dfs/input.txt")

def bfs(y,x,color):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1
    cnt = 1
    while queue:
        y,x = queue.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=Y or nx>=X:
                continue
            if visited[ny][nx] == 0 and battle_area[ny][nx] == color:
                queue.append((ny,nx))
                visited[ny][nx] = 1
                cnt += 1
    return cnt

X, Y = map(int,input().split())
battle_area = [list(input()) for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]
me = 0
enemy = 0
for y in range(Y):
    for x in range(X):
        if visited[y][x] == 0:
            cnt = bfs(y,x,battle_area[y][x])
            if battle_area[y][x] == "W":
                me += cnt**2
            else:
                enemy += cnt**2
print(me, enemy)