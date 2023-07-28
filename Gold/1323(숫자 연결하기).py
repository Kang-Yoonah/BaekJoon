import sys
input = sys.stdin.readline
N, K = map(int, input().split())

ans, Nr = 1, N
R, r = set(), N%K
while r != 0:
    R.add(r)
    Nr = int(str(Nr)+str(N))
    r = Nr%K
    if r in R:
        ans = -1
        break
    ans += 1
print(ans)