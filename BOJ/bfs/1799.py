import sys
sys.stdin = open('1799.txt')

def 전처리(spot):
     n = len(spot)
     bit = [0]*n
     d1 = [0]*(2*N-1)
     d2 = [0]*(2*N-1)
     
     f(0,spot,n,bit,d1,d2)

def f(depth,spot,n,bit,d1,d2):
     global maxV
     if depth == n:
          maxV = max(maxV,sum(bit))
     
     else:
          i,j = spot[depth]
          k, l = N-1-i+j, i+j
          if d1[k] == 0 and d2[l] ==0:
               bit[depth] = 1
               d1[k], d2[l] = 1, 1
               f(depth+1,spot,n,bit,d1,d2)
               bit[depth] = 0
               d1[k], d2[l] = 0, 0
               f(depth+1,spot,n,bit,d1,d2)
          else:
               f(depth+1,spot,n,bit,d1,d2)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxV = 0
black = []
white = []
for i in range(N):
     for j in range(N):
          if arr[i][j] == 1:
               if (i+j)%2:
                    black.append((i,j))
               else:
                    white.append((i,j))
전처리(white)
v1 = maxV
maxV = 0
전처리(black)
v2 = maxV
print(v1+v2)
