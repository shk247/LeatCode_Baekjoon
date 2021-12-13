import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    end = n//2+2
    answer = 0 
    for i in range(1,end):
        tmp = 0
        for j in range(i, end):    
            tmp += j 
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
    print(answer+1)
                
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    start, end = 0, 1
    answer = 0 
    sum_number = 1
    
    while start < n//2+1:
        if sum_number<n:
            end+=1
            sum_number += end
        elif sum_number == n:
            answer += 1
            sum_number -= start
            end += 1
            start += 1
            sum_number += end
        else:
            sum_number -= start
            start += 1

if __name__=='__main__':
    mysolution()