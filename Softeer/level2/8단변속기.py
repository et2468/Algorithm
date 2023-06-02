import sys

numbers = list(map(int,input().split()))

changes = 0
for i in range(1,8):
    if numbers[i-1] == numbers[i]-1:
        changes += 1
    elif numbers[i-1] == numbers[i]+1:
        changes -= 1
    else:
        break

if changes == 7:
    print("ascending")
elif changes == -7:
    print("descending")
else:
    print("mixed")