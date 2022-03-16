from collections import deque
import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    answer = [0]*n
    start = 0 
    end = n-1
    for num in nums:
        # 맨 위 카드
        if num==1:
            answer[start]=n
            start+=1
        # 위에서 두 번째 카드
        elif num==2:
            idx = start+1
            while answer[idx]!=0:
                idx+=1
            answer[idx]=n
        # 맨 아래 카드 
        elif num==3:
            answer[end]=n
            end-=1
        n-=1
    print(*answer)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    conditions = deque(list(map(int, input().split())))
    after = deque([i for i in range(1, n+1)])
    answer = deque()
    while conditions:
        condition = conditions.pop()
        num = after.popleft()
        if condition==1:
            answer.appendleft(num)
        elif condition==2:
            answer.insert(1, num)
        else:
            answer.append(num)
    print(*answer)
    
if __name__=='__main__':
    mysolution()