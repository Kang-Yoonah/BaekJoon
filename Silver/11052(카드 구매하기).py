import sys
input = sys.stdin.readline

N = int(input())
P = [0]+list(map(int, input().split()))
day = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,i+1):
        day[i] = max(day[i], day[i-j]+P[j])
print(day[N])