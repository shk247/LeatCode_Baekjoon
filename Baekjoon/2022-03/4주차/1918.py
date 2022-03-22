import sys 

def mysolution():
    input = sys.stdin.readline
    s = input().rsplit()
    alpha = []
    symbol = []
    for i in s:
        if i.isalpha():
            alpha.append(i)
            
    
def solution():
    input = sys.stdin.readline
    a = input()
    stack = [] 
    res='' 

    for x in a:
        if x.isalpha(): 
            res+=x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x =='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    res+=stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res+=stack.pop()
                stack.pop()

    while stack:
        res += stack.pop()
        
    print(res)
    
if __name__=='__main__':
    mysolution()