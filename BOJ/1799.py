import sys, itertools
sys.stdin = open('1799.txt')

def check(temp):
     n = len(temp)
     for i in range(n):
          for j in range(i+1,n):
               if bit[i] and bit[j]:
                    x1,y1 = temp[i]
                    x2,y2 = temp[j]
                    if abs(x1-x2) == abs(y1-y2):
                         return False
     return True
          


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxV = 0
spot = []
for i in range(N):
     for j in range(N):
          if arr[i][j] == 1:
               spot.append((i,j))

n = len(spot)
idxs = [i for i in range(n)]
sub_cnt = 0
my_true = True
while my_true and n:
     for i in list(itertools.combinations(idxs,sub_cnt)):
          bit = [1]*n
          temp = spot[:]
          for j in i:
               bit[j] = 0
          if check(temp):
               my_true = False
               break
     sub_cnt += 1
print(sub_cnt)