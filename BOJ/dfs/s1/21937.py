import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
adjacency_dict = dict()
for m in range(M):
    end, start = map(int,input().split())
    if adjacency_dict.get(start) is None:
        adjacency_dict[start] = [end]
    else:
        adjacency_dict[start].append(end)

# print(adjacency_dict)
start_node = int(input())
visited = [start_node]
cnt = 0
def dfs(depth,node):
    global cnt
    if adjacency_dict.get(node) is None:
        return
    else:
        for nxt_node in adjacency_dict.get(node):
            if nxt_node not in visited:
                visited.append(nxt_node)
                cnt+=1
                dfs(depth+1,nxt_node)

dfs(0,start_node)
print(cnt)