import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def match(i):
    for num in List[i]:
        if visited[num]: continue
        visited[num] = 1
        if Task[num] == -1 or match(Task[num]):
            Task[num] = i
            return True
    return False
for _ in range(int(input())):
    N, M = map(int,input().split())
    List = []
    for _ in range(M):
        a,b = map(int, input().split())
        List.append(list(range(a,b+1)))    

    Task = [-1]*(N+1)
    for i in range(M):
        visited = [0]*(N+1)
        match(i)
    print(sum(map(lambda x:1 if x>=0 else 0, Task)))