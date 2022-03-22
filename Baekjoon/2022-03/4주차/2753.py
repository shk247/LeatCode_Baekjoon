import sys 

def mysolution():
    input = sys.stdin.readline
    year = int(input())
    
    if (year%400 == 0) or (year%4==0 and year%100!=0):
        print(1)
    else:
        print(0) 
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()