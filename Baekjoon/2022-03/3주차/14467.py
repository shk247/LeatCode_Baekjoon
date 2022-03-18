import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = {}
    answer =0 
    for _ in range(n):
        num, position = map(int, input().split())
        if num not in dict:
            dict[num]=position
        else:
            if dict[num] != position:
                answer += 1
                dict[num] = position
    print(answer)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()