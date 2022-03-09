import sys 

def mysolution():
    input = sys.stdin.readline
    d, n = map(int, input().split())
    oven = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    answer = 0 
    
    for i in range(d-1, -1, -1):
        print()
        
def solution():
    input = sys.stdin.readline
    d, n = map(int, input().split())
    oven = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    
    for i in range(1, d):
        oven[i] = min(oven[i], oven[i-1])
        
    pizzaidx = 0 
    depth = d-1
    
    for i in range(d-1, -1, -1):
        if pizzaidx>=len(pizza):
            print(depth+1)
            return 
        if oven[i]>=pizza[pizzaidx]:
            pizzaidx+=1
            depth=i
    print(0)
    
if __name__=='__main__':
    mysolution()