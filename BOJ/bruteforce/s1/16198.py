import sys
sys.stdin = open('input.txt')

N = int(input())
marbles = list(map(int,input().split()))

max_total_energy = 0
def backtracking(depth, total_energy):
    global max_total_energy

    if depth == N-2:
        max_total_energy = max(max_total_energy, total_energy)
        return
    
    for i in range(1, len(marbles)-1):
        total_energy = total_energy + marbles[i-1] * marbles[i+1]
        now = marbles.pop(i)
        backtracking(depth+1, total_energy)
        marbles.insert(i,now)
        total_energy = total_energy - marbles[i-1] * marbles[i+1]
        
backtracking(0,0)
print(max_total_energy)