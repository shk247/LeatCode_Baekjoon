import sys 

def mysolution():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    visit = list(map(int, input().split()))
     
    if sum(visit)==0:
        print("SAD")
        return
    
    period = []
    
    for i in range(0, n-x+1):
        period.append(sum(visit[i:i+x]))
        
    print(max(period))
    print(period.count(max(period)))
    
def solution():
    input = sys.stdin.readline
    n, x = map(int, input().split())
    visit = list(map(int, input().split()))
     
    if sum(visit)==0:
        print("SAD")
        return
    else:
        v = visit[:x]
        max_v = v
        cnt = 1
        for i in range(x, n):
            v += visit[i]
            v -= visit[i-x]
            
            if v>max_v:
                max_v = v
                cnt = 1
            elif v == max_v:
                cnt += 1
                
    print(max_v)
    print(cnt)
            
if __name__=='__main__':
    mysolution()