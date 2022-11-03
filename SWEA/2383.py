import sys
sys.stdin = open('2383.txt')

def stairs(ptoe,k):
    if not ptoe:
        return 0
    time = 0
    stack = []
    Q = [0,0,0]
    while sum(ptoe):
        for i in range(len(ptoe)):
            if ptoe[i]:
                ptoe[i] -= 1
                if ptoe[i] == 0:
                    stack.append(k)

        for i in range(3):
            if Q[i]:
                Q[i] -= 1
                if stack and Q[i]==0:
                    Q[i] = stack.pop()
            elif Q[i] == 0 and stack:
                Q[i] = stack.pop()
        time += 1
        # print(time)
    while stack:
        for i in range(3):
            if Q[i]:
                Q[i] -= 1
                if stack and Q[i]==0:
                    Q[i] = stack.pop()
            elif Q[i] == 0 and stack:
                Q[i] = stack.pop()
        time += 1
    time += max(Q)
    return time

def exit(p1,p2):
    global minV
    e1,e2 = exit_list
    
    ptoe1, ptoe2 =[],[]
    for pi,pj in p1:
        ptoe1.append(abs(pi-e1[0])+abs(pj-e1[1]))
    for pi,pj in p2:
        ptoe2.append(abs((pi-e2[0]))+abs(pj-e2[1]))
    # print(ptoe1)
    # print(ptoe2)
    v1 = stairs(ptoe1,arr[e1[0]][e1[1]])
    v2 = stairs(ptoe2,arr[e2[0]][e2[1]])
    time = max(v1,v2)
    minV = min(minV,time)
def f(depth,i):
    p1,p2 = [],[]
    if depth == n:
        for a in range(n):
            if bit[a]:
                p1.append(people_list[a])
            else:
                p2.append(people_list[a])
        # print(p1)
        # print(p2)
        exit(p1,p2)
    else:
        bit[i] = 1
        f(depth+1,i+1)
        bit[i] = 0
        f(depth+1,i+1)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    people_list = []
    exit_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people_list.append([i,j])
            elif arr[i][j] != 0:
                exit_list.append([i,j])
    
    
    # people_list / exit_list
    minV = 9999
    n = len(people_list)
    bit = [0]*n
    f(0,0)
    print(f'#{tc+1}',minV+1)