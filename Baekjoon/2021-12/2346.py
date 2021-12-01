import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    ballons = list(range(1,n+1))
    nums = list(map(int, input().split())) 
    answer = []
    idx = 0 
        
    while ballons:
        # print('idx=',idx, 'answer=',answer, 'ballons=',ballons, 'nums=',nums)
        answer.append(ballons.pop(idx))
        idx = nums.pop(idx) - 1
        print('idx=',idx, 'answer=',answer, 'ballons=',ballons, 'nums=',nums)
        
        if abs(idx)>len(ballons):
            idx %= len(ballons)
            print('idx=',idx)
            
    print(' '.join(answer))
        
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    ballons = list(range(1,n+1))
    nums = list(map(int, input().split())) 
    result = []
    
    idx = 0
    num = nums.pop(idx)
    result.append(ballons.pop(idx))
    
    while nums:
        if num<0:
            idx = (idx+num)%len(nums)
        else:
            idx = (idx+num-1)%len(nums)
            
        num = nums.pop(idx)
        result.append(ballons.pop(idx))
        
    print(' '.join(map(str,result)))

if __name__=='__main__':
    solution()