import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    cnt = 0 
    
    for _ in range(n):
        word = input().strip()
        stack = []
        
        for i in range(len(word)):
            if stack and stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])

        if not stack:
            cnt += 1
    print(cnt)

if __name__=='__main__':
    solution()