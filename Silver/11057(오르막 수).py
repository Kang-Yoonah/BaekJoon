N = int(input())
num, ans = [1]*10, 10
for _ in range(N-1):
    v, ans = ans, 0
    for j in range(10):
        ans += v
        v -= num[j]
        num[j] += v
    ans %= 10007
print(ans)