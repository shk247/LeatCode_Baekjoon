import sys 

def check(n):
    pre = r = -1
    while n != 0:
        n, r = divmod(n, 10)
        if pre>=r:
            return False
        pre = r 
    return True
    
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    if n>=1023:
        print(-1)
        return
    
    cnt = 0 
    for i in range(10000000000):
        ch = check(i)
        if ch:
            cnt += 1
        if cnt == n+1:
            print(i)
            break
        
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = []
    def add_digit(digit, num):
        if digit==1:
            nums.append(num)
        else:
            for i in range(num%10):
                add_digit(digit-1, num*10+i)
        
    def backtracking(digit):
        for i in range(digit-1, 10):
            add_digit(digit, i)
            
    for i in range(1, 11):
        backtracking(i)
    
    if n>=len(nums):
        print(-1)
    else:
        print(nums[n])
                

if __name__=='__main__':
    solution()