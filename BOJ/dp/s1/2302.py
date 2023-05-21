import sys
sys.stdin = open("input.txt")

N = int(input())
M = int(input())

DP = [0]*43
DP[0], DP[1] = 1, 1

for i in range(2,43):
    DP[i] = DP[i-1] + DP[i-2]

# print(DP)
vip = []
for i in range(M):
    vip.append(int(input())-1)


ans = 1
if M >= 1:
    start = 0
    for end in vip:
        sub = end - start
        ans*=DP[sub]
        start = end + 1
    sub = N - start
    ans *= DP[sub]
    print(ans)
else:
    print(DP[N])
