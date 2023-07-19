import sys
input = sys.stdin.readline
def sol(N):
    num1 = sorted(list(map(int, input().split())))
    num2 = sorted(list(map(int, input().split())), reverse=True)
    sum = 0
    for i,j in zip(num1,num2):
        sum += i*j
    print(sum)
sol(int(input()))