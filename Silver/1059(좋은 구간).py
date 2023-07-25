import sys
input = sys.stdin.readline

def sol(N):
    s = sorted(list(map(int, input().split())))
    n = int(input())
    
    ind = 0
    for i in range(N):
        if s[i] >= n:
            ind = i
            break
    if s[ind] == n: print(0)
    else:
        if ind==0: S=1
        else: S=s[ind-1]+1
        E, ans = s[ind]-1, 0
        while S != n+1:
            ans += ((E-S)-(n-S-1))
            S += 1
        print(ans-1)
sol(int(input()))