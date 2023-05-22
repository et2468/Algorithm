import sys
sys.stdin = open("input.txt")

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
# print(board)
can_go = [[0]*N for _ in range(N)]
can_go[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(can_go[i][j])
        if can_go[i][j] != 0 and 0<=i+board[i][j]<N:
            can_go[i+board[i][j]][j] += can_go[i][j]
        if can_go[i][j] != 0 and 0<=j+board[i][j]<N:
            can_go[i][j+board[i][j]] += can_go[i][j]

