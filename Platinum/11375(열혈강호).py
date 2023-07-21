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

N, M = map(int,input().split())
List = []
for _ in range(N):
    LIST = list(map(int, input().split()))
    LIST.pop(0)
    List.append(LIST)

Task = [-1]*(M+1)
for i in range(N):
    visited = [0]*(M+1)
    match(i)
print(sum(map(lambda x:1 if x>=0 else 0, Task)))