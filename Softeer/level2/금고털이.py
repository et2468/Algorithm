import sys

W, N = map(int,input().split())
KgOfPrice = [0]*10001
for _ in range(N):
    Mi, Pi = map(int,input().split())
    KgOfPrice[Pi] += Mi

answer = 0
for price in range(10000,-1,-1):
    if KgOfPrice[price] == 0:
        continue
    else:
        if KgOfPrice[price] >= W:
            answer += W * price
            break
        else:
            answer += KgOfPrice[price] * price
            W -= KgOfPrice[price]
print(answer)