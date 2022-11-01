import sys
sys.stdin = open('2383.txt')

def exit(p1,p2):
    e1,e2 = exit_list
    
    ptoe1, ptoe2 =[],[]
    for pi,pj in p1:
        ptoe1.append(abs((pi-e1[0])+pj-e1[1]))
    for pi,pj in p2:
        ptoe2.append(abs((pi-e1[0])+pj-e1[1]))

def f(depth,i):
    p1,p2 = [],[]
    if depth == N:
        for a in range(N):
            if bit[a]:
                p1.append(people_list[a])
            else:
                p2.append(people_list[a])
        print(p1)
        print(p2)
        exit()
    else:
        bit[i] = 1
        f(depth+1,i+1)
        bit[i] = 0
        f(depth+1,i+1)

T = int(input())
for tc in range(1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    people_list = []
    exit_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people_list.append([i,j])
            elif arr[i][j] != 0:
                exit_list.append([[i,j]])
    
    
    # people_list / exit_list
    bit = [0]*N
    f(0,0)
    