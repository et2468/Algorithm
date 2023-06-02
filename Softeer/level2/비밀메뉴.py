import sys
input = sys.stdin.readline

M, N, K = map(int,input().split())
target = list(map(int,input().split())) # M길이
gene = list(map(int,input().split())) # N길이

for i in range(N-M+1):
    cnt = 0
    for j in range(M):
        if target[j] == gene[i+j]:
            cnt+=1
    if cnt == M:
        print("secret")
        break
else:
    print("normal")