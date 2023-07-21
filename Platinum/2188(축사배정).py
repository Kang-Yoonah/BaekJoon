import sys
input = sys.stdin.readline

def match(i):            # 소가 원하는 축사로 넣기 시도
    if cow[i]:           # 축사를 찾는 과정에서 이미 방문한 소이면 False
        return False    
    cow[i] = True        # 지금 탐색하고 있는 소를 방문했다는 의미

    for num in like[i]:  # 소가 원하는 축사들에 대해 가능한지 탐색
        if shed[num] == -1 or match(shed[num]):      # 그 축사가 비어있거나, 축사에 들어있는 소가 다른 곳으로 옮겨갈 수 있을 때
            shed[num] = i      # 그 축사에 해당 소를 넣는다.
            return True        # 그리고 성공했다는 의미로 True
    return False               # 소가 원하는 축사 중에서는 들어갈 수 있는 축사가 없다.

N, M = map(int, input().split())
like = [list(map(int, input().split()))[1:] for _ in range(N)]
shed = [-1]*(M+1)

for i in range(N):
    cow = [False]*N
    match(i)

print(sum(map(lambda x : 1 if x>=0 else 0, shed)))