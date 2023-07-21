import sys
input = sys.stdin.readline
def prime():
    N = [1]*2000
    N[0]=N[1]=0
    for i in range(2,2000):
        if N[i]:
            for j in range(i*2,2000,i):
                N[j] = 0
    return N

def match(j):
    for num in List[j]:
        if visited[num]: continue
        visited[num]=1
        if Total[num] == -1 or match(Total[num]):
            Total[num]=j
            return True
    return False

n = int(input())//2
num = list(map(int, input().split()))
prime = prime()     

num1, num2 = [], []
v = num[0]%2
for value in num:
    if value%2 == v:
        num1.append(value)
    else:
        num2.append(value)

ans, List = [], []
if len(num1) == len(num2):
    for i in num1:
        tmp = []
        for j in num2:
            if prime[i+j]:
                tmp.append(j)
        List.append(tmp)

    for num in List[0]:   
        Total = {key:-1 for key in num2}
        for j in range(1,n):
            visited = {key:0 for key in num2}
            visited[num] = 1
            match(j)
        if sum(map(lambda x : 1 if x>=0 else 0, Total.values()))==n-1:
            ans.append(num)

if ans:
    print(' '.join(map(str,sorted(ans))))
else:
    print(-1)