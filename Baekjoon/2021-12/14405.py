import sys 

def mysolution():
    s = input().replace('pi','1').replace('ka','1').replace('chu','1')
    if s.isdigit():
        print("YES")
    else:
        print("NO")
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()