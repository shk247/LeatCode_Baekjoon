import sys 

def mysolution():
    input = sys.stdin.readline 
    n = int(input())
    answer = [1,3,5,11,21] + [0]*(n-4)
    for i in range(5, n):
        answer[i] = answer[i-1] + answer[i-2] * 2
    print(answer[n-1]%10007)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()