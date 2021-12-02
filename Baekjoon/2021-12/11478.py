import sys 

def mysolution():
    input = sys.stdin.readline
    s = input().strip()
    total = []
    for i in range(1, len(s)+1):
        for j in range(0, len(s)+1-i):
            total.append(s[j:j+i])
    print(len(set(total)))
            
def solution():
    input = sys.stdin.readline
    s = input().strip()
    answer = set()
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            answer.add(s[i:j+1])
            
    print(len(answer))

if __name__=='__main__':
    mysolution()