import heapq
import sys

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    heap = []
    for _ in range(n):
        num = int(input())
        if num == 0:
            if heap:
                check = [heapq.heappop(heap)[1]]
                
                if len(heap)>0:
                    while check[-1] == heap[0]:
                        check.append(heapq.heappop(heap)[1])
                    
                _min = min(check)
                check.remove(_min)
                    
                for i in range(len(check)):
                    heapq.heappush(heap, (abs(check[i]), check[i]))
                        
                print(_min)
            
            else:
                print(0)
            
        else:
            heapq.heappush(heap, (abs(num), num))

def solution():
    input = sys.stdin.readline
    n = int(input())
    q = []
    for i in range(n):
        a = int(input())
        if a!=0:
            heapq.heappush(q, (abs(a),a))
        else:
            if not q:
                print(0)
            else:
                print(heapq.heappop(q)[1])

if __name__=='__main__':
    mysolution()