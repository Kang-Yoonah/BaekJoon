import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))
odd_sum = [0]*N
even_sum = [0]*N
odd = even = 0
for i in range(0,N):
    if i % 2:
        even += card[-i]
        even_sum[-i] = even
    else:
        odd += card[i]
        odd_sum[i] = odd 

result = [even_sum[1], odd_sum[N-2]]
last = card[-1]
for i in range(0,N-2,2):
    result.append(odd_sum[i]+even_sum[i+3])
    result.append(odd_sum[i]+even_sum[i+1]-last)
print(max(result))
