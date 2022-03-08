import sys 

def mysolution():
    input = sys.stdin.readline
    n, h = map(int, input().split())
    height = [int(input()) for _ in range(n)]
    
def solution():
    input = sys.stdin.readline
    n, h = map(int, input().split())
    
    top = [0]*(h+1)
    bottom = [0]*(h+1)
    for i in range(n):
        num = int(input())
        if i%2==0:
            bottom[h-num+1] += 1
        else:
            top[num] += 1
            
    for i in range(h-1, 0, -1):
        top[i] += top[i+1]
    for i in range(1, h+1):
        bottom[i] += bottom[i-1]
        
    total = [0]*(h+1)
    for i in range(1, h+1):
        total[i] = top[i] + bottom[i]
    
    total = total[1:]
    
    ans = min(total)
    print(ans, total.count(ans)) 
        
    
if __name__=='__main__':
    solution()