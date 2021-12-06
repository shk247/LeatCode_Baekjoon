import sys 
import re
from collections import deque

def mysolution():
    # input = sys.stdin.readline
    while True:
        line = input()
        if line == '.':
            return
        line = ''.join(re.findall('\W+', line))
        line = ''.join(re.findall('\S+', line))
        
        if not line:
            print("yes")
            continue        
        
        line = deque(line[:-1])
        stack = []
        
        while line:
            tmp = line.popleft()
            if tmp == '(' or tmp == '[':
                stack.append(tmp)
            elif len(stack)==0:
                print("no")
                break
            
            if tmp == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print("no")
                    break
            elif tmp == ']':            
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print("no")
                    break
        else:
            if stack:
                print('no')
            else:
                print('yes')
            
    
def solution():
    while True:
        s = input()
        if s=='.':
            break
        stack = []
        temp = True
        
        for i in s:
            if i=='(' or i=='[':
                stack.append(i)
            elif i==')':
                if not stack or stack[-1] == '[':
                    temp = False
                    break
                elif stack[-1]=='(':
                    stack.pop()
            elif i==']':
                if not stack or stack[-1] == '(':
                    temp = False
                    break
                elif stack[-1]=='[':
                    stack.pop()
        if temp == True and not stack:
            print('yes')
        else:
            print('no')      

if __name__=='__main__':
    mysolution()