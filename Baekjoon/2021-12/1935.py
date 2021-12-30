import sys 
from collections import deque 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    expre = deque(input().strip())
    
    dict = {}
    for i in range(n):
        dict[chr(65+i)] = input().strip()
    
    for i in range(len(expre)):
        if expre[i] in dict.keys():
            expre[i] = dict[expre[i]]
            
    stack = [expre.popleft()]
    
    while expre or len(stack)!=1:
        if stack[-1].isdecimal() or '.' in stack[-1]:
            stack.append(expre.popleft())
        else:
            oper = stack.pop()
            right = stack.pop()
            left = stack.pop()
            stack.append(str(round(eval(left+oper+right), 2)))
    
    print("{:.2f}".format(float(stack[0])))
    
def solution():
    input = sys.stdin.readline
    n=int(input())
    str=input()
    nums=[0]*n
    for i in range(n):
        nums[i]=int(input())
    stack=[]

    for ch in str:
        if ch.isupper():
            stack.append(nums[ord(ch)-ord('A')])
        else:
            num2=stack.pop()
            num1=stack.pop()
            if ch=='+':
                stack.append(num1+num2)
            elif ch=='-':
                stack.append(num1-num2)
            elif ch=='/':
                stack.append(num1/num2)
            elif ch=='*':
                stack.append(num1*num2)
        print(f"{stack[0]:.2f}")
    
if __name__=='__main__':
    mysolution()