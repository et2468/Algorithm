import sys
sys.stdin = open("input.txt")

N = int(input())
DP = [1,1,1,1,1]
for i in range(1,N):
    t = [0,0,0,0,0]
    t[0] = (DP[2]+DP[3]+DP[4])%1000000007
    t[1] = (DP[3]+DP[4])%1000000007
    t[2] = (DP[0]+DP[4])%1000000007
    t[3] = (DP[0]+DP[1]+DP[4])%1000000007
    t[4] = (DP[0]+DP[1]+DP[2]+DP[3])%1000000007
    DP = t[:]
print(sum(DP)%1000000007)