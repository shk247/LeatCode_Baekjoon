import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
    for i in range(1, n+1):
        num_sum = i + sum(map(int, str(i)))
        if num_sum == n:
            print(i)
            break
    else:
        print(0)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    
    for i in range(1, n+1):
        num = sum(map(int, str(i)))
        num_sum = i + num
        if num_sum == n:
            print(i)
            break
        if i == n:
            print(0)

if __name__=='__main__':
    mysolution()