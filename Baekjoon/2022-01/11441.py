import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    num_sum = [0]
    for num in nums:
        num_sum.append(num_sum[-1]+num)
        
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        print(num_sum[b]-num_sum[a-1])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()