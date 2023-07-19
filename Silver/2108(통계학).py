import sys
from collections import Counter
input = sys.stdin.readline

def sol(N):
    num = sorted([int(input()) for _ in range(N)])
    mean = sum(num)/N
    print(0) if (mean > -1 and mean < 0) else print(f"{mean:.0f}")
    print(num[N//2])

    cnt = Counter(num).most_common(2)

    if len(num) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])

    print(num[N-1]-num[0])
sol(int(input()))