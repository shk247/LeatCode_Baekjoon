import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        doc_num, doc = map(int, input().split())
        priority = list(map(int, input().split()))
        queue = deque()
        for i in range(doc_num):
            queue.append([i,priority[i]])
            
        priority.sort(reverse=True)
        priority = deque(priority)
        cnt = 0 
        while True:
            if queue[0][1] == priority[0]:
                cnt += 1
                if queue[0][0] == doc:
                    print(cnt)
                    break
                else:
                    queue.popleft()
                    priority.popleft()
            else:
                queue.append(queue.popleft())   
    
    
def solution():
    input = sys.stdin.readline
    test_case = int(input())
    
    for _ in range(test_case):
        n,m = list(map(int, input().split()))
        imp = list(map(int, input().split()))
        idx = list(range(len(imp)))
        idx[m] = 'target'
        
        order = 0 
        
        while True:
            if imp[0] == max(imp):
                order += 1
                
                if idx[0] == 'target':
                    print(order)
                    break
                else:
                    imp.pop(0)
                    idx.pop(0)
            else:
                imp.append(imp.pop(0))
                idx.append(idx.pop(0))
        

if __name__=='__main__':
    mysolution()