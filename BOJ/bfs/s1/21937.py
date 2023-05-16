import sys
sys.stdin = open("input.txt")
from collections import deque
N, M = map(int, input().split())
adjacency_dict = dict()
for m in range(M):
    end, start = map(int,input().split())
    if adjacency_dict.get(start) is None:
        adjacency_dict[start] = [end]
    else:
        adjacency_dict[start].append(end)

start_node = int(input())
cnt = 0

def bfs(node):
    global cnt
    queue = deque()
    queue.append(node)
    visited = [0]*(N+1)
    visited[node] = 1
    while queue:
        start = queue.popleft()
        if adjacency_dict.get(start) is None:
            continue
        for end in adjacency_dict.get(start):
            if visited[end] == 0:
                queue.append(end)
                visited[end] = 1
                cnt+=1
bfs(start_node)
print(cnt)
