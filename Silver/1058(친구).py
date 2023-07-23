import sys
input = sys.stdin.readline

def Count(f, F):
    for i in range(N):
        if F[i] == 'Y':
            f[i] = 'Y'
    return f        

N = int(input())
F = [list(input().strip()) for _ in range(N)]
ans = 0
for i in range(N):
    f = F[i].copy()
    for j in range(N):
        if F[i][j] == 'Y':
            f = Count(f, F[j])
    ans = max(ans, f.count('Y')-1)
print(ans)